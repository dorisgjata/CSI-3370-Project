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
                <b-field label="Calories" label-for="item-calories"/>
              </div>
              <div class="field-body">
                <div class="field">
                  <div class="control has-icon has-icon-right">
                    <b-input
                      v-model="addItemForm.itemCalories"
                      id="item-calories"
                      type="text"
                      required
                      placeholder="Enter Item Calories"
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
      <div class="column">
        <div class="card">
          <div class="card-content">
            <div class="title is-4">Current Food Items</div>
            <b-table :data="itemsData">
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
                  field="itemCalories"
                  label="Calories"
                  width="40"
                  numeric
                >{{ props.row.itemCalories }}</b-table-column>
                <b-table-column
                  field="itemFilters"
                  label="Filter"
                  width="40"
                  numeric
                >{{ props.row.itemFilters}}</b-table-column>
                <b-table-column label="Delete" width="40">
                  <button type="button" class="button" @click="deleteItem(props.row.itemId)">Delete</button>
                </b-table-column>
                <b-table-column label="Update" width="40">
                  <button
                    type="button"
                    value="edit"
                    class="button"
                    @click="editItem(props.row),isUpdateModalActive = true"
                  >Update</button>
                </b-table-column>
              </template>
            </b-table>
          </div>
        </div>
      </div>
    </div>
    <b-modal :active.sync="isUpdateModalActive" :width="640" scroll="keep">
      <div class="card">
        <div class="card-content">
          <form class="w-100" ref="editItemModal" id="edit-modal" title="Edit Item" hide-footer>
            <section>
              <b-field id="form--edit-id-group" label="Item Id:" label-for="form-edit-id-input">
                <b-input
                  disabled
                  id="form-edit-id-input"
                  type="int"
                  v-model="editItemForm.itemId"
                  required
                  placeholder="Enter Id"
                ></b-input>
              </b-field>
                 <b-field id="form--edit-id-group" label="Filter Id:" label-for="form-edit-id-filter">
                <b-input
                  disabled
                  id="form-edit-id-filter"
                  type="int"
                  v-model="editItemForm.itemFilters"
                  required
                  placeholder="Item Filter Id"
                ></b-input>
              </b-field>
              <b-field
                id="form--edit-name"
                label=" Item Name:"
                label-for="form-edit-name-input"
              >
                <b-input
                  id="form-edit-name-input"
                  type="text"
                  v-model="editItemForm.itemName"
                  required
                  placeholder="Enter Item Name"
                ></b-input>
              </b-field>
              <b-field
                id="form--edit-ingredients"
                label="itemIngredients:"
                label-for="form-edit-itemIngredients"
              >
                <b-input
                  id="form-edit-itemIngredients"
                  type="int"
                  v-model="editItemForm.itemIngridents"
                  required
                  placeholder="Enter Ingredients"
                ></b-input>
              </b-field>
              <b-field
                id="form--edit-itemNutrients"
                label="itemNutrients:"
                label-for="form-edit-itemNutrients"
              >
                <b-input
                  id="form-edit-itemNutrients"
                  type="int"
                  v-model="editItemForm.itemNutrients"
                  required
                  placeholder="Enter Nutrients"
                ></b-input>
              </b-field>
              <b-field
                id="form--edit-itemCalories"
                label="itemCalories:"
                label-for="form-edit-itemCalories"
              >
                <b-input
                  id="form-edit-itemCalories"
                  type="int"
                  v-model="editItemForm.itemCalories"
                  required
                  placeholder="Enter Calories"
                ></b-input>
              </b-field>
              <button class="button is-primary" @click="onSubmitUpdate">Update</button>
              <button class="button is-danger" @click="onResetUpdate">Reset</button>
            </section>
          </form>
        </div>
      </div>
    </b-modal>
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
      isUpdateModalActive: false,
      addItemForm: {
        filterId: "",
        itemId: "",
        itemName: "",
        itemPortion: "",
        itemIngridents: "",
        itemNutrients: "",
        itemitemCalories: ""
      },
      editItemForm: {
        itemFilters: "",
        itemId: "",
        itemName: "",
        itemPortion: "",
        itemIngridents: "",
        itemNutrients: "",
        itemCalories: ""
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
          console.log(this.data);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    deleteItem(id) {
      const path = `http://localhost:5000/items/${id}`;
      axios
        .delete(path)
        .then(() => {
          this.getItems();
        })
        .catch(error => {
          this.getItems();
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
          itemNutrients: payload.itemNutrients,
          itemCalories: payload.itemCalories
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
      this.addItemForm.itemCalories = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        filterId: this.addItemForm.filterId,
        itemId: this.addItemForm.itemId,
        itemName: this.addItemForm.itemName,
        itemPortion: this.addItemForm.itemPortion,
        itemIngridents: this.addItemForm.itemIngridents,
        itemNutrients: this.addItemForm.itemNutrients,
        itemCalories: this.addItemForm.itemCalories
      };
      this.addItem(payload);
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.isUpdateModalActive = false;
      const payload = {
        itemId: this.editItemForm.itemId,
        itemName: this.editItemForm.itemName,
        itemPortion: this.editItemForm.itemPortion,
        itemIngridents: this.editItemForm.itemIngridents,
        itemNutrients: this.editItemForm.itemNutrients,
        itemFilters: this.editItemForm.itemFilters,
        itemCalories: this.editItemForm.itemCalories
      };
      this.updateItem(payload, this.editItemForm.itemId);
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.isUpdateModalActive = false;
      this.initForm();
      this.getItems();
    },
    editItem(item) {
      this.editItemForm = item;
    },
    updateItem(payload, itemId) {
      const path = `http://localhost:5000/items/${itemId}`;
      axios
        .post(path, payload)
        .then(() => {
          console.log(payload)
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
        });
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