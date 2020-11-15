<template>
  <modal
    name="modal-merchant-profile-management-detail"
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
  >
    <div class="modal-content">
      <div class="modal-header bg-primary">
        <button type="button" class="close" style="color: white" @click.prevent="handleCloseModal()">&times;</button>
        <h5 class="modal-title">Merchant Profile Detail</h5>
      </div>
      <div class="modal-body p-3">
        <div class="pb-0" style="border: 1px dotted #aaaaaa">
          <div class="row pb-0">
            <div class="col-sm-12">
              <div class="card-title bg-gray-500 text-white p-1 pl-3 mb-3">Profile information</div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Merchant ID</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.profile_id" disabled>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 10em;">MCC</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.mcc" disabled>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Based Currency</span>
                    <select class="form-control" v-model="profileInfoForm.base_currency" disabled>
                      <option :value=1>Hong Kong</option>
                      <option :value=2>Viet Nam</option>
                    </select>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 10em;">Base Country</span>
                    <select class="form-control" v-model="profileInfoForm.base_country" disabled>
                      <option :value=1>Hong Kong</option>
                      <option :value=2>Viet Nam</option>
                    </select>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Merchant Name</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.profile_name" disabled>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 10em">Default language</span>
                    <select class="form-control" v-model="profileInfoForm.default_language" disabled>
                      <option :value=1>Hong Kong</option>
                      <option :value=2>Viet Nam</option>
                    </select>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Abbreviation</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.abbreviation" disabled>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 10em;">Tax ID</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.tax_id" disabled>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Profile Status</span>
                    <select class="form-control" v-model="profileInfoForm.status" disabled>
                      <option :value=1>Active</option>
                      <option :value=2>Not Active</option>
                    </select>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 10em;">TID</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.tid" disabled>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Website URL</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.website_url" disabled>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 10em;">DBA Name</span>
                    <input type="text" class="form-control" v-model="profileInfoForm.dba_name" disabled>
                  </div>
                </div>
              </div>
              <div class="card-title bg-gray-500 text-white p-1 pl-3 mb-3" disabled>Contacts</div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Street Name</span>
                    <input type="text" class="form-control" v-model="contactForm.street_name" disabled>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 10em;">State</span>
                    <input type="text" class="form-control" v-model="contactForm.state" disabled>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">City</span>
                    <input type="text" class="form-control" v-model="contactForm.city" disabled>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width:10em">Send initial email</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioRegionOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="contactForm.send_initial_email" disabled>&ensp; Yes
                      <input type="radio" :value=2 name="RadioRegionOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="contactForm.send_initial_email" disabled>&ensp; No
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3 pb-2">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em;">Phone Number</span>
                    <input type="text" class="form-control" v-model="contactForm.phone_number" disabled>
                  </div>
                </div>
              </div>
              <div class="card-title bg-gray-500 text-white p-1 pl-3 mb-3">Features</div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Email Pay</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioFeaturesOption1" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.email_pay" disabled>&ensp; Enable
                      <input type="radio" :value=2 name="RadioFeaturesOption1" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.email_pay" disabled>&ensp; Disable
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">QR Code</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioFeaturesOption2" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.qr_code" disabled>&ensp; Enable
                      <input type="radio" :value=2 name="RadioFeaturesOption2" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.qr_code" disabled>&ensp; Disable
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3" style="min-width: 12em">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Subscription</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioFeaturesOption3" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.subscription" disabled>&ensp; Enable
                      <input type="radio" :value=2 name="RadioFeaturesOption3" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.subscription" disabled>&ensp; Disable
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Refund</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioFeaturesOption4" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.refund" disabled>&ensp; Enable
                      <input type="radio" :value=2 name="RadioFeaturesOption4" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.refund" disabled>&ensp; Disable
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3 pb-2" style="min-width: 12em">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Default Email Receipt</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioFeaturesOption5" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.default_email_receipt" disabled>&ensp; Sale
                      <input type="radio" :value=2 name="RadioFeaturesOption5" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.default_email_receipt" disabled>&ensp; Manual
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3 pb-2" style="min-width: 12em">
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Default Payment Mode</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <input type="radio" :value=1 name="RadioFeaturesOption6" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.default_payment_mode" disabled>&ensp; Sale
                      <input type="radio" :value=2 name="RadioFeaturesOption6" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="featuresForm.default_payment_mode" disabled>&ensp; Auth Capture (1 - 7 days)
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
                      <input type="radio" :value=1 name="RadioFeesOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="feeForm.payment_mechanism" disabled>&ensp; Credit Cards
                      <input type="radio" :value=2 name="RadioFeesOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="feeForm.payment_mechanism" disabled>&ensp; Invoices
                      <input type="radio" :value=3 name="RadioFeesOption" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="feeForm.payment_mechanism" disabled>&ensp; Others
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Setup Charge</span>
                    <input type="text" class="form-control" v-model="feeForm.setup_charge" disabled>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 11em">Annual Charge</span>
                    <input type="text" class="form-control" v-model="feeForm.annual_charge" disabled>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Per Transaction Fee (Fix)</span>
                    <input type="text" class="form-control" v-model="feeForm.per_transaction_fee" disabled>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 11em;">Per Successful Rate</span>
                    <input type="text" class="form-control" v-model="feeForm.per_successful_rate" disabled>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3">
                <div class="col-sm-6 pr-0">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 13.5em">Per Transaction Rate (%)</span>
                    <input type="text" class="form-control" v-model="feeForm.per_transaction_rate" disabled>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="input-group input-group-sm">
                    <span class="input-group-addon" style="min-width: 11em"> Refund return rate</span>
                    <div class="input-group-append">
                      <input type="radio" :value=1 name="RadioRegionOption1" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="feeForm.refund_return_rate" disabled>&ensp; Yes
                      <input type="radio" :value=2 name="RadioRegionOption1" style="width: 19px; height: 19px; vertical-align: bottom; margin-left: 12px;" v-model="feeForm.refund_return_rate" disabled>&ensp; No
                    </div>
                  </div>
                </div>
              </div>
              <div class="row pl-3 pr-3 pb-2">
                <div class="col-sm-12">
                  <div class="input-group">
                    <span class="input-group-addon" style="min-width: 11.5em">Comments</span>
                    <div class="input-group-append" style="flex: 1 1 auto;">
                      <textarea class="form-control" rows="5" resize="none" v-model="feeForm.comments" disabled></textarea>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-footer p-3">
        <button type="button" class="btn btn-primary btn-sm btn-fill" @click.prevent="handleOpenModalCreateMerchantUser" v-if="profileInfoForm.status === 2">
          <i class="fa fa-plus"></i> Create Merchant User
        </button>
        <button type="button" class="btn btn-warning btn-sm btn-fill" @click.prevent="handleOpenModalMPMEdit">
          <i class="fa fa-edit"></i> Edit
        </button>
        <button type="button" class="btn btn-danger btn-sm btn-fill" @click.prevent="handleCloseModal">
          <i class="fa fa-ban"></i> Cancel
        </button>
      </div>
    </div>
  </modal>
