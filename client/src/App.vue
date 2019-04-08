<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};

</script>

<style>
body{
  height: 100%;
}
#main{
  background-image:url("./assets/background.jpg");
  background-size: cover;
  background-repeat: no-repeat;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  padding-bottom: 150px;
}
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
