import Vue from 'vue'
import VueRouter from 'vue-router'
import Landpage from '../components/Landpage.vue'
import Gafas from '../components/Gafas.vue'
import Guantes from '../components/Guantes.vue'
import Desinfectantes from '../components/Desinfectantes.vue'
import Otros from '../components/Otros.vue'
import Infantiles from '../components/Infantiles.vue'
import Medicas from '../components/Medicas.vue'
import FFP3 from '../components/FFP3.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Landpage',
    component: Landpage
  },
  {
    path: '/gafas',
    name: 'Gafas',
    component: Gafas
  },
  {
    path: '/guantes',
    name: 'Guantes',
    component: Guantes
  },
  {
    path: '/desinfectantes',
    name: 'Desinfectantes',
    component: Desinfectantes
  },
  {
    path: '/otros',
    name: 'Otros',
    component: Otros
  },
  {
    path: '/infantiles',
    name: 'Infantiles',
    component: Infantiles
  },
  {
    path: '/medicas',
    name: 'Medicas',
    component: Medicas
  },
  {
    path: '/FFP3-N95-FFP2',
    name: 'FFP3',
    component: FFP3
  },
]

const router = new VueRouter({
  routes
})

export default router
