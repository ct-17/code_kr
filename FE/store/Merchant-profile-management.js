import {apiGetDataTableMerchantProfile} from '../api/Merchant-profile-management'
import {apiSearchDataTableMerchantProfile} from '../api/Merchant-profile-management'
import {apiGetListLanguageData} from "../api/Merchant-profile-management";
import {apiCreateProfileInformation} from "../api/Merchant-profile-management";
import {apiInitCreateProfileInformation} from "../api/Merchant-profile-management";
import {apiInitProfileInformationDetail} from "../api/Merchant-profile-management";
import {apiDeleteMerchantProfile} from "../api/Merchant-profile-management";
import {CONSTANTS} from '../utils/constant'

const actions = {
  apiGetDataTableMerchantProfile ({commit, state}) {
    return new Promise((resolve, reject) => {
      apiGetDataTableMerchantProfile()
        .then(response => {
          const data = response.data
          if (data.code === CONSTANTS.SUCCESS) {
            /*
            ** logic at here if need to process
            */
          }
          resolve(data) // resovle
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  apiSearchDataTableMerchantProfile ({commit, state}, payload) {
    return new Promise((resolve, reject) => {
      apiSearchDataTableMerchantProfile(payload)
        .then(response => {
          const data = response.data
          if (data.code === CONSTANTS.SUCCESS) {
            /*
            ** logic at here if need to process
            */
          }
          resolve(data) // resovle
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  apiGetListLanguageData ({commit, state}) {
    return new Promise((resolve, reject) => {
      apiGetListLanguageData()
        .then(response => {
          const data = response.data
          if (data.code === CONSTANTS.SUCCESS) {
            /*
            ** logic at here if need to process
            */
          }
          resolve(data) // resovle
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  apiDeleteMerchantProfile ({commit, state}, payload) {
    return new Promise((resolve, reject) => {
      apiDeleteMerchantProfile(payload)
        .then(response => {
          const data = response.data
          if (data.code === CONSTANTS.SUCCESS) {
            /*
            ** logic at here if need to process
            */
          }
          resolve(data) // resovle
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  apiCreateProfileInformation ({commit, state}, payload) {
    return new Promise((resolve, reject) => {
      apiCreateProfileInformation(payload)
        .then(response => {
          const data = response.data
          if (data.code === CONSTANTS.SUCCESS) {
            /*
            ** logic at here if need to process
            */
          }
          resolve(data) // resovle
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  apiInitCreateProfileInformation ({commit, state} ) {
    return new Promise((resolve, reject) => {
      apiInitCreateProfileInformation()
        .then(response => {
          const data = response.data
          if (data.code === CONSTANTS.SUCCESS) {
            /*
            ** logic at here if need to process
            */
          }
          resolve(data) // resovle
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  apiInitProfileInformationDetail ({commit, state}, payload) {
    return new Promise((resolve, reject) => {
      apiInitProfileInformationDetail(payload)
        .then(response => {
          const data = response.data
          if (data.code === CONSTANTS.SUCCESS) {
            /*
            ** logic at here if need to process
            */
          }
          resolve(data) // resovle
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}

const state = () => ({})
const getters = {}
const mutations = {}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
