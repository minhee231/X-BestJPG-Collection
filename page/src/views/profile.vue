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
    LeoNeed: {
      "ichika": "星乃一歌",
      "saki": "天馬咲希",
      "honami": "望月穂波",
      "shiho": "日野森志歩"
    }

  }),

  components: {
    MainContent,
  },
};
</script>