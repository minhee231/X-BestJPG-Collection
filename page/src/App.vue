<template>
  <v-app>
    <v-main>
      <HelloWorld></HelloWorld>
      <cons />
      <MainContent />
      <!-- <Content /> -->
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
//import Content from './components/Content.vue'
import Cons from './components/cons.vue'
import MainContent from './components/MainContent.vue'


export default {
  name: 'App',

  components: {
    HelloWorld,
    Cons,
    MainContent                                          
  },

  data: () => ({
    //
  }),
}
</script>
