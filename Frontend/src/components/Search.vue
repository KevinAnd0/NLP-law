<template>
    <div class="container col-8 mb-5" style="background-color: rgba(235, 215, 184, 0.429)">
        <div class="col h-50">
            <h3>Sökresultat:</h3>
        </div>
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
        handleSelectItem(item){
            this.item = item.documentlink
            if(this.item !== null){
                window.open("src/pdfs/" + this.item);
            }else{
                alert("Ingen dom hittad")
            }
            console.log(this.item)
        }   
    }
    
    
}
</script>

<style scoped>
.list-group-item{
    background-color: rgb(235, 215, 184);
}
.list-group-item:hover {
    background-color: rgb(199, 171, 133);
} 
  
 
</style>