<template>
  <section class="info">
    <img src="../assets/FoodCourt.png" width="604" height="409" id="FoodCourt" alt="Food Court">
    <div class="content has-text-left">
      <h1>Pioneer Food Court</h1>
      <br>
      <strong>Chick-Fil-A:</strong>
      Monday to Friday: 10:00am to 7:00pm
      <br>
      <strong>Subway:</strong>
      Monday to Friday: 10:00am to 7:00pm
      <br>
      <strong>Panda Express:</strong>
      Monday to Friday: 10:00am to 7:00pm
      <br>
      <strong>Moe's Southeast Grill:</strong>
      Monday to Friday: 10:00am to 7:00pm
    </div>
  </section>
</template>
<style>
:root {
  --primary: #ddd;
  --dark: #333;
  --light: #fff;
  --shadow: 0 1px 5px rgba(104, 104, 104, 0.8);
}
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
export default {
  name: "Contact"
};
</script>
