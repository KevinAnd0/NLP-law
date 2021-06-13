<template>
  <nav class="navbar " id="navbar">
    <div class="container-fluid">
      <span class="navbar-brand mb-0 h1">
        <router-link to="/">
          <h1>DUMSTOL <i class="fas fa-gavel"></i></h1>
        </router-link>
      </span>
      <SearchField />
    </div>
  </nav>
</template>
<script>
import SearchField from './SearchField.vue'
export default {
  components:{
    SearchField
  },
 
}
</script>

<style scoped>

a{
   color:black;
   text-decoration: none;
   
}
a:hover{
    color: rgba(0, 0, 0, 0.603)
}
.navbar{
    background-color: rgba(235, 215, 184, 0.829);
}

</style>