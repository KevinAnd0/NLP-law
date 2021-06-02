<template>
    <div>
        <form @submit="submit">
            <h2>Search links</h2>
            <input type="text" v-model="search_phrase" placeholder="write text">
            <input type="submit" value="search">
        </form>

        <div>
            <ul>
                <li v-for="item in lagerstedt" :key="item.id">{{item.summary}}</li>
            </ul>
        </div>

        <!-- <section v-for="item in lagerstedt" :key="item.keyword" >
            <div class="text">
                <h2>{{item.keyword}}</h2>
            </div>
            <div>{{lagerstedt}}</div>
        </section> -->
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