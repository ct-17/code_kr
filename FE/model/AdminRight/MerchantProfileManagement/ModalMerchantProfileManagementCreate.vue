<template>
  <modal
    name="modal-merchant-profile-management-create"
    :width="1000"
    height="auto"
    :shiftY="0.2"
    :delay="200"
    :adaptive="true"
    draggable=".modal-header"
    :scrollable="true"
    :reset="true"
    :clickToClose="false"
    @before-open="handleEventBeforeOpenModal"
    @before-close="handleEventBeforeCloseModal"
  >
    <div class="modal-content">
      <div class="modal-header bg-primary">
        <button type="button" class="close" style="color: white" @click.prevent="handleCloseModal()">&times;</button>
        <h5 class="modal-title">Create Merchant Profile</h5>
      </div>
      <div class="modal-body p-3">
        <div class="pb-0" style="border: 1px dotted #aaaaaa">
          <div class="row pb-0">
            <div class="col-sm-12">
              <div class="card-title bg-gray-500 text-white p-1 pl-3 mb-3">Profile information</div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Merchant ID</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.profile_id">
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 9.4em;">MCC</span>
                    <input type="text" class="form-control" maxlength="4" v-model="profileInfoForm.mcc">
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.4em;">Based Currency</span>
                    <select class="form-control" v-model="profileInfoForm.base_currency">
                      <option
                        class="select-default"
                        v-for="item in comboBoxCurrency"
                        :key="item.id"
                        :label="item.name"
                        :value="item.id"
                      >
                      </option>
                    </select>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 9.4em;">Base Country</span>
                    <select class="form-control" v-model="profileInfoForm.base_country">
                      <option
                        class="select-default"
                        v-for="item in comboBoxCountry"
                        :key="item.id"
                        :label="item.name"
                        :value="item.id"
                      >
                      </option>
                    </select>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Merchant Name</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.profile_name">
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 9em">Default language</span>
                    <select class="form-control" v-model="profileInfoForm.default_language">
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
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Abbreviation</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.abbreviation">
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 9.4em;">Tax ID</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.tax_id">
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Profile Status</span>
                    <select class="form-control" v-model="profileInfoForm.status" disabled>
                      <option :value=1>Active</option>
                      <option :value=2>InActive</option>
                    </select>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 9.4em;">TID</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.tid">
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Website URL</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.website_url">
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 9.4em;">DBA Name</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.dba_name">
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3 pb-2">
              </div>
              <div class="card-title bg-gray-500 text-white p-1 pl-3 mb-3">Contacts</div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Street Name</span>
                    <input type="text" class="form-control" v-model="contactForm.street_name">
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 9.4em;">State</span>
                    <input type="text" class="form-control" v-model="contactForm.state">
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">City</span>
                    <input type="text" class="form-control" v-model="contactForm.city">
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 9.4em">Send initial email</span>
                    <div class="input-group-append">
                      <input type="radio" name="RadioSIEOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="contactForm.send_initial_email" :value=1>&ensp; Yes
                      <input type="radio" name="RadioSIEOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="contactForm.send_initial_email" :value=2>&ensp; No
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Phone Number</span>
                    <input type="text" class="form-control" v-model="contactForm.phone_number">
                  </div>
                </div>
              </div>
              <div class="card-title bg-gray-500 text-white p-1 pl-3 mb-3">Features</div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Email Pay</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioEmailPayOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.email_pay">&ensp; Enable
                      <input type="radio" :value=2 name="RadioEmailPayOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.email_pay">&ensp; Disable
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">QR Code</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioQRCodeOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.qr_code">&ensp; Enable
                      <input type="radio" :value=2 name="RadioQRCodeOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.qr_code">&ensp; Disable
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3" style="min-width: 13.5em">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Subscription</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioSubscriptionOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.subscription">&ensp; Enable
                      <input type="radio" :value=2 name="RadioSubscriptionOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.subscription">&ensp; Disable
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Refund</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioRefundOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.refund">&ensp; Enable
                      <input type="radio" :value=2 name="RadioRefundOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.refund">&ensp; Disable
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3 pb-2" style="min-width: 13.5em">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Default Email Receipt</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioDEROption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.default_email_receipt">&ensp; Sale
                      <input type="radio" :value=2 name="RadioDEROption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.default_email_receipt">&ensp; Manual
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3" style="min-width: 13.5em">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em"> Default Payment Mode</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioDPMOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.default_payment_mode">&ensp; Sale
                      <input type="radio" :value=2 name="RadioDPMOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.default_payment_mode">&ensp; Auth Capture (1 - 7 days)
                    </div>
                  </div>
                </div>
              </div>
              <div class="card-title bg-gray-500 text-white p-1 pl-3 mb-3">Fees</div>
              <div class="row pr-3 pl-3">
                <div class="col-sm-12">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Payment Mechanism</span>
                    <div class="input-group-append text-left">
                      <input type="radio" :value=1 name="RadioPaymentMechanismOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="feesForm.payment_mechanism">&ensp; Credit Cards
                      <input type="radio" :value=2 name="RadioPaymentMechanismOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="feesForm.payment_mechanism">&ensp; Invoices
                      <input type="radio" :value=3 name="RadioPaymentMechanismOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="feesForm.payment_mechanism">&ensp; Others
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Setup Charge</span>
                    <input type="text" class="form-control" v-model="feesForm.setup_charge">
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 11em">Annual Charge</span>
                    <input type="text" class="form-control" v-model="feesForm.annual_charge">
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">

              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Per Transaction Fee (Fix)</span>
                    <input type="text" class="form-control" v-model="feesForm.per_transaction_fee">
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 11em;">Per Successful Rate</span>
                    <input type="text" class="form-control" v-model="feesForm.per_successful_rate">
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Per Transaction Rate (%)</span>
                    <input type="text" class="form-control" v-model="feesForm.per_transaction_rate">
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 11em"> Refund return rate</span>
                    <div class="input-group-append">
                      <input type="radio" :value=1 name="RadioRRROption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="feesForm.refund_return_rate">&ensp; Yes
                      <input type="radio" :value=2 name="RadioRRROption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="feesForm.refund_return_rate">&ensp; No
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3 pb-2">
                <div class="col-sm-12">
                  <div class="input-group">
                    <span class="input-group-addon" style="min-width: 11.5em">Comments</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <textarea class="form-control" rows="5" resize="none" v-model="feesForm.comments"></textarea>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-footer p-3">
        <button type="button" class="btn btn-primary btn-sm btn-fill" @click.prevent="handleOpenGatewayConfiguration()">
          <i class="fa fa-upload"></i> Gateway Configuration
        </button>
        <button type="button" class="btn btn-warning btn-sm btn-fill" @click.prevent="handleSaveMerchantProfile()">
          <i class="fa fa-save"></i> Save
        </button>
        <button type="button" class="btn btn-danger btn-sm btn-fill" @click.prevent="handleCloseModal()">
          <i class="fa fa-ban"></i> Cancel
        </button>
      </div>
    </div>
  </modal>
