// store/accounts.js

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const ACCOUNT_API_URL = 'http://127.0.0.1:8000/accounts'
  const token = ref('')
  const isLogin = computed(() => {
    return token.value? true : false
  })

  const signUp = function ({ username, age, password1, password2 }) {
    axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/signup/`,
      data: {
        username, age, password1, password2
      }
    })
      .then(res => {
        console.log('회원가입 성공')
        token.value = res.data.key
      })
      .catch(err => {
        console.log(err.response.data)
        alert(err.response.data.detail)
      })
  }

  const logIn = function ({ username, password }) {
    axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        console.log('로그인 성공')
        token.value = res.data.key
      })
      .catch(err => {
        console.log(err.response.data)
        alert(err.response.data.non_field_errors)
      })
  }



  return { ACCOUNT_API_URL, token, isLogin, signUp, logIn }
}, { persist: true })
