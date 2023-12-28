<template>
  <v-app>
    <v-main>
      <Header></Header>
      <RouterView/>
    </v-main>
  </v-app>
</template>

<script>
import { RouterView } from 'vue-router';
import Header from './components/Header.vue'

export default {
  name: 'App',

  components: {
    Header,
    RouterView,
},

  data: () => ({
    //
  }),
}
</script>
