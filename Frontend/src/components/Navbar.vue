<template>
  <nav class="navbar " id="navbar">
    <div class="container-fluid">
      <span class="navbar-brand mb-0 h1">
        <router-link to="/">
          <h1>DUMSTOL <i class="fas fa-gavel"></i></h1>
        </router-link>
      </span>
      <!-- <form @submit="submit" class="d-flex w-50">
        <input class="form-control me-2" type="search" v-model="search_phrase" placeholder="Sök i vägledande domar..." aria-label="Search">
        <button class="btn btn-outline-secondary" type="submit">Sök</button>
      </form> -->
      <!-- <form @submit="submit" class="d-flex w-50">
            
        <input type="search" class="form-control me-2" v-model="search_phrase"  placeholder="Sök i vägledande domar...">
      
        <button type="submit" class="btn btn-outline-secondary mb-2">Sök</button>
                
              
        </form> -->
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
  // methods:{
  //       submit(event){
  //           event.preventDefault()
  //           this.$store.commit('setSearchResults', {
  //               search_phrase: this.search_phrase
  //           })
  //           this.$store.dispatch('insertSearchPhrase')
        
  //       }
        
  //   },

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