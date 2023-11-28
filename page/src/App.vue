<template>
  <v-app>
    <v-main>
      <Header></Header>
      <Side/>
      <RouterView/>
    </v-main>
  </v-app>
</template>

<script>
import { RouterView } from 'vue-router';
import Header from './components/Header.vue'
import Side from './components/SideBar.vue'


export default {
  name: 'App',

  components: {
    Header,
    Side,
    RouterView,
},

  data: () => ({
    //
  }),
}
</script>
