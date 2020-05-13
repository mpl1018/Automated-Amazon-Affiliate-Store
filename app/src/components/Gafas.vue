<template>
    <div>

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
              <div class="card myItem" v-for = "(i,index) in gafas" :key="index"  style="width: 17rem;">
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
        gafas: "gafas"
      })
    },
    created(){
        if (this.gafas[0]==null) this.getProds("gafas");
    },
    methods: {
        ...mapActions({
          getProds: 'getProds'
        })
    },
}
</script>