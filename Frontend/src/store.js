import { createStore } from "vuex" 

const store = createStore({
   
    state:{
        
        lagerstedt: []
   },
   
   mutations:{
       setSearchResults(state, results){
           state.results = results
           console.log(results)

       },
   },
   
   actions:{
        
        async insertSearchPhrase({state}){
            let response = await fetch('/api/search/' + state.results.search_phrase)
            let data = await response.json()
            console.log(data)


            const uniqueDocuments = Array.from(new Set(data.map(a => a.id)))
             .map(id => {
                return data.find(a => a.id === id)
             })
            console.log(uniqueDocuments) 

            
            state.lagerstedt = uniqueDocuments
            console.log(state.lagerstedt)      
       
        }
    }
})

export default store