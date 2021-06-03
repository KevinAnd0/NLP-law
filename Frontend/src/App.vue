<template>
  <div class="container">
    <router-link to="/">DUMSTOL</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  created(){
    this.$store.dispatch('getText')  //dispatch an action
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 25px;
  
}
a{
  text-decoration: none;
}
</style>