</template>

<script>
  import {mapActions} from 'vuex'

  export default {
    name: 'ModalMerchantProfileManagementDetail',
    data() {
      return {
        rowID: 0,
        profileInfoForm: {
          profile_id: '',
          base_country: '',
          base_currency: '',
          default_language: '',
          profile_name: '',
          abbreviation: '',
          status: '',
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
          phone_number: ''
        },
        featuresForm: {
          email_pay: 1,
          qr_code: 1,
          subscription: 1,
          refund: 1,
          default_email_receipt: 1,
          default_payment_mode: 1
        },
        feeForm: {
          payment_mechanism: 1,
          setup_charge: '',
          annual_charge: '',
          per_transaction_fee: '',
          per_transaction_rate: '',
          per_successful_rate: '',
          refund_return_rate: 1,
          comments: ''
        }
      }
    },
    methods: {
      ...mapActions('MerchantProfileManagement', {
        apiInitProfileInformationDetail: 'apiInitProfileInformationDetail'
      }),
      handleEventBeforeOpenModal(event) {
        this.ERROR_CODE = event.params.ERROR_CODE;
        this.rowID = event.params.rowID;
        console.log("error", this.ERROR_CODE);
        this.handleGetDateProfileInfo();
        this.handleGetDateContacts();
        this.handleGetDateFeatures();
        this.handleGetDateFee()
      },
      handleCloseModal() {
        this.$modal.hide('modal-merchant-profile-management-detail')
      },
      handleOpenModalMPMEdit() {
        this.$modal.show('modal-merchant-profile-management-edit')
      },
      handleOpenModalCreateMerchantUser () {
        this.$modal.show('modal-merchant-user-management-create')
      },
      handleGetDateProfileInfo() {
        this.apiInitProfileInformationDetail({rowID: this.rowID})
          .then(response => {
            if (response.code === 0) {
              this.profileInfoForm = response.profile_info_data;
            } else {
              this.handleCloseModal()
              this.commonErrorVue(this.ERROR_CODE['GET_MERCHANT_PROFILE_DETAIL'][response.code], 'warning')
            }
          })
          .catch(err => {
            console.log(err)
          })
          .finally(fnal => {
            console.log('always come here')
          })
      },
      handleGetDateContacts() {
        this.apiInitProfileInformationDetail({rowID: this.rowID})
          .then(response => {
            if (response.code === 0) {
              this.contactForm = response.contact_data;
            } else {
              this.handleCloseModal()
              this.commonErrorVue(this.ERROR_CODE['GET_MERCHANT_PROFILE_DETAIL'][response.code], 'warning')
            }
          })
          .catch(err => {
            console.log(err)
          })
          .finally(fnal => {
            console.log('always come here')
          })
      },
      handleGetDateFeatures() {
        this.apiInitProfileInformationDetail({rowID: this.rowID})
          .then(response => {
            if (response.code === 0) {
              this.featuresForm = response.features_data;
            } else {
              this.handleCloseModal()
              this.commonErrorVue(this.ERROR_CODE['GET_MERCHANT_PROFILE_DETAIL'][response.code], 'warning')
            }
          })
          .catch(err => {
            console.log(err)
          })
          .finally(fnal => {
            console.log('always come here')
          })
      },
      handleGetDateFee() {
        this.apiInitProfileInformationDetail({rowID: this.rowID})
          .then(response => {
            if (response.code === 0) {
              this.feeForm = response.fee_data;
            } else {
              this.commonErrorVue(this.ERROR_CODE['GET_MERCHANT_PROFILE_DETAIL'][response.code], 'warning')
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
