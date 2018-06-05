import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        username:null,
        token:null,
    },
    mutations:{
        saveToken:function(state,userToken){
            state.username = userToken.username;
            state.taken = userToken.token;
            Cookie.set('username',userToken.username,'20min')
            Cookie.set('token',userToken.token,'20min')
        },
        clearToken:function(state){
            state.username = null
            state.token = null
            Cookie.remove('username')
            Cookie.remove('token')
        }
    }
})