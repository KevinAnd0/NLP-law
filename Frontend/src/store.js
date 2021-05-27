import { createStore } from "vuex" 

const store = createStore({
   state:{
        name: "Vue"
   },
   mutations:{
       setName(state, x){
           state.name = x
       }
   },
   actions:{
        async ({commit}){
            let name = 'Vue with vuex'
            commit('setName', name)
        }
   }
})

export default store