</template>

<script>
  import {mapActions} from 'vuex'

  export default {
    name: "ModalMerchantProfileManagementCreate",

    beforeDestroy() {
    },
    data() {
      return {
        isModalTypeAction: 'create',
        comboBoxCurrency: [],
        comboBoxLanguage: [],
        comboBoxCountry: [],
        profileInfoForm: {
          profile_id: '',
          base_country: '',
          base_currency: '',
          default_language: '',
          profile_name: '',
          abbreviation: '',
          status: 2,
          website_url: '',
          tax_id: '',
          tid: '',
          dba_name: '',
          mcc: ''
        },
        contactForm: {
          street_name: '',
          city: '',
          state: '',
          send_initial_email: 1,
          phone_number: '',
        },
        featuresForm: {
          email_pay: 1,
          qr_code: 1,
          subscription: 1,
          refund: 1,
          default_email_receipt: 1,
          default_payment_mode: 1
        },
        feesForm: {
          payment_mechanism: 1,
          setup_charge: '',
          annual_charge: '',
          per_transaction_fee: '',
          per_transaction_rate: '',
          per_successful_rate: '',
          refund_return_rate: 1,
          comments: ''
        },
        ERROR_CODE: '',
        rowID: 0
      }
    },
    methods: {
      ...mapActions('MerchantProfileManagement', {
        apiCreateProfileInformation: 'apiCreateProfileInformation',
        apiInitCreateProfileInformation: 'apiInitCreateProfileInformation'
      }),
      handleEventBeforeOpenModal(event) {
        this.ERROR_CODE = event.params.ERROR_CODE;
        console.log("error", this.ERROR_CODE);
        this.handleGetListCurrency(),
          this.handleGetListLanguage(),
          this.handleGetListCountry()
      },
      handleCloseModal() {
        console.log('close modal')
        this.$modal.hide('modal-merchant-profile-management-create')
      },
      handleOpenCMU() {
        this.$modal.show('modal-merchant-user-management-create')
      },
      handleOpenGatewayConfiguration() {
        this.$router.push('/configuration-setting')
      },
      handleSaveMerchantProfile() {
        let input_data = Object.assign(this.profileInfoForm, this.contactForm, this.featuresForm, this.feesForm);

        if (this.profileInfoForm.profile_id === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_02'], 'warning');
        } else if (this.profileInfoForm.mcc === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_03'], 'warning');
        } else if (this.profileInfoForm.base_currency === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_04'], 'warning');
        } else if (this.profileInfoForm.base_country === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_05'], 'warning');
        } else if (this.profileInfoForm.profile_name === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_06'], 'warning');
        } else if (this.profileInfoForm.default_language === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_07'], 'warning');
        } else if (this.profileInfoForm.abbreviation === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_08'], 'warning');
        } else if (this.profileInfoForm.tax_id === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_09'], 'warning');
        } else if (this.profileInfoForm.status === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_10'], 'warning');
        } else if (this.profileInfoForm.tid === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_11'], 'warning');
        } else if (this.profileInfoForm.website_url === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_12'], 'warning');
        } else if (this.profileInfoForm.dba_name === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_13'], 'warning');
        } else if (this.contactForm.street_name === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_14'], 'warning');
        } else if (this.contactForm.state === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_15'], 'warning');
        } else if (this.contactForm.city === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_16'], 'warning');
        } else if (this.contactForm.phone_number === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_17'], 'warning');
        } else if (this.feesForm.setup_charge === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_18'], 'warning');
        } else if (this.feesForm.annual_charge === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_19'], 'warning');
        } else if (this.feesForm.per_transaction_fee === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_20'], 'warning');
        } else if (this.feesForm.per_successful_rate === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_21'], 'warning');
        } else if (this.feesForm.per_transaction_rate === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_22'], 'warning');
        } else if (this.feesForm.comments === '' || this.profileInfoForm.profile_id === undefined) {
          this.commonNotifyVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE']['ERR_AR11_23'], 'warning');
        } else {
          this.apiCreateProfileInformation(input_data)
            .then(response => {
              if (response.code === 0) {
                this.tableData = response.table_data;
                this.commonConfirmOKVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE'][response.code], 'warning')
                this.handleCloseModal()
              } else {
                this.commonErrorVue(this.ERROR_CODE['CREATE_MERCHANT_PROFILE'][response.code], 'warning')
              }
            })
            .catch(err => {
              console.log(err)
            })
            .finally(fnal => {
              console.log('always come here')
            })
        }
      },
      handleGetListCurrency() {
        this.apiInitCreateProfileInformation()
          .then(response => {
            if (response.code === 0) {
              this.comboBoxCurrency = response.currency_data;
            } else {
              this.handleCloseModal()
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
      handleGetListCountry() {
        this.apiInitCreateProfileInformation()
          .then(response => {
            if (response.code === 0) {
              this.comboBoxCountry = response.country_data;
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
      handleGetListLanguage() {
        this.apiInitCreateProfileInformation()
          .then(response => {
            if (response.code === 0) {
              this.comboBoxLanguage = response.language_data;
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
      handleEventBeforeCloseModal() {
        this.profileInfoForm.profile_id = "";
        this.profileInfoForm.base_country = "";
        this.profileInfoForm.base_currency = "";
        this.profileInfoForm.default_language = "";
        this.profileInfoForm.profile_name = "";
        this.profileInfoForm.abbreviation = "";
        this.profileInfoForm.status = "";
        this.profileInfoForm.website_url = "";
        this.profileInfoForm.tax_id = "";
        this.profileInfoForm.profile_id = "";
        this.profileInfoForm.profile_id = "";
        this.profileInfoForm.profile_id = "";
      }
    }
  }
</script>
