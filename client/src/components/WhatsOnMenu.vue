<template>
  <div class="conatiner">
    <div class="columns">
           <div class="column">
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
              <b-field label="Prefered Calories" label-for="calories"/>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <b-input id="calories" type="text" required placeholder="Select Calories"></b-input>
                </div>
              </div>
            </div>
            <div class="field-body">
              <b-field>
                <button
                  v-bind:class="{ 'is-primary': isDairyFree }"
                  class="button is-rounded"
                  @click="isDairyFree=!isDairyFree,dairyFree()"
                >
                  <span>Dairy Free</span>
                </button>

                <button
                  v-bind:class="{ 'is-primary': isNutFree }"
                  class="button is-rounded"
                  @click="isNutFree=!isNutFree,dairyFree()"
                >
                  <span>Nuts Free</span>
                </button>
              </b-field>
            </div>
          </div>
      </div>
      </div>
   
 
    </div>

    <div class="section">
      <div class="columns is-centered" v-if="itemsData">
        <div v-for="(item, index) in this.searchitems()" :key="index" class="column is-one-third">
          <!--  <div v-if="(isDairyFree && !isNutFree &&  item.itemFilters!=='Contains Dairy')"> <ItemsView v-bind:item="item"/></div>
          <div v-if="(isNutFree && !isDairyFree && item.itemFilters!=='Contains Nuts')"> <ItemsView v-bind:item="item"/></div>
          <div v-else-if="(isNutFree && isDairyFree && item.itemFilters==='Normal')"> <ItemsView v-bind:item="item"/></div>
          -->
          <ItemsView v-bind:item="item"/>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.column {
  display: flex;
}
</style>


<script>
import axios from "axios";
import ItemsView from "@/components/ItemsView";

export default {
  name: "WhatsOnMenu",
  components: {
    ItemsView,
  },
  data() {
    return {
      data: "",
      isDairyFree: false,
      isNutFree: false,
      filtersData: [],
      itemsData: [],
      initialData: [],
      search: ""
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
    updateFiler() {
      //Todo: find a better way
      const dairy = this.initialData;
      const nut = this.initialData;
      const norm = this.initialData;
      if (this.isDairyFree && !this.isNutFree) {
        console.log("before", this.itemsData);
        this.itemsData = dairy.filter(
          item => item.itemFilters !== "Contains Dairy"
        );
        console.log("after", this.itemsData);
      } else if (this.isNutFree && !this.isDairyFree) {
        console.log("before", this.itemsData);
        this.itemsData = nut.filter(
          item => item.itemFilters !== "Contains Nuts"
        );
        console.log("after", this.itemsData);
      } else if (this.isNutFree && this.isDairyFree) {
        console.log("before", this.itemsData);
        this.itemsData = norm.filter(item => item.itemFilters === "Normal");
        console.log("after", this.itemsData);
      } else {
        console.log("idk", this.initialData);
        this.itemsData = this.initialData;
      }
      console.log(this.itemsData);
    },
    nutFree() {
      const array = this.itemsData;
      const nutfree = [];
      array.forEach(item => {
        if (item.itemFilters !== "Contains nuts") {
          nutfree.push(item);
        }
      });
      this.itemsData = nutfree;
    },
    normal() {
      const array = this.itemsData;
      const normal = [];
      array.forEach(item => {
        if (item.itemFilters === "Normal") {
          normal.push(item);
        }
      });
      this.itemsData = this.initialData;
    },
    searchitems: function() {
      return this.itemsData.filter(item => {
        return item.itemName.toLowerCase().includes(this.search.toLowerCase());
      });
    }
  },
  updated() {
    console.log("dairy", this.isDairyFree);
    console.log("nuts", this.isNutFree);
    if (this.isDairyFree && !this.isNutFree) {
    }
    if (this.isNutFree && !this.isDairyFree) {
    } else if (this.isNutFree && this.isDairyFree) {
    }
  },
  created() {
    this.getItems();
  }
};
</script>