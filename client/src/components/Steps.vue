<template>
  <div class="steps" id="stepsDemo">
    <b-tabs v-model="activeTab">
       <b-tab-item label="Add Periods">
        <Periods/>
      </b-tab-item>
      <b-tab-item label="Add Filters">
        <Filters/>
      </b-tab-item>
      <b-tab-item label="Add Items">
        <Items/>
      </b-tab-item>
      <b-tab-item label="Add Meals">
        <Meal/>
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
    </div> -->
  </div>
</template>

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
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getItems() {
      const path = "http://localhost:5000/items";
      axios
        .get(path)
        .then(res => {
          this.itemsData = res.data.items;
          console.log(this.itemsData);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  mounted() {},
  created() {
    this.getFilters();
    this.getItems();
  }
};
</script>