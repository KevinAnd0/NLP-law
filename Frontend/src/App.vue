<template>
  <div>
      <Navbar />
      <router-view></router-view>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
export default {
  components: {
    Navbar
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');
#app {
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  
}  
body {
 
 background-image: url("/src/assets/bill-oxford-OXGhu60NwxU-unsplash.jpg");
 background-color: #cccccc;
 /* background-position: center; */
 background-size: cover;
 background-attachment: fixed;
}
h1{
  font-family: Playfair Display, serif;
}

</style>
