<template>
    <v-app>
      <v-main>
        <MainContent :UserPromptTag="LeoNeed"></MainContent>
      </v-main>
    </v-app>
  </template>


<script>
import MainContent from '../components/MainContent.vue';

export default {
  name: 'LeoNeedComponent',
  
  data: () => ({
    

  }),

  components: {
    MainContent,
  },
};
</script>