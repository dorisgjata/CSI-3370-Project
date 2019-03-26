<template>
  <div class="container">
    <div v-if="account">
      <div v-if="account.userFavorites">{{account.userFavorites}}</div>
      <div v-if="account.userPreferences">{{account.userPreferences}}</div>
      <div class="columns centered">
        <div class="column is-one-third">
          <p class="title is-5">Profile</p>
          <div class="card">
            <div class="card-image">
              <figure class="image is-4by3">
                <img src="../assets/fav-menu.jpg" alt="food">
              </figure>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-48x48">
                    <img src="../assets/fav-menu.jpg" alt="food">
                  </figure>
                </div>
                <div class="media-content">
                  <p class="title is-4">Hello</p>
                  <p class="subtitle is-6">{{account.userName}}</p>
                </div>
              </div>
            </div>
            <footer class="card-footer">
              <router-link to="/menu">
                <a v-if="!account.userPreferences" class="card-footer-item">Add Preferences</a>
              </router-link>
              <router-link to="/menu">
                <a v-if="!account.userFavourites" class="card-footer-item">Add Favorites</a>
              </router-link>
            </footer>
          </div>
        </div>

        <div class="column is-one-third">
          <p class="title is-5">Favorites</p>
          <div v-if="!account.userFavourites">
            <div class="card">
              <div class="card-content">
                <div class="media-content">
                  <p class="subtitle is-6">No Favorites Selected</p>
                </div>
              </div>
            </div>
          </div>
          <!-- TODO -->
          <div v-if="account.userFavourites">
            <div v-for="(fav, index) in account.userFavourites" :key="index">
              <div class="card">
                <div class="card-content">
                  <div class="media">
                    <div class="media-left">
                      <figure class="image is-48x48">
                        <img src="../assets/fav-menu.jpg" alt="food">
                      </figure>
                    </div>
                    <div class="media-content">
                      <p class="title is-6">{{fav.favouriteRecommendation}}</p>
                      <p class="title is-6">{{fav.favouriteMeal}}</p>
                      <p class="title is-6">{{fav.favouriteCalories}}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-one-third">
          <p class="title is-5">Preferences</p>
          <div v-if="!account.userPreferences">
            <div class="card">
              <div class="card-content">
                <div class="media-content">
                  <p class="subtitle is-6">No Preferences Selected</p>
                </div>
              </div>
            </div>
          </div>
          <!-- TODO -->
          <div v-if="account.userPreferences">
            <div v-for="(pref, index) in account.userPreferences" :key="index">
              <div class="card">
                <div class="card-content">
                  <div class="media">
                    <div class="media-left">
                      <figure class="image is-48x48">
                        <img src="../assets/fav-menu.jpg" alt="food">
                      </figure>
                    </div>
                    <div class="media-content">
                      <p class="title is-6">{{pref.preferenceNutrients}}</p>
                      <p class="title is-6">{{pref.preferenceFilters}}</p>
                      <p class="title is-6">{{pref.preferenceCalories}}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
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
      account: null
    };
  },
  methods: {
    getAccount(userEmail) {
      const url = `http://localhost:5000/user/${userEmail}`;
      fetch(url, {
        method: "GET", // *GET, POST, PUT, DELETE, etc.
        mode: "cors", // no-cors, cors, *same-origin
        //body: JSON.stringify(data), // data can be `string` or {object}!
        headers: {
          "Content-Type": "application/json"
        }
      })
        .then(res => res.json())
        .then(response => {
          console.log("Success:", JSON.stringify(response));
          this.account = response;
          console.log(this.account.userPreferences);
        })
        .catch(error => console.error("Error:", error));
    }
  },
  created() {
    const userEmail = this.$router.history.current.params.email;
    this.getAccount(userEmail);
  }
};
</script>