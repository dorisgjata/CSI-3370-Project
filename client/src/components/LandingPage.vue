<template>
  <div id="landing" class="main">
    <div class="parallax"></div>
    <div class="parallax2">
      <img src="../landingpage/logo_transparent.png" alt="Logo" width="600" height="500">
    </div>
    <div class="header2">
      <b>Today's Menu</b>
    </div>
    <div class="content">
      <div class="header2">
        <b>Breakfast</b>
      </div>
      <!--Breakfast-->
      <div class="boxes">
        <div class="box">
          <h1>Pancakes</h1>
          <img src="../landingpage/breakfastplaceholder.jpg" alt="Fries">
          <p>Fluffy panckees served with syrup, bacon, and eggs</p>
        </div>
        <div class="box">
          <h1>Bagels</h1>
          <img src="../landingpage/Bagel-Plain-Alt.jpg" alt="bagel" height="75%">
          <p>Fresh baked New York style bagel with cream cheese option</p>
        </div>
        <div class="box">
          <h1>French Toast</h1>
          <img src="../landingpage/frenchtoast.jpg" alt="Fries">
          <p>Warm french toast with meletd butter</p>
        </div>
        <div class="box">
          <h1>Cereal</h1>
          <img src="../landingpage/cereals.jpg" alt="Fries">
          <p>Your choice of various cereals served with dairy, soy, or rice milk</p>
        </div>
      </div>
      <!--Lunch-->
      <div class="header2">
        <b>Lunch</b>
      </div>
      <div class="boxes">
        <div class="box">
          <h1>Rueben</h1>
          <img src="../landingpage/reuben.jpg" alt="Fries">
          <p>Freshly toasted reuben sandwhich served with a side of chips</p>
        </div>
        <div class="box">
          <h1>BLT Sandwich</h1>
          <img src="../landingpage/blt.jpg" alt="Fries">
          <p>Crunchy BLT sandwhich with fresh locally grown tomatoes and lettuce. Served with a side of fried</p>
        </div>
        <div class="box">
          <h1>Burrito Bowl</h1>
          <img src="../landingpage/burritoBowl.jpg" alt="Fries">
          <p>Fresh rice, lettuce, salsa and your choice of add-ons such as guac, cheese, and beans</p>
        </div>
        <div class="box">
          <h1>Cheeseburger</h1>
          <img src="../landingpage/burger.jpg" alt="Fries">
          <p>Never frozen 100% beef patty with lettuce, tomato, and cheese sandwiched in a brioche bun. Served with side of fries</p>
        </div>
      </div>
      <!--Dinner-->
      <div class="header2">
        <b>Dinner</b>
      </div>
      <div class="boxes">
        <div class="box">
          <h1>Mac & Cheese</h1>
          <img src="../landingpage/macandcheese.jpg" alt="Fries" height="75%">
          <p>Rich creamy cheese sauce with tender pasta</p>
        </div>

        <div class="box">
          <h1>Sweet & Sour Chicken</h1>
          <img src="../landingpage/sweetAndSourChicken.png" alt="Fries" height="77%">
          <p>Tender fried chicken atop a bed of white rice topped with green onions and sesame seeds</p>
        </div>

        <div class="box">
          <h1>Tacos</h1>
          <img src="../landingpage/tacos.jpg" alt="Fries">
          <p>Baked shells stuffed with your choice of: ground turkey, diced tomatos, onions, cheese, and lettuce</p>
        </div>
        <div class="box">
          <h1>Pizza</h1>
          <img src="../landingpage/pizza.jpg" alt="Pizza">
          <p>The classic fan favorite, your choice of up to 3 toppings</p>
        </div>
      </div>
    </div>
    <div class="parallax3">
      <div class="header">
        <h1>Fresh Vegetarian Options</h1>
        <img src="../landingpage/campusDining.gif" width="85%" height="90%">
      </div>
      <div class="header">
        <h1>Matches Your Prefrences</h1>
        <img src="../landingpage/campusDining3.gif" width="85%" height="90%">
      </div>
      <div class="bottom">
        <a href="https://www.tesla.com">
          <!--Add link to main site here-->
          <img src="../landingpage/Continue.png" width="60%" height="8%">
        </a>
      </div>
    </div>
  </div>
