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
        <div class="column centered">
          <div class="column">
            <p class="title is-5">Favorite Items</p>
            <div v-if="favorites.length===0">
              <div class="card">
                <div class="card-content">
                  <div class="media-content">
                    <p class="subtitle is-6">No Favorite Items Selected</p>
                  </div>
                </div>
              </div>
            </div>
            <!-- TODO -->
            <div v-if="favorites.length!==0">
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
                      <button
                        type="button"
                        class="button"
                        @click=" deleteFavItem(fav.favouriteItem, userEmail) "
                      >Delete</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="column">
            <p class="title is-5">Favorite Meals</p>
            <div v-if="favoriteMeals.length===0">
              <div class="card">
                <div class="card-content">
                  <div class="media-content">
                    <p class="subtitle is-6">No Favorite Meals Selected</p>
                  </div>
                </div>
              </div>
            </div>
            <!-- TODO -->
            <div v-if="favoriteMeals.length!==0">
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
                      <button
                        type="button"
                        class="button"
                        @click=" deleteFavMeal(fav.favouriteMeal, userEmail) "
                      >Delete</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="column">
          <div class="column">
            <p class="title is-5">Recommended Meal</p>
            <div v-if="favoriteMeals.length===0">
              <div class="card">
                <div class="card-content">
                  <div class="media-content">
                    <p class="subtitle is-6">You have to presave meals to get recommendations</p>
                  </div>
                </div>
              </div>
            </div>
            <div v-if="favoriteMeals.length!==0 && mealData.length!==0">
              <div v-for="(meal, index) in mealData" :key="index">
                <div class="card">
                  <div class="card-content">
                    <div class="media">
                      <div class="media-left">
                        <figure class="image is-48x48">
                          <img src="../assets/fav-menu.jpg" alt="food">
                        </figure>
                      </div>
                      <div class="media-content">
                        <div class="has-text-left">
                          <div>
                            <strong>First Item:</strong>
                            <p class="subtitle is-6">{{meal.foodItem1}}</p>
                          </div>
                          <div>
                            <strong>Second Item:</strong>
                            <p class="subtitle is-6">{{meal.foodItem2}}</p>
                          </div>
                          <div>
                            <strong>Third Item:</strong>
                            <p class="subtitle is-6">{{meal.foodItem3}}</p>
                          </div>
                          <div>
                            <strong>Period:</strong>
                            <p class="subtitle is-6">{{meal.mealPeriod}}</p>
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
      favorites: [],
      favoriteMeals: [],
      mealData: null,
      userEmail: ""
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
    getMeals() {
      const path = "http://localhost:5000/meal";
      axios
        .get(path)
        .then(res => {
          this.mealData = res.data.meals;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
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
    },
    deleteFavMeal(favouriteMeal, userEmail) {
      const path = `http://localhost:5000/user/${userEmail}/favouritemeal/${favouriteMeal}`;
      axios
        .delete(path)
        .then(() => {
          this.getMealFavorites();
          this.sucess();
        })
        .catch(error => {
          this.error();
        });
    },
    deleteFavItem(favouriteItem, userEmail) {
      const path = `http://localhost:5000/user/${userEmail}/favourites/${favouriteItem}`;
      axios
        .delete(path)
        .then(() => {
          this.getUserFavorites();
          this.sucess();
        })
        .catch(error => {
          this.error();
        });
    },
    sucess() {
      this.$toast.open({
        message: "Removed successfully",
        type: "is-info"
      });
    },
    error() {
      this.$toast.open({
        message: "Couldn't remove successfully",
        type: "is-danger"
      });
    }
  },
  created() {
    this.userEmail = this.$router.history.current.params.email;
    console.log("ROUTER", this.$router);
    this.getUserFavorites(this.userEmail);
    this.getAccount(this.userEmail);
    this.getMealFavorites(this.userEmail);
    this.getMeals();
  }
};
</script>