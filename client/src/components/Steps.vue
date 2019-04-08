<template>
  <div class="steps">
    <b-tabs position="is-centered" class="block" v-model="activeTab">
      <b-tab-item label="Periods">
        <Periods/>
      </b-tab-item>
      <b-tab-item label="Filters">
        <Filters/>
      </b-tab-item>
      <b-tab-item label="Items">
        <Items/>
      </b-tab-item>
      <b-tab-item label="Meals">
        <Meal/>
      </b-tab-item>
      <b-tab-item label="Stats">
        <div class="column">
          <div class="card">
            <div class="card-content">
              <div class="title is-4">Max Favourite Meal</div>
              <b-table :data="favMeals">
                <template slot-scope="props">
                  <b-table-column
                    field="mealid"
                    label="Meal Id"
                    width="40"
                    numeric
                  >{{ props.row.mealid }}</b-table-column>
                  <b-table-column
                    field="mealname"
                    label="Name"
                    width="40"
                    numeric
                  >{{ props.row.mealname }}</b-table-column>
                </template>
              </b-table>
              <div class="title is-4">Max Favourite Item</div>
              <b-table :data="favItem">
                <template slot-scope="props">
                  <b-table-column
                    field="itemid"
                    label="Item Id"
                    width="40"
                    numeric
                  >{{ props.row.itemid }}</b-table-column>
                  <b-table-column
                    field="itemname"
                    label="Name"
                    width="40"
                    numeric
                  >{{ props.row.itemname }}</b-table-column>
                </template>
              </b-table>
            </div>
          </div>
        </div>
      </b-tab-item>
    </b-tabs>
    <!--     <div class="section">
      <div class="columns is-centered" v-if="itemsData">
        <div v-for="(item, index) in itemsData" :key="index" class="column is-one-third">
          <div class="card">
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-48x48">
                    <img src="../assets/fav-menu.jpg" alt="food">
                  </figure>
                </div>
                <div class="media-content">
                  <p class="title is-4">{{item.itemName}}</p>
                  <p class="subtitle is-6">{{item.itemPortion}}</p>
                </div>
              </div>
              <div class="has-text-left">
                <div>
                  <strong>Filter:</strong>
                  {{item.itemFilters}}
                </div>
                <div>
                  <strong>Ingredients:</strong>
                  {{item.itemIngridents}}
                </div>
                <div>
                  <strong>Calories and Nutrients:</strong>
                  {{item.itemNutrients}}
                </div>
                <div>
                  <strong>Portion:</strong>
                  {{item.itemPortion}}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>-->
  </div>
</template>
<style>
.tabs {
  background-color: white;
}
.tab-content {
  background-color: #ddd;
}
</style>

<script>
import axios from "axios";
import Filters from "@/components/Filters";
import Items from "@/components/Items";
import Meal from "@/components/Meal";
import Periods from "@/components/Periods";

export default {
  name: "Steps",
  components: {
    Periods,
    Filters,
    Items,
    Meal
  },
  data() {
    return {
      filtersData: [],
      itemsData: [],
      activeTab: 0,
      favMeals:[],
      favItem:[]
    };
  },
  methods: {
    getFilters() {
      const path = "http://localhost:5000/filters";
      axios
        .get(path)
        .then(res => {
          this.filtersData = res.data.filters;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getItems() {
      const path = "http://localhost:5000/items";
      axios
        .get(path)
        .then(res => {
          this.itemsData = res.data.items;
        })
        .catch(error => {
          console.error(error);
        });
    },
        getFavMeal() {
      const path = "http://localhost:5000/favmeals/";
      axios
        .get(path)
        .then(res => {
          this.favMeals = res.data.favoritemeals;
                    console.log(this.favMeals);

        })
        .catch(error => {
          console.error(error);
        });
    },
      getFavItem() {
      const path = "http://localhost:5000/favitems/";
      axios
        .get(path)
        .then(res => {
          this.favItem = res.data.favoriteitems;
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
  mounted() {},
  created() {
    this.getFilters();
    this.getItems();
    this.getFavMeal();
    this.getFavItem();

  }
};
</script>