<template>
    <div>
    <div class="site-blocks-cover">
      <div class="container">
        <div class="row">
          <div class="col-md-6 ml-auto order-md-2 align-self-start">
            <div class="site-block-cover-content">
            <h2 class="sub-title">#Recíbelas en casa, sin salir de casa.</h2>
            <h1>MASCARILLAS</h1>
            <p><router-link class="btn btn-black rounded-0"  to="/FFP3-N95-FFP2">Comprar ahora</router-link></p>
            </div>
          </div>
          <div class="col-md-6 order-1 align-self-end">
              <img src="../assets/images/m1.jpg" alt="Image" class="img-fluid">
          </div>
        </div>
      </div>
    </div>

   <div class="site-section">
      <div class="container">
        <div class="row">
          <div class="title-section text-center mb-5 col-12">
            <h2 class="text-uppercase">Productos más vendidos</h2>
            <a class="btn" v-b-toggle.collapse-2 data-toggle="collapse" role="button" aria-expanded="false" aria-controls="FFP2">
              Más información
            </a>
            <b-collapse id="collapse-2">
              <b-card>{{des}}</b-card>
            </b-collapse>


          </div>
        </div>
        <div class="row">
              <div class="card myItem" v-for = "(i,index) in productos" :key="index" >
                <img class="card-img-top" :src="i.imagen"  alt="Card image cap" width="300" height="200">
                <div class="card-body">
                  <p class="card-text"><a class="text-dark"  target="_blank" :href="i.link">{{i.titulo}}</a></p>
                  <strong class="item-price"> {{i.precio}}</strong>
                </div>
              </div>
        </div>
      </div>
    </div>



    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    data(){
        return{
            des: "En está página podrás encontrar todos los productos útiles para la crisis causada por el COVID-19",
        }
    },
    computed: {
      ...mapGetters({
        productos: "productos"
      })
    },
    created(){
        if (this.productos[0]==null) this.getProds("productos");
    },
    methods: {
        ...mapActions({
          getProds: 'getProds'
        })
    },
}
</script>

<style>
 .myItem{
   width: 17rem;
   margin-bottom: 10px;
   margin-left: 1%;
 }
  @media only screen and (max-width: 768px) {
   .myItem{
     margin-left: 20%;
   }
  }
</style>