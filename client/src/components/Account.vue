<template>
  <div class="container">
    <div v-if="account">
      <div v-if="account.userFavorites">{{account.userFavorites}}</div>
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
              <a
                v-if="!account.userPreferences"
                @click="goToMenu()"
                class="card-footer-item"
              >Add Favorite Meals</a>

              <a
                v-if="!account.userFavourites"
                @click="goToMenu()"
                class="card-footer-item"
              >Add Favorite Items</a>
            </footer>
          </div>
        </div>

        <div class="column is-one-third">
          <p class="title is-5">Favorite Items</p>
          <div v-if="!favorites">
            <div class="card">
              <div class="card-content">
                <div class="media-content">
                  <p class="subtitle is-6">No Favorite Items Selected</p>
                </div>
              </div>
            </div>
          </div>
          <!-- TODO -->
          <div v-if="favorites">
            <div v-for="(fav, index) in favorites" :key="index">
              <div class="card">
                <div class="card-content">
                  <div class="media">
                    <div class="media-left">
                      <figure class="image is-48x48">
                        <img src="../assets/fav-menu.jpg" alt="food">
                      </figure>
                    </div>
                    <div class="media-content">
                      <p class="title is-6">{{fav.itemName}}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="column is-one-third">
          <p class="title is-5">Favorite Meals</p>
          <div v-if="!favoriteMeals">
            <div class="card">
              <div class="card-content">
                <div class="media-content">
                  <p class="subtitle is-6">No Favorite Meals Selected</p>
                </div>
              </div>
            </div>
          </div>
          <!-- TODO -->
          <div v-if="favoriteMeals">
            <div v-for="(fav, index) in favoriteMeals" :key="index">
              <div class="card">
                <div class="card-content">
                  <div class="media">
                    <div class="media-left">
                      <figure class="image is-48x48">
                        <img src="../assets/fav-menu.jpg" alt="food">
                      </figure>
                    </div>
                    <div class="media-content">
                      <p class="title is-6">{{fav.mealName}}</p>
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
  name: "Account",
  data() {
    return {
      account: null,
      favorites: null,
      favoriteMeals: null
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
          // console.log("Success:", JSON.stringify(response));
          this.account = response;
          // console.log(this.account.userPreferences);
        })
        .catch(error => console.error("Error:", error));
    },
    getUserFavorites(userEmail) {
      axios
        .get(`http://localhost:5000/user/${userEmail}/favourites`)
        .then(res => {
          console.log(res.data.favorites);
          this.favorites = res.data.favorites;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getMealFavorites(userEmail) {
      axios
        .get(`http://localhost:5000/user/${userEmail}/favouritemeal`)
        .then(res => {
          console.log(res.data);
          this.favoriteMeals = res.data.favoritemeals;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    goToMenu() {
      this.$router.push({
        name: "WhatsOnMenu",
        params: { email: this.userEmail }
      });
      console.log("menu done");
    }
  },
  created() {
    this.userEmail = this.$router.history.current.params.email;
    console.log("ROUTER", this.$router);
    this.getUserFavorites(this.userEmail);
    this.getAccount(this.userEmail);
    this.getMealFavorites(this.userEmail)
  }
};
</script>