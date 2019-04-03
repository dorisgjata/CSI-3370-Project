<template>
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
              <div class="field-body">
              <div style="padding:5px" class="field">
                <button class="button is-primary is-pulled-right" @click="onSubmit">Add Favourite</button>
              </div>
            </div>
            </div>
          </div>   
</template>

<script>
import axios from "axios";

export default {
  name: "ItemsView",
  props: ['item'],
  data() {
    return {
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        filterId: this.addItemForm.filterId,
        itemId: this.addItemForm.itemId,
        itemName: this.addItemForm.itemName,
        itemPortion: this.addItemForm.itemPortion,
        itemIngredients: this.addItemForm.itemIngredients,
        itemNutrients: this.addItemForm.itemNutrients
      };
      this.addItem(payload);
    },
  },
};
</script>