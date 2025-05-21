<!-- views/LoginView.vue -->

<template>
  <div>
    <h1>SignUp</h1>
    <form @submit.prevent="onLogIn">
      <label for="username">username: </label>
      <input type="text" id="username" v-model="username">
      <br>

      <label for="password">password: </label>
      <input type="password" id="password" v-model="password">
      <br>

      <input type="submit" value="signup">
    
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/accounts.js'

  const accountStore = useAccountStore()
  
  const username = ref('')
  const password = ref('')

  const onLogIn = function () {
    const userInfo = {
      username: username.value,
      password: password.value,
    }
    accountStore.logIn(userInfo)
  }
</script>

<style>

</style>
