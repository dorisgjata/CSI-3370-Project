<template>
 <section class="boxes">
      <div class="box">

                <div class="media-content">
                  <p class="title is-4">{{item.itemName}}</p>
                </div>
                <img src="../assets/fav-menu.jpg" alt="food">

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
          </section>   
</template>
<style>
/* CSS Variables */
:root {
  --primary: #ddd;
  --dark: #333;
  --light: #fff;
  --shadow: 0 1px 5px rgba(104, 104, 104, 0.8);
}


/* Boxes */
.boxes {
  display: grid;
  grid-gap: 15px;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}

.box {
  background: var(--primary);
  text-align: center;
  padding: 1.5rem 2rem;
  box-shadow: var(--shadow);
}

/* Info */
.info {
  background: var(--primary);
  box-shadow: var(--shadow);
  display: grid;
  grid-gap: 35px;
  grid-template-columns: repeat(2, 1fr);
  padding: 5rem;
  font-size: 19px;
}

 
</style>
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