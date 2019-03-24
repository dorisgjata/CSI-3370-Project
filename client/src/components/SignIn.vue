<template>
  <div class="conatiner">
    <button
      class="button"
      @click="handleClickSignIn"
      v-if="!isSignIn"
      :disabled="!isInit"
    >Sign In with Google</button>
    <button class="button" @click="handleClickSignOut" v-if="isSignIn" :disabled="!isInit">Sign Out</button>
    <div v-if="user!==''">Hello {{this.user}}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignIn",
  data() {
    return {
      isInit: false,
      isSignIn: false,
      user: ""
    };
  },
  methods: {
    handleClickGetAuth() {
      this.$gAuth
        .getAuthCode()
        .then(authCode => {
          console.log(authCode);
          // On success
          return this.$http.post("localhost:5000/auth/google", {
            code: authCode,
            redirect_uri: "postmessage"
          });
        })
        .then(response => {
          // And then
        })
        .catch(error => {
          // On fail do something
        });
    },
    handleClickSignIn() {
      this.$gAuth
        .signIn()
        .then(googleuser => {
           this.isSignIn = this.$gAuth.isAuthorized;
         
          const data  = {
            "firstName": googleuser.w3.ofa,
            "lastName": googleuser.w3.wea,
            "email": googleuser.w3.U3,
            "accessToken": googleuser.Zi.access_token,
            "tokenId": googleuser.Zi.id_token
          };
          const url ='http://localhost:5000/users'
          fetch(url, {
            method: "POST", // *GET, POST, PUT, DELETE, etc.
            mode: "cors", // no-cors, cors, *same-origin
            body: JSON.stringify(data), // data can be `string` or {object}!
            headers:{
              'Content-Type': 'application/json'
            }
            }).then(res => res.json())
            .then(response => console.log('Success:', JSON.stringify(response)))
            .catch(error => console.error('Error:', error));           
            // On success do something, refer to https://developers.google.com/api-client-library/javascript/reference/referencedocs#googleusergetid
        })
        .catch(error => {
          // On fail do something
        });
    },
    handleClickSignOut() {
      this.$gAuth
        .signOut()
        .then(() => {
          // On success do something
          this.isSignIn = this.$gAuth.isAuthorized;
        })
        .catch(error => {
          // On fail do something
        });
    }
  },
  mounted() {
    let that = this;
    let checkGauthLoad = setInterval(function() {
      that.isInit = that.$gAuth.isInit;
      that.isSignIn = that.$gAuth.isAuthorized;
      if (that.isInit) clearInterval(checkGauthLoad);
    }, 1000);
    
  },
  created(){
    if (this.isSignIn === true){
      console.log(this.$gauth)
          this.user = googleuser.w3.ig;

      } 
  }
};
</script>