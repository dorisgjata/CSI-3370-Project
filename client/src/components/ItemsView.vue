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
          <strong>Nutrients:</strong>
          {{item.itemNutrients}}
        </div>
        <div>
          <strong>Portion:</strong>
          {{item.itemPortion}}
        </div>
          <div>
          <strong>Calories:</strong>
          {{item.itemCalories}}
        </div>
      </div>
      <div class="field-body">
        <div style="padding:5px" class="field">
          <button
            class="button is-primary is-pulled-right"
            @click="addItem(item)"
          >Add Favourite</button>
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
  props: ["item"],
  data() {
    return {
      userEmail: this.$router.history.current.params.email,
    };
  },
  methods: {
      addItem(item) {
      const userEmail=this.userEmail;
      axios({
        method: "post",
        url: `http://localhost:5000/user/${userEmail}/favourites`,
        data: {
          userEmail: userEmail,
          favouriteItem: item.itemId,
        }
      })
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },
  },
};
</script>