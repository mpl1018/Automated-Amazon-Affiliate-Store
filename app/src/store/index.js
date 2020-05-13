import Vue from 'vue'
import Vuex from 'vuex'
import {db} from '../main'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    productos:[],
    gafas: [],
    guantes: [],
    desinfectantes: [],
    otros: [],
    infantiles: [],
    medicas: [],
  },
  getters:{
    productos(state){
      return state.productos;
    },
    gafas(state){
      return state.gafas;
    },
    guantes(state){
      return state.guantes;
    },
    desinfectantes(state){
      return state.desinfectantes;
    },
    otros(state){
      return state.otros;
    },
    infantiles(state){
      return state.infantiles;
    },
    medicas(state){
      return state.medicas;
    },
  },
  mutations: {
    async get(state, producto){
      try{
        let local = JSON.parse(localStorage.getItem(producto));
        if (local == null || new Date().getTime()-local.timeStamp>300000){
          console.log('hola');
          const snapshot = await db.collection(producto).get();
          const productos = []; 
    
          snapshot.forEach(element => {
              let prodData = element.data();
              prodData.id = element.id;
              productos.push(prodData)
          });
          
          let array_obj = {
            data: productos,
            timeStamp: new Date().getTime()
          }
  
          if (producto == 'productos')
            state.productos = productos;
            
          
          else if (producto == 'gafas')
            state.gafas = productos;
  
          
          else if (producto == 'guantes')
            state.guantes = productos;
  
          
          else if (producto == 'desinfectantes')
            state.desinfectantes = productos;
  
          
          else if (producto == 'infantiles')
            state.infantiles = productos;
  
          
          else if (producto == 'medicas')
            state.medicas = productos;
  
          
          else if (producto == 'otros')
            state.otros = productos;
  
          
          localStorage.setItem(producto, JSON.stringify(array_obj));
        }
        else {
          console.log('pedo')
          if (producto == 'productos')
            state.productos = local.data;
            
          
          else if (producto == 'gafas')
            state.gafas = local.data;
  
          
          else if (producto == 'guantes')
            state.guantes = local.data;
  
          
          else if (producto == 'desinfectantes')
            state.desinfectantes = local.data;
  
          
          else if (producto == 'infantiles')
            state.infantiles = local.data;
  
          
          else if (producto == 'medicas')
            state.medicas = local.data;
  
          
          else if (producto == 'otros')
            state.otros = local.data;
        } 



  
      }catch(error){
        console.log(error);
      }
    }
  },
  actions: {
    getProds({ commit }, prod) {
      commit("get", prod)
    }
  },
  modules: {
  },
});
