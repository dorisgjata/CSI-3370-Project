<template>
  <div class="conatiner">
    <div class="columns">
      <div class="column is-full-width box">
        <b-field
          id="searchfield"
          aria-label="What are you looking for?"
          label-for="searchgroup"
          class="column is-grouped is-grouped-right"
        >
          <b-input
            expanded
            id="searchgroup"
            aria-labelledby="searchfield"
            placeholder="What are you looking for?"
            v-model="search"
          />
        </b-field>
        <div class="column is-half">
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <b-field label="Calories" label-for="calories"/>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <b-input
                    v-model="calorie"
                    id="calories"
                    type="text"
                    required
                    placeholder="Select Calories"
                  ></b-input>
                </div>
              </div>
            </div>
            <div class="field-body">
              <b-field>
                <div class="control">
                  <button
                    v-bind:class="{ 'is-primary': isDairyFree }"
                    class="button is-rounded"
                    @click="isDairyFree=!isDairyFree,updateFiler()"
                  >
                    <span>Dairy Free</span>
                  </button>
                </div>
                <div class="control">
                  <button
                    v-bind:class="{ 'is-primary': isNutFree }"
                    class="button is-rounded"
                    @click="isNutFree=!isNutFree,updateFiler()"
                  >
                    <span>Nuts Free</span>
                  </button>
                </div>
              </b-field>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="section has-background-white-bis" v-if="itemsData">
      <p class="title is-5 has-text-left">Items</p>
      <div class="columns is-centered is-multiline">
        <div v-for="(item, index) in this.searchitems()" :key="index" class="column is-one-third">
          <!--  <div v-if="(isDairyFree && !isNutFree &&  item.itemFilters!=='Contains Dairy')"> <ItemsView v-bind:item="item"/></div>
          <div v-if="(isNutFree && !isDairyFree && item.itemFilters!=='Contains Nuts')"> <ItemsView v-bind:item="item"/></div>
          <div v-else-if="(isNutFree && isDairyFree && item.itemFilters==='Normal')"> <ItemsView v-bind:item="item"/></div>
          -->
          <ItemsView v-bind:item="item"/>
        </div>
      </div>
    </div>
    <div class="section has-background-white-bis">
      <p class="title is-5 has-text-left">Meals</p>
      <div class="columns is-centered is-multiline" v-if="mealData">
        <div v-for="(meal, index) in mealData" :key="index" class="column is-one-third">
          <section class="boxes">
            <div class="box">
              <div class="media-content">
                <p class="title is-4">{{meal.mealName}}</p>
                <img src="../assets/fav-menu.jpg" alt="food">
              </div>
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
                <div class="field-body">
                  <div style="padding:5px" class="field">
                    <button
                      class="button is-primary is-pulled-right"
                      @click="addMeal(meal)"
                    >Add Favourite</button>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.column {
  display: flex;
}
.field-body {
  padding-left: 10px !important;
}
</style>


<script>
import axios from "axios";
import ItemsView from "@/components/ItemsView";

export default {
  name: "WhatsOnMenu",
  components: {
    ItemsView
  },
  data() {
    return {
      userEmail: this.$router.history.current.params.email,

      data: "",
      isDairyFree: false,
      isNutFree: false,
      filtersData: [],
      itemsData: [],
      initialData: [],
      mealData: [],
      search: "",
      calorie: ""
    };
  },
  methods: {
    getItems() {
      const path = "http://localhost:5000/items";
      axios
        .get(path)
        .then(res => {
          this.itemsData = res.data.items;
          this.initialData = res.data.items;
          console.log(this.itemsData);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
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
    updateFiler() {
      //Todo: find a better way
      const dairy = this.initialData;
      const nut = this.initialData;
      const norm = this.initialData;
      if (this.isDairyFree && !this.isNutFree) {
        this.itemsData = dairy.filter(
          item => item.itemFilters !== "Contains Dairy"
        );
      } else if (this.isNutFree && !this.isDairyFree) {
        this.itemsData = nut.filter(
          item => item.itemFilters !== "Contains Nuts"
        );
      } else if (this.isNutFree && this.isDairyFree) {
        this.itemsData = norm.filter(item => item.itemFilters === "Normal");
      } else {
        this.itemsData = this.initialData;
      }
      console.log(this.itemsData);
    },
    searchitems: function() {
      const array = [];
      return this.itemsData.filter(item => {
        if (this.search) {
          return item.itemName
            .toLowerCase()
            .includes(this.search.toLowerCase());
        } else if (this.calorie) {
          return item.itemCalories <= this.calorie;
        } else return this.itemsData;
      });
    },
    searchcalorie: function() {
      return this.itemsData.filter(item => {
        const cal = item.itemCalorie.includes(this.calorie);
        console.log(cal);
      });
    },
    addMeal(meal) {
      const userEmail = this.userEmail;
      axios({
        method: "post",
        url: `http://localhost:5000/user/${userEmail}/favouritemeal`,
        data: {
          userEmail: userEmail,
          favouriteMeal: meal.mealId
        }
      })
        .then(() => {
          this.sucess();
        })
        .catch(error => {
          console.log(error);
          this.error();
        });
    },
    sucess() {
      this.$toast.open({
        message: "Added successfully",
        type: "is-info"
      });
    },
    error() {
      this.$toast.open({
        message: "Couldn't add successfully",
        type: "is-danger"
      });
    }
  },
  created() {
    this.getItems();
    this.getMeals();
  }
};
</script>