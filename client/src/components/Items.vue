<template>
  <div id="items">
    <div class="columns is-mobile is-centered">
      <div class="column is-half">
        <form class="card">
          <div class="card-content">
            <div class="title is-4">Add Food Items</div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <b-field label="Filters"></b-field>
              </div>
              <div class="field-body">
                <div class="field">
                  <b-select v-model="addItemForm.filterId" placeholder="Select a filter">
                    <option v-for="filter in data" :value="filter.filterId" :key="filter.filterId">
                      <div>{{ filter.filterName }}</div>
                    </option>
                  </b-select>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <b-field label="Item Id" label-for="item-id"/>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <b-input
                      v-model="addItemForm.itemId"
                      id="item-id"
                      type="text"
                      required
                      placeholder="Enter Item Id"
                    ></b-input>
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <b-field label="Item Name" label-for="item-name"/>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control">
                    <b-input
                      v-model="addItemForm.itemName"
                      id="item-name"
                      type="text"
                      required
                      placeholder="Enter Item Name"
                    ></b-input>
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <b-field label="Portion" label-for="item-portion"/>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control has-icon has-icon-right">
                    <b-input
                      v-model="addItemForm.itemPortion"
                      id="item-portion"
                      type="text"
                      required
                      placeholder="Enter Item Portion"
                    ></b-input>
                  </div>
                </div>
              </div>
            </div>
            <div class="field is-horizontal">
              <div class="field-label is-normal">
                <b-field label="Ingredients" label-for="item-ingredients"/>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control has-icon has-icon-right">
                    <b-input
                      v-model="addItemForm.itemIngridents"
                      id="item-ingredients"
                      type="text"
                      required
                      placeholder="Enter Item Ingredients"
                    ></b-input>
                  </div>
                </div>
              </div>
            </div>
            <div class="step-content has-text-centered">
              <div class="field is-horizontal">
                <div class="field-label is-normal">
                  <b-field label="Nutrients" label-for="item-nutrients"/>
                </div>
                <div class="field-body">
                  <div class="field">
                    <div class="control">
                      <b-input
                        v-model="addItemForm.itemNutrients"
                        id="item-nutrients"
                        type="text"
                        required
                        placeholder="Enter Item Nutrients"
                      ></b-input>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="field-body">
              <div style="padding:5px" class="field">
                <button class="button is-primary is-pulled-right" @click="onSubmit">Submit</button>
              </div>
            </div>
          </div>
        </form>
      </div>
      <div class="column ">
            <div class="card">
          <div class="card-content">
            <div class="title is-4">Current Food Items</div>
            <b-table :data="itemsData" >
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
                field="itemPortion"
                label="Portion"
                width="40"
                numeric
              >{{ props.row.itemPortion }}</b-table-column>
              <b-table-column
                field="itemFilters"
                label="Filter"
                width="40"
                numeric
              >{{ props.row.itemFilters}}</b-table-column>
            </template>
          </b-table>
      </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Items",
  data() {
    return {
      data: [],
      itemsData: [],
      addItemForm: {
        filterId: "",
        itemId: "",
        itemName: "",
        itemPortion: "",
        itemIngridents: "",
        itemNutrients: ""
      }
    };
  },
  methods: {
    getFilters() {
      const path = "http://localhost:5000/filters";
      axios
        .get(path)
        .then(res => {
          this.data = res.data.filters;
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
    addItem(payload) {
      axios({
        method: "post",
        url: "http://localhost:5000/items",
        data: {
          filterId: payload.filterId,
          itemId: payload.itemId,
          itemName: payload.itemName,
          itemPortion: payload.itemPortion,
          itemIngridents: payload.itemIngridents,
          itemNutrients: payload.itemNutrients
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
    initForm() {
      this.addItemForm.filterId = "";
      this.addItemForm.itemId = "";
      this.addItemForm.itemName = "";
      this.addItemForm.itemPortion = "";
      this.addItemForm.itemIngridents = "";
      this.addItemForm.itemNutrients = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        filterId: this.addItemForm.filterId,
        itemId: this.addItemForm.itemId,
        itemName: this.addItemForm.itemName,
        itemPortion: this.addItemForm.itemPortion,
        itemIngridents: this.addItemForm.itemIngridents,
        itemNutrients: this.addItemForm.itemNutrients
      };
      this.addItem(payload);
    },
    success() {
      this.$toast.open({
        message: "Added successfully!",
        type: "is-success"
      });
    }
  },
  mounted() {},
  created() {
    this.getFilters();
    this.getItems();
  }
};
</script>