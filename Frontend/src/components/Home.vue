<template>
    <div>
        <form @submit="submit">
            <h2>Search links</h2>
            <input type="text" v-model="search_phrase" placeholder="write text">
            <input type="submit" value="search">
        </form>

        <div>
            <li class="text" v-for="r in results" :key="r.id">{{r}}</li> 
        </div>
       
    </div>
</template>
<script>
export default {
    computed:{
        results(){
            return this.$store.state.results
        }
    },
    methods:{
        submit(event){
            event.preventDefault()
            this.$store.commit('setSearchPhrase', {
                search_phrase: this.search_phrase
            })
            this.$store.dispatch('insertSearchPhrase')
            this.$store.dispatch('getText')
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