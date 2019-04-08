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