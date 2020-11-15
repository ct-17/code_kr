import request from '../utils/request'

export function apiGetDataTableMerchantProfile () {
  return request({
    url: '/webapp/merchantprofilemanagement/get_table_merchant_profile',
    method: 'post'
  })
}


export function apiSearchDataTableMerchantProfile (payload) {
  return request({
    url: '/webapp/merchantprofilemanagement/search_table_merchant_profile',
    method: 'post',
    data: payload
  })
}

export function apiDeleteMerchantProfile (payload) {
  return request({
    url: '/webapp/merchantprofilemanagement/delete_merchant_profile',
    method: 'post',
    data: payload
  })
}


export function apiGetListLanguageData () {
  return request({
    url: '/webapp/merchantprofilemanagement/get_combobox_language',
    method: 'post'
  })
}

export function apiCreateProfileInformation (payload) {
  return request({
    url: '/webapp/merchantprofilemanagement/create_profile_information',
    method: 'post',
    data: payload
  })
}

export function apiInitCreateProfileInformation () {
  return request({
    url: '/webapp/merchantprofilemanagement/init_create_profile_information',
    method: 'post',
  })
}


export function apiInitProfileInformationDetail (payload) {
  return request({
    url: '/webapp/merchantprofilemanagement/init_profile_information_detail',
    method: 'post',
    data: payload
  })
}
