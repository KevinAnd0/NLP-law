<template>
    <div>
        <li class="text" v-for="r in results" :key="r.id">{{r}}</li> 
    </div>
</template>

<script>
export default {
    computed:{
        results(){
            return this.$store.state.results
        }
    }

}
</script>

<style>

</style>