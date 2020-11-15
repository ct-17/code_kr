<template>
  <div class="row">
    <div class="col-sm-12 card pt-4">
      <div class="row">
        <div class="col-sm-3 pr-0">
          <div class="input-group input-group-sm">
            <span class="input-group-addon">Merchant name</span>
            <input type="text" class="form-control" v-model="searchForm.merchant_name">
          </div>
        </div>
        <div class="col-sm-3 pr-0">
          <div class="input-group input-group-sm">
            <span class="input-group-addon">Merchant Abbreviation</span>
            <input type="text" class="form-control" v-model="searchForm.abbreviation">
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-3 pr-0">
          <div class="input-group input-group-sm">
            <span class="input-group-addon" style="min-width: 8.8em">Language</span>
            <select class="form-control" v-model="searchForm.language">
              <option
                class="select-default"
                v-for="item in comboBoxLanguage"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              >
              </option>
            </select>
          </div>
        </div>
        <div class="col-sm-3 pr-0">
          <div class="input-group input-group-sm">
            <span class="input-group-addon" style="min-width: 11.8em">Status</span>
            <select class="form-control" v-model="searchForm.status">
              <option :value=1>Active</option>
              <option :value=2>InActive</option>
            </select>
          </div>
        </div>
        <div class="col-sm-6 pr-0">
          <button type="button" class="btn btn-fill btn-sm btn-info" @click.prevent="handleOpenModalMPMCSearch"><i class="fa fa-search"></i> Search</button>
          <button type="button" class="btn btn-fill btn-sm btn-primary" @click.prevent="handleOpenModalMPMCreate"><i class="fa fa-plus"></i> Create</button>
        </div>
      </div>
      <div class="row pt-2">
        <div class="col-sm-12">
          <el-table
            class="table table-sm"
            ref="tableMerchant"
            :data="queriedData"
            style="width: 100%"
          >
            <el-table-column
              v-for="column in tableColumns"
              :min-width="column.minWidth"
              :key="column.label"
              :align="column.align"
              show-tooltip-when-overflow
              :prop="column.prop"
              header-align="center"
              :label="column.label"
              :sortable="column.sortable"
            >
            </el-table-column>
            <el-table-column
              label="Action"
              min-width="100px"
              align="center"
            >
              <template slot-scope="props">
                <button class="btn btn-sm btn-primary" @click.prevent="handleOpenModalMPMDetail(props.row.id)">Detail</button>
                <button class="btn btn-sm btn-danger" v-if="props.row.status !== 'Active'" @click.prevent="handleOpenModalMPMDelete(props.row.id)">Delete</button>
                <span>{{props.row.status.value}}</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-6 pagination-info pt-4" v-if="total > 0">
          <p>Showing {{ from + 1 }} to {{ to }} of {{ total }} entries</p>
        </div>
        <div class="col-sm-6 text-right">
          <p-pagination
            v-model="pagination.currentPage"
            :per-page="pagination.perPage"
            :total="pagination.total"
          >
          </p-pagination>
        </div>
      </div>
    </div>
    <ModalMerchantProfileManagementCreate/>
    <ModalMerchantProfileManagementDetail/>
    <ModalMerchantProfileManagementEdit/>
    <ModalMerchantUserManagementCreate/>
  </div>
