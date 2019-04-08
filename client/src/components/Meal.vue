<template>
  <div id="meal">
    <section>
      <b-tabs>
        <b-tab-item label="Select Items">
          <div class="column">
            <b-table :data="itemsData" :checked-rows.sync="checkedRows" checkable>
              <template slot-scope="props">
                <b-table-column
                  field="itemId"
                  label="Item Id"
                  width="40"
                  numeric
                >{{ props.row.itemId }}</b-table-column>
                <b-table-column
                  field="itemName"
                  label="Name"
                  width="40"
                  numeric
                >{{ props.row.itemName }}</b-table-column>
                <b-table-column
                  field="itemFilters"
                  label="Filter"
                  width="40"
                  numeric
                >{{ props.row.itemFilters}}</b-table-column>
              </template>
            </b-table>
          </div>
        </b-tab-item>

        <b-tab-item :disabled="checkedRows.length!==3" label="Add Meal">
          <div class="columns">
            <div v-for="(item, index) in checkedRows" :key="index" class="column is-one-third">
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
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <b-field label="Period"></b-field>
            </div>
            <div class="field-body">
              <div class="field">
                <b-select v-model="addMealForm.mealPeriod" placeholder="Select a period">
                  <option
                    v-for="period in periodsData"
                    :value="period.periodId"
                    :key="period.periodId"
                  >
                    <div>{{ period.periodName }}</div>
                  </option>
                </b-select>
              </div>
            </div>
          </div>
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <b-field label="Meal Id" label-for="meal-id"/>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <b-input
                    v-model="addMealForm.mealId"
                    id="meal-id"
                    type="text"
                    required
                    placeholder="Enter Meal Id"
                  ></b-input>
                </div>
              </div>
            </div>
          </div>
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <b-field label="Meal Name" label-for="meal-name"/>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <b-input
                    v-model="addMealForm.mealName"
                    id="meal-name"
                    type="text"
                    required
                    placeholder="Enter Meal Name"
                  ></b-input>
                </div>
              </div>
            </div>
          </div>
          <div class="field-body">
            <div style="padding:5px" class="field">
              <button class="button is-primary is-pulled-right" @click="onSubmit">Submit</button>
            </div>
          </div>
        </b-tab-item>
        <div class="column">
          <div class="card">
            <div class="card-content">
              <div class="title is-4">Current Meals</div>
              <b-table :data="mealData" class="is-fullwidth">
                <template slot-scope="props">
                  <b-table-column field="mealId" label="Meal Id">{{ props.row.mealId }}</b-table-column>
                  <b-table-column field="mealName" label="Name">{{ props.row.mealName }}</b-table-column>
                  <b-table-column field="foodItem1" label="Item1">{{ props.row.foodItem1}}</b-table-column>
                  <b-table-column field="foodItem2" label="Item2">{{ props.row.foodItem2}}</b-table-column>
                  <b-table-column field="foodItem3" label="Item3">{{ props.row.foodItem3 }}</b-table-column>
                  <b-table-column field="mealPeriod" label="Period">{{ props.row.mealPeriod }}</b-table-column>
                  <b-table-column field="mealPeriod" label="Delete">
                    <button
                      type="button"
                      class="button"
                      @click="deleteMeal(props.row.mealId)"
                    >Delete</button>
                  </b-table-column>
                </template>
              </b-table>
            </div>
          </div>
        </div>
      </b-tabs>
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Meal",
  data() {
    return {
      checkedRows: [],
      itemsData: [],
      periodsData: [],
      mealData: [],
      addMealForm: {
        mealId: "",
        foodItem1: "",
        foodItem2: "",
        foodItem3: "",
        mealPeriod: "",
        mealName: ""
      }
    };
  },
  methods: {
    getItems() {
      const path = "http://localhost:5000/items";
      axios
        .get(path)
        .then(res => {
          this.itemsData = res.data.items;
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
    getPeriods() {
      const path = "http://localhost:5000/periods";
      axios
        .get(path)
        .then(res => {
          this.periodsData = res.data.periods;
          console.log(this.periodsData);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addMeal(payload) {
      axios({
        method: "post",
        url: "http://localhost:5000/meal",
        data: {
          mealId: payload.mealId,
          foodItem1: payload.foodItem1,
          foodItem2: payload.foodItem2,
          foodItem3: payload.foodItem3,
          mealPeriod: payload.mealPeriod,
          mealName: payload.mealName
        }
      })
        .then(function(response) {
          console.log(payload);
          this.success();
        })
        .catch(function(error) {
          console.log(error);
        });
      this.initForm();
    },
    deleteMeal(id) {
      const path = `http://localhost:5000/meal/${id}`;
      axios
        .delete(path)
        .then(() => {
        })
        .catch(error => {
        });
    },
    initForm() {
      this.addMealForm.mealId = "";
      this.addMealForm.foodItem1 = "";
      this.addMealForm.foodItem2 = "";
      this.addMealForm.foodItem3 = "";
      this.addMealForm.mealPeriod = "";
      this.addMealForm.mealName = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        foodItem1: this.checkedRows[0].itemId,
        foodItem2: this.checkedRows[1].itemId,
        foodItem3: this.checkedRows[2].itemId,
        mealId: this.addMealForm.mealId,
        mealPeriod: 1,
        mealName: this.addMealForm.mealName
      };
      this.addMeal(payload);
    }
  },
  updated() {
    console.log(this.checkedRows);
  },
  created() {
    this.getItems();
    this.getMeals();
    this.getPeriods();
  }
};
</script>