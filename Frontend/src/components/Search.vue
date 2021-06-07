<template>
    <div class="container col-8">
        <div class="col mt-3  " style="height: 50px">
            <h3>Sökresultat:</h3>
        </div>
        <div class="list-group">
            <a href="#" class="list-group-item list-group-item-action" v-for="item in lagerstedt" :key="item.id">{{item.summary}}</a> 
        </div>
    </div>
</template>
<script>
export default {
    computed:{
        lagerstedt(){
            return this.$store.state.lagerstedt
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