</template>
<style>
/* CSS Variables */
:root {
  --primary: #ddd;
  --secondary: rgba(219, 219, 219, 0.53);
  --text :rgb(25, 5, 38);
  --dark: #333;
  --light: #fff;
  --shadow: 0 1px 5px rgba(90, 90, 90, 0.8);
}

.content {
  background-color: white;
  z-index: -3;
  height: 2400px;
  background-repeat: repeat-y;
  background-size: cover;
  z-index: 1
}

.main {
  perspective: 1px;
  transform-style: preserve-3d;
  height: 100vh;
  overflow-x: hidden;
}

.parallax {
  position: relative;
  background-image: url("../landingpage/background.jpg");
  background-size: 100% 100%;
  background-repeat: no-repeat;
  margin-top: 60% 0 0 0;
  font-family: sans-serif;
  font-size: 4rem;
  text-align: center;
  height: 100vh;
  display: flex;
  flex: 0 1 auto;
  Transform: translateZ(-1px) scale(2);
  z-index: -1;

}

.parallax2 {
  position: relative;
  margin: -1000px 40% 800px 39%;
  height: 40vh;
  display: flex;
  flex: 0 1 inherit;
  Transform: translateZ(-2px) scale(4);
  z-index: -1;
}

.parallax3 {
  position: absolute;
  margin: 40% 0 0 0;
  font-size: 1rem;
  text-align: center;
  height: 100vh;
  width: 100%;
  
  flex: 0 1 inherit;
  Transform: translateZ(-1px) scale(2);
  z-index: -1;
}


.btn {
  background: var(--dark);
  color: var(--light);
  padding: 0.6rem 1.3rem;
  text-decoration: none;
  border: 0;
}

img {
  max-width: 100%;
  max-height: 100%;
}
.box img {
  max-width: 210px;
  max-height: auto;
}

/* Top Container */
.top-container {
  display: grid;
  grid-gap: 20px;
  grid-template-areas:
    'showcase showcase top-box-a'
    'showcase showcase top-box-b';
}

/* Showcase */
.showcase {
  grid-area: showcase;
  height: 479px;
  width: 1290px;
  background: url(../landingpage/food3.jpg);
  background-size: cover;
  background-position: center;

  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: center;
  box-shadow: var(--shadow);
}

.showcase h1 {
  font-size: 4rem;
  margin-bottom: 0;
  color: var(--light);
}

.showcase p {
  font-size: 1.3rem;
  margin-top: 0;
  color: var(--light);
}

/* Top Box */
.top-box {
  background: var(--primary);
  display: grid;
  align-items: center;
  justify-items: center;
  box-shadow: var(--shadow);
  padding: 1.5rem;
}

.top-box .price {
  font-size: 2.5rem;
}

.top-box-a {
  grid-area: top-box-a;
}

.top-box-b {
  grid-area: top-box-b;
}

/* Boxes */
.boxes {
  display: grid;
  grid-gap: 15px;
  grid-template-columns: repeat(4, minmax(200px, 1fr));
}

.box {
  background: var(--primary);
  height: 45vh;
  text-align: center;
  padding: 1% 0 1%;
  margin-top: 15%;
  margin-bottom: 1%;
  box-shadow: var(--shadow);
}

.header {
  background: var(--secondary);
  height: 95vh;
  text-align: center;
  margin: 5% 0 3% 0;
  
  box-shadow: var(--shadow);
    
}

.header2 {
  background: var(--secondary);
  height: 14vh;
  text-align: center;
  text-transform: Uppercase;
  color: var(--text);
  margin: 20% 0 20%;
  box-shadow: var(--shadow);
  font-size: 5rem; 
}

.header3{
  height: 1vh;
  text-align: center;
  color: var(--text);
  margin: 1% 0 20%;
  box-shadow: var(--shadow);
  font-size: 5rem;
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

.bottom{
  background: url("../landingpage/backgroundCut.jpg");
}

</style>

<script>
export default {
    name: "LandingPage"
}
</script>

