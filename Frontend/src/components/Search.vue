<template>
    <div class="container col-8 mb-5">
        <div class="col h-50">
            <h3 class="rounded-bottom">Sökresultat för: {{search_phrase}}</h3>
        </div>
        <div class="list-group">
            <a href="#" tabindex="1" class="list-group-item list-group-item-action" v-for="item in search_result" :key="item.id" v-on:click="handleSelectItem(item)">AVGJORD DOMS DOKUMENT: {{item.documentlink}} // SAMMANFATTNING: {{item.summary}}</a>   
        </div>
    </div>
</template>
<script>
export default {
    computed:{
        search_result(){
            for(var i = 0; i < this.$store.state.search_result.length; i++){
                var obj = this.$store.state.search_result[i];
                if(obj.documentlink === null){
                    obj.documentlink = "Det finns ingen dom än"
                }

            }

            return this.$store.state.search_result
        }, 
        search_phrase(){
            return this.$store.state.results.search_phrase
        }
    },
    methods:{
        handleSelectItem(item){
            this.item = item.documentlink
            if(this.item !== null && this.item !== "Det finns ingen dom än"){
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
.list-group-item[tabindex]:focus{
    background-color: rgb(218, 195, 195);
}
h3{
    background-color: rgb(235, 215, 184);
} 
</style>