</template>
<script>
  import {mapActions} from 'vuex'
  import ModalMerchantProfileManagementCreate from '../modals/AdminRights/MerchantProfileManagement/ModalMerchantProfileManagementCreate'
  import ModalMerchantProfileManagementDetail from '../modals/AdminRights/MerchantProfileManagement/ModalMerchantProfileManagementDetail'
  import ModalMerchantProfileManagementEdit from '../modals/AdminRights/MerchantProfileManagement/ModalMerchantProfileManagementEdit'
  import ModalMerchantUserManagementCreate from '../modals/AdminRights/MerchantUserManagement/ModalMerchantUserManagementCreate'

  export default {
    components: {
      ModalMerchantProfileManagementCreate,
      ModalMerchantProfileManagementDetail,
      ModalMerchantProfileManagementEdit,
      ModalMerchantUserManagementCreate
    },
    computed: {
      pagedData() {
        return this.tableData.slice(this.from, this.to)
      },
      queriedData() {
        if (!this.searchQuery) {
          this.pagination.total = this.tableData.length
          return this.pagedData
        }
        let result = this.tableData
          .filter((row) => {
            let isIncluded = false
            for (let key of this.propsToSearch) {
              if (row[key] !== undefined && row[key] !== null) {
                let rowValue = row[key].toString().toLowerCase()
                if (rowValue.includes && rowValue.includes(this.searchQuery.toLowerCase())) {
                  isIncluded = true
                }
              }
            }
            return isIncluded
          })
        this.pagination.total = result.length
        return result.slice(this.from, this.to)
      },
      to() {
        let highBound = this.from + this.pagination.perPage
        if (this.pagination.total < highBound) {
          highBound = this.pagination.total
        }
        return highBound
      },
      from() {
        return this.pagination.perPage * (this.pagination.currentPage - 1)
      },
      total() {
        this.pagination.total = this.tableData.length
        return this.tableData.length
      }
    },
    created() {
    },
    async mounted() {
      // ========================================================== start import ERROR_CODE by language
      // ==============================================================================================
      const currentLang = this.$i18n.locale
      await import(`../errorcode/AdminRights/MerchantProfileManagement/${currentLang}.js`)
        .then((DATA) => {
          this.ERROR_CODE = DATA.ERROR_CODE
        })
        .catch(async () => {
          await import('../errorcode/AdminRights/MerchantProfileManagement/en.js')
            .then((DATA) => {
              this.ERROR_CODE = DATA.ERROR_CODE
            })
        })
      console.log('[this.ERROR_CODE merchant]', this.ERROR_CODE)
      // ==============================================================================================
      // =========================================================== stop import ERROR_CODE by language
      // coding continue ...

      this.handleGetDataTableMerchantProfile(),
        this.handleGetListLanguageData()
    },

    beforeDestroy() {
    },
    data() {
      return {
        searchQuery: '',
        pagination: {
          perPage: 10,
          currentPage: 1,
          perPageOptions: [5, 10, 20, 50],
          total: 0
        },
        propsToSearch: ['profile_name', 'abbreviation', 'salary'],
        tableColumns: [
          {
            prop: 'profile_name',
            label: 'Merchant Name',
            minWidth: 200,
            sortable: true
          },
          {
            prop: 'abbreviation',
            label: 'Merchant Abbreviation',
            minWidth: 200,
            sortable: true
          },
          {
            prop: 'base_country',
            label: 'Country',
            minWidth: 100,
            sortable: true
          },
          {
            prop: 'updated_time',
            label: 'Last login',
            minWidth: 150,
            sortable: true
          },
          {
            prop: 'status',
            label: 'Current Status',
            minWidth: 100,
            sortable: true
          }
        ],
        tableData: [],
        table_loading: false,
        multipleSelection: [],
        searchForm: {
          merchant_name: '',
          abbreviation: '',
          language: '',
          status: ''
        },
        comboBoxLanguage: []
      }
    },
    methods: {
      ...mapActions('MerchantProfileManagement', {
        apiGetDataTableMerchantProfile: 'apiGetDataTableMerchantProfile',
        apiGetListLanguageData: 'apiGetListLanguageData',
        apiSearchDataTableMerchantProfile: 'apiSearchDataTableMerchantProfile',
        apiDeleteMerchantProfile: 'apiDeleteMerchantProfile'
      }),
      handleOpenModalMPMDetail(rowID) {
        this.$modal.show('modal-merchant-profile-management-detail', {rowID: rowID, ERROR_CODE: this.ERROR_CODE})
      },
      handleOpenModalMPMDelete(rowID) {
        this.apiDeleteMerchantProfile({rowID: rowID})
          .then(response => {
            if (response.code === 0) {
              this.commonNotifyVue(this.ERROR_CODE['DELETE_MERCHANT_PROFILE'][response.code], 'warning')
              this.handleGetDataTableMerchantProfile()
            } else {
              this.commonErrorVue(this.ERROR_CODE['DELETE_MERCHANT_PROFILE'][response.code], 'warning')
            }
          })
          .catch(err => {
            console.log(err)
          })
          .finally(fnal => {
            console.log('always come here')
          })
      },
      handleSelectionChange(val) {
        this.multipleSelection = val
      },
      handleOpenModalMPMCreate() {
        this.$modal.show('modal-merchant-profile-management-create', {ERROR_CODE: this.ERROR_CODE})
      },
      handleGetDataTableMerchantProfile() {
        this.apiGetDataTableMerchantProfile()
          .then(response => {
            if (response.code === 0) {
              this.tableData = response.table_data;
              for (let one_data of response.table_data) {
                if (one_data['status'] === 1) {
                  one_data['status'] = "Active"
                } else if (one_data['status'] === 2) {
                  one_data['status'] = "InActive"
                }
                ;
                if (one_data['base_country'] === 1) {
                  one_data['base_country'] = "HongKong"
                } else if (one_data['base_country'] === 2) {
                  one_data['base_country'] = "England"
                }
              }
            } else {
              this.commonErrorVue(this.ERROR_CODE['GET_TABLE_MERCHANT_PROFILE'][response.code], 'warning')
            }
          })
          .catch(err => {
            console.log(err)
          })
          .finally(fnal => {
            console.log('always come here')
          })
      },
      handleOpenModalMPMCSearch() {
        this.apiSearchDataTableMerchantProfile(this.searchForm)
          .then(response => {
            if (response.code === 0) {
              this.tableData = response.table_data;
              for (let one_data of response.table_data) {
                if (one_data['status'] === 1) {
                  one_data['status'] = "Active"
                } else if (one_data['status'] === 2) {
                  one_data['status'] = "InActive"
                };
                if (one_data['base_country'] === 1) {
                  one_data['base_country'] = "HongKong"
                } else if (one_data['base_country'] === 2) {
                  one_data['base_country'] = "England"
                }
              }
            } else {
            }
          })
          .catch(err => {
            console.log(err)
          })
          .finally(fnal => {
            console.log('always come here')
          })
      },
      handleGetListLanguageData() {
        this.apiGetListLanguageData()
          .then(response => {
            console.log("code:", response.code)
            if (response.code === 0) {
              this.comboBoxLanguage = response.table_data;
              console.log("cuong: ", this.comboBoxLanguage)
            } else {
            }
          })
          .catch(err => {
            console.log(err)
          })
          .finally(fnal => {
            console.log('always come here')
          })
      }
    }
  }
</script>

<style>
  .el-select .el-input {
    width: 110px;
  }

  .input-with-select .el-input-group__prepend {
    background-color: #fff;
  }
</style>
