<template>
    <div class="min-vh-100 container rounded-bottom " style=" background-color: rgba(235, 215, 184, 0.429)">
       

        <div class="col rounded-3 mb-3 " style="height:200px;">
            <h1 class="display-4">DUMSTOL</h1>
            <h2>Vägledande domar för dummies</h2>
        </div>
    
        <div class="d-none d-sm-block">
            <div class="row">
                <div class="col-6 col-sm-6">
                    <img src="/src/assets/jing-xi-lau-Y5oVH2tNN9U-unsplash.jpg" class="rounded-3 border border-dark w-100">
                </div>
                
                <div class="col-4 col-sm-6 rounded-3">
                    <h2>För dig som konsument</h2>
                    <p class="lead "> I vår app har vi valt att fokusera på vägledande domar rörande konsumentfrågor.</p>
                </div>
        </div>
        
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