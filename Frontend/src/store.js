import { createStore } from "vuex" 

const store = createStore({
   
    state:{
        results:{
            search_phrase: ""
        },
        search_result: []  
    },
   
    mutations:{
       setSearchResults(state, results){
           state.results = results
           console.log(state.results.search_phrase)

       },
    },
   
    actions:{
        insertSearchPhrase({state}){
            fetch('/api/search/' + state.results.search_phrase)
             .then(async response => {
                const data = await response.json();
                console.log(data)

            const uniqueDocuments = Array.from(new Set(data.map(a => a.id)))
                .map(id => {
                    return data.find(a => a.id === id)
            })
            console.log(uniqueDocuments) 

            
            state.search_result = uniqueDocuments
            console.log(state.search_result) 

                // check for error response
                if (!response.ok) {
                // get error message from body or default to response statusText
                const error = (data && data.message) || response.statusText;
                return Promise.reject(error);
                }

                this.totalVuePackages = data.total;
            })
            .catch(error => {
                this.errorMessage = error;
                console.log("There was an error!");
                alert("No data!!!!");
                state.search_result = " "
            });

            
        }
    }
})

export default store