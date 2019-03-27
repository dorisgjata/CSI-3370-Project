<template>
  <div class="navbar-menu">
    <div class="navbar-start">
    <a class="navbar-item" href="/">Home</a>
    <a class="navbar-item" href="/steps">Menu</a>
    <a class="navbar-item">About</a>
    <a class="navbar-item">Contact</a>
    </div>
    <div id="signin"></div>
    <div class="navbar-end">
      <a class="navbar-item" @click="goToAccount(userEmail)" v-if="isSignIn">Account</a>
      <div class="navbar-item">
        <button
          class="button is-primary"
          @click="handleClickSignIn"
          v-if="!isSignIn"
          :disabled="!isInit"
        >Sign In with Google</button>
        <button
          class="button is-primary"
          @click="handleClickSignOut"
          v-if="isSignIn"
          :disabled="!isInit"
        >Sign Out</button>
      </div>
    </div>
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
      userEmail: "dorisgjata@gmail.com"
    };
  },
  methods: {
    handleClickSignIn() {
      this.$gAuth
        .signIn()
        .then(googleuser => {
          this.isSignIn = this.$gAuth.isAuthorized;
          const user = googleuser.w3.ofa;
          this.userEmail = googleuser.w3.U3;
          const data = {
            firstName: googleuser.w3.ofa,
            lastName: googleuser.w3.wea,
            email: googleuser.w3.U3,
            accessToken: googleuser.Zi.access_token,
            tokenId: googleuser.Zi.id_token
          };
          const url = "http://localhost:5000/users";
          fetch(url, {
            method: "POST", // *GET, POST, PUT, DELETE, etc.
            mode: "cors", // no-cors, cors, *same-origin
            body: JSON.stringify(data), // data can be `string` or {object}!
            headers: {
              "Content-Type": "application/json"
            }
          })
            .then(res => res.json())
            .then(response => console.log("Success:", JSON.stringify(response)))
            .catch(error => console.error("Error:", error));
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
    },
    goToAccount(userEmail) {
      this.$router.push({ name: "account", params: { email: this.userEmail } });
    }
  },
  mounted() {
    let that = this;
    let checkGauthLoad = setInterval(function() {
      that.isInit = that.$gAuth.isInit;
      that.isSignIn = that.$gAuth.isAuthorized;
      if (that.isInit) clearInterval(checkGauthLoad);
      if (that.isSignIn) {
        console.log(that.$gAuth);
        this.user = that.$gAuth.googleuser.w3.ig;
      }
    }, 1000);
  },
  created() {}
};
</script>