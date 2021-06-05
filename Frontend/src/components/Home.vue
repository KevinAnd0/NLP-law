<template>
    <div class="container">
        <form @submit="submit">
            <h2>Search links</h2>
            <div class="row">
                <div class="col-4">
                    <input type="text" class="form-control" id="searchField" v-model="search_phrase"  placeholder="write text">
                </div>
                <div class="col-2">
                    <button type="submit" class="btn btn-primary mb-2" id="button" value="search">Sök</button>
                </div>
            </div>       
        </form>

        <div class="list-group">
            <a href="#" class="list-group-item list-group-item-action" v-for="item in lagerstedt" :key="item.id" v-on:click="handleSelectItem(item)">{{item.summary}}</a>       
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
        
        },
         
        handleSelectItem(item){
            this.item = item.documentlink
            if(this.item !== null){
                window.open("src/pdfs/" + this.item);
            }else{
                alert("Ingen dom hittad")
            }
            console.log(this.item)
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
    .morot{
        float: left;
    }
    a:hover{
        background-color:lightgrey;
    }
</style>