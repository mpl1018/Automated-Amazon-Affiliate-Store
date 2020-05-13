<template>
    <div>
      <b-navbar toggleable="lg" class="site-navbar bg-white py-2">
          
          <b-navbar-brand class="d-flex align-items-center justify-content-between">
            <div class="logo">
              <div class="site-logo">
                <router-link class="js-logo-clone" to="/" >MASCARILLAS</router-link>
              </div>
            </div>
          </b-navbar-brand>

          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
          <b-collapse id="nav-collapse" is-nav>
          <b-container>
            <b-navbar-nav  class="d-flex align-items-center justify-content-between">
              
              <b-nav-item-dropdown text="MASCARILLAS">
                <!-- <b-dropdown-item href="#">FFP3</b-dropdown-item> -->
                <b-dropdown-item><router-link to="/FFP3-N95-FFP2">FFP3/N95/FFP2</router-link></b-dropdown-item>
                <b-dropdown-item><router-link to="/medicas">Médicas</router-link></b-dropdown-item>
                <b-dropdown-item><router-link to="/infantiles">Infantiles</router-link></b-dropdown-item>
              </b-nav-item-dropdown>
              <b-nav-item><router-link to="/gafas" >GAFAS</router-link></b-nav-item>
              <b-nav-item><router-link to="/guantes" >GUANTES</router-link></b-nav-item>
              <b-nav-item><router-link to="/desinfectantes" >DESINFECTANTES</router-link></b-nav-item>
              <b-nav-item><router-link to="/otros" >OTROS</router-link></b-nav-item>              
            </b-navbar-nav>

            <b-navbar-nav class="ml-auto">
              <b-nav-item href="https://www.facebook.com/Mascarillas-Online-105843177654160" target="_blank"><img src="https://img.icons8.com/android/24/000000/facebook.png"/></b-nav-item>
              <b-nav-item href="https://www.instagram.com/tumascarilla/" target="_blank"><img src="https://img.icons8.com/metro/26/000000/instagram-new.png"/></b-nav-item>
            </b-navbar-nav>
          </b-container>
          </b-collapse>
      </b-navbar>
    </div>
</template>

