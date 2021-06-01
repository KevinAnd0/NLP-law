<template>
    <div>
        <form @submit="submit">
            <h2>Search links</h2>
            <input type="text" v-model="search_phrase" placeholder="write text">
            <input type="submit" value="search">
        </form>

        <div>
            <p class="text" v-for="(lager, i) of lagerstedt" :key="i">{{ lager.keyword }}</p>
        </div>
       
    </div>
</template>
<script>
export default {
    computed:{
        lagerstedt(){
            return this.$store.state.lagerstedt
        }
    },
    methods:{
        submit(event){
            event.preventDefault()
            this.$store.commit('setSearchResults', {
                search_phrase: this.search_phrase
            })
            this.$store.dispatch('insertSearchPhrase')
        
        }
        
    },
    
    
}
</script>

<style  scoped>
    form{
        margin-top: 15px;
        background-color: grey;
        border-radius:5px;
        padding:10px;
    }
</style>