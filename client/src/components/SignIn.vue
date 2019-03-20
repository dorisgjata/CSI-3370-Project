<template>
  <div class="conatiner">
    <!-- <button class="button" @click="handleClickGetAuth" :disabled="!isInit">get auth code</button> -->
    <button class="button" @click="handleClickSignIn" v-if="!isSignIn" :disabled="!isInit">Sign In with Google</button>
    <button class="button" @click="handleClickSignOut" v-if="isSignIn" :disabled="!isInit">Sign Out</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Locatons",
  data() {
    return {
      isInit: false,
      isSignIn: false
    }
  },
  methods: {
    handleClickGetAuth(){
      this.$gAuth.getAuthCode()
      .then(authCode => {
        console.log(authCode)
        // On success
        return this.$http.post('localhost:5000/auth/google', { code: authCode, redirect_uri: 'postmessage' })
      })
      .then(response => {
        // And then
      })
      .catch(error => {
        // On fail do something
      })
    },
    handleClickSignIn(){
      this.$gAuth.signIn()
      .then(user => {
        // On success do something, refer to https://developers.google.com/api-client-library/javascript/reference/referencedocs#googleusergetid
        console.log('user', GoogleUser)
        this.isSignIn = this.$gAuth.isAuthorized
      })
      .catch(error  => {
        // On fail do something
      })
    },
    handleClickSignOut(){
      this.$gAuth.signOut()
      .then(() => {
        // On success do something
        this.isSignIn = this.$gAuth.isAuthorized
      })
      .catch(error  => {
        // On fail do something
      })
    }
  },
  mounted(){
    let that = this
    let checkGauthLoad = setInterval(function(){
      that.isInit = that.$gAuth.isInit
      that.isSignIn = that.$gAuth.isAuthorized
      if(that.isInit) clearInterval(checkGauthLoad)
    }, 1000);
  }
  
}
</script>