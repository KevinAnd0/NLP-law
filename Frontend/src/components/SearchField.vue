<template>
    
    <form @submit="submit" class="d-flex w-50">
            
        <input type="search" class="form-control me-2" v-model="search_phrase"  placeholder="Sök i vägledande domar..." aria-label="Search">
      
        <button type="submit" class="btn btn-secondary">Sök</button>
                        
    </form>
    
</template>

<script>
export default {
    data(){
        return{
            search_phrase: ""
        }
    },
    methods:{
        submit(event){
            
            this.$router.push('search') // redirect to 'Search.vue'
            this.$store.commit('setSearchResults', {
                search_phrase: this.search_phrase
            })
            this.$store.dispatch('insertSearchPhrase')
            this.search_phrase = ""
            event.preventDefault()
        },
    
        
    }

}
</script>

<style>

</style>