<template>
    <v-app>
      <v-main>
        <MainContent :UserPromptTag="Sekai" :UserPromptName="Sekai_btn"></MainContent>
      </v-main>
    </v-app>
  </template>


<script>
import MainContent from '../components/MainContent.vue';

export default {
  name: 'SekaiComponent',
  
  data: () => ({
    Sekai_btn: [
      "prsk"
    ],

    Sekai: [
      "prsk_fa"
    ]
    
  }),

  components: {
    MainContent,
  },
};
</script>