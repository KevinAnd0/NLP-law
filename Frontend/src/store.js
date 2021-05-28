import { createStore } from "vuex" 

const store = createStore({
   
    state:{
        results: [],
        search_phrase: []
   },
   
   mutations:{
       setSearchResults(state, results){
           state.results = results
           console.log(results)
       },
       setSearchPhrase(state, data){
           console.log(data)
           state.search_phrase = data
       }

   },
   
   actions:{
        async getText ({commit}){
            let response = await fetch('/api/')
            let data  = await response
            console.log(data)
            commit('setSearchResults', data)

        },
        
        /* async insertSearchPhrase({state}){
            let response = await fetch('/api/',{
                method: 'post',
                headers: {'content-type':'application/json'},
                body: JSON.stringify(state.search_phrase)
            })
            let data = await response.json()
            console.log(data)
        } */
   }
})

export default store