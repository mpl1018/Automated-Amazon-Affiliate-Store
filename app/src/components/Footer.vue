<template>
    <div>

            <!-- <a class="btn" v-b-toggle.collapse-2 data-toggle="collapse" role="button" aria-expanded="false" aria-controls="FFP2">
              Más información
            </a>
            <b-collapse id="collapse-2">
              <b-card>{{des}}</b-card>
            </b-collapse> -->
        <div id="accordion" class="text-center">  
        <div class="card" > 
            <div class="card-header" id="headingTwo">
            <h1 class="mb-0">
                <button class="btn btn-link collapsed"  v-b-toggle.collapse-2>
                CORONAVIRUS. ¿Qué es? 
                </button>
            </h1>
            </div>

            <b-collapse id="collapse-2" class=" card-body">
                <p>      Los coronavirus son un grupo de virus muy amplio y que pueden causar diferentes alteraciones de la salud (como un resfriado o afecciones más graves como neumonía o bronquitis). El virus de Wuhan o 2019-nCoV es una especie perteneciente a este grupo, y la transmisión se estima que es tanto respiratoria (gotas respiratorias de más de 5 micras) como por contacto de superficies contaminadas.

                    Es importante destacar que el virus puede CONTAGIARSE ANTES de mostrar síntomas, por lo que las medidas de prevención son interesantes incluso si no se acerca a nadie que los muestre.   </p> 
            </b-collapse>       
            
        </div>
        <div class="card">
            <div class="card-header" id="headingThree">
            <h2 class="mb-0">
                <button class="btn btn-link collapsed" v-b-toggle.collapse-3 data-toggle="collapse" >
                ¿Qué recomiendan las autoridades? 
                </button>
            </h2>
            </div>
            <b-collapse id="collapse-3" class="card-body">
                <p>      Las autoridades sanitarias recomiendan el uso de mascarillas combinadas con desinfectante de manos, así como medidas de precaución básicas: estornudar en el codo y no en la mano, lavarse las manos frecuentemente, evitar aglomeraciones, beber agua para humedecer la garganta, etc..
                Si decidimos salir de casa, es muy recomendable hacerse con una mascarilla (ojo, no todas sirven!) y un pequeño desinfectante (sobre todo si utilizamos transporte público).</p>
            </b-collapse>

        </div>

        <div class="card">
            <div class="card-header" id="headingThree">
            <h1 class="mb-0">
                <button class="btn btn-link collapsed"  v-b-toggle.collapse-4>
                ¿QUÉ MASCARILLAS NOS PROTEGEN?
                </button>
            </h1>
            </div>
            <b-collapse id="collapse-4" class="card-body">
                <p>A pesar de lo que vemos tan a menudo por la calle, las mascarillas quirúrgicas (un filtro simple de color blanco o azul) NO funcionan para protegernos contra la transmisión de este virus, sino que pueden dar una falsa sensación de seguridad.

                Las mascarillas ratificadas por médicos y personal sanitario cualificado son del tipo FFP3, preferiblemente, aunque del tipo FFP2 alto pueden servir, ya que el tamaño de este virus es menor a 0,6 micras. 
                El precio de las máscaras contra estos virus ronda los 5-10 euros y ofrecen un 99% de filtración (son las de máxima protección). En las últimas semanas ha aumentado exponencialmente la demanda, pero es importante recordar que la mascarilla que compremos debe cumplir los requisitos para protegernos.</p>
            </b-collapse>  


        </div>

        <div class="card">
            <div class="card-header" id="headingThree">
            <h5 class="mb-0">
                <button class="btn btn-link collapsed" v-b-toggle.collapse-5 >
                protocolo de higiene de manos
                </button>
            </h5>
            </div>
            <b-collapse id="collapse-5" class="card-body">
                <p>
                En cuanto a la desinfección de manos, el Ministerio de Sanidad, insiste en realizar un estricto protocolo de higiene de manos (incluso cuando usamos mascarilla). Por el momento afirman que un lavado con agua, jabón y desinfectante de manos es suficiente. Estos virus se inactivan tras 5 minutos de contacto con un desinfectante normal, incluyendo la lejía doméstica que podemos utilizar para limpiar y desinfectar superficies.       </p>     
            </b-collapse>
         
        </div>
        </div>

        <footer class="site-footer custom-border-top">
        <div class="container">
            <div class="row">
            <div class="col-lg-5 ml-auto mb-5 mb-lg-0">
                <div class="row">
                <div class="col-md-12">
                    <h3 class="footer-heading mb-4">INFO DE CONTACTO</h3>
                    <ul class="list-unstyled">
                    <li>Avinguda Diagonal, 639, 641, 08028 Barcelona</li>
                    <li>mascarillavirus@gmail.com</li>
                    </ul>
                </div>
            </div>
            
            </div>
            </div>

        </div>
        <div class="row pt-5 mt-5 text-center">
            <div class="col-md-12">
            <p>
            Made with <b-icon-heart-fill></b-icon-heart-fill> by <a href="https://github.com/mpl1018" target="_blank" class="text-primary">mpl1018</a>
            </p>
            </div>
            
        </div>
        </footer>
    </div>
</template>