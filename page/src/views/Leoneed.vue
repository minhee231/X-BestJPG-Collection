<template>
    <v-app>
      <v-main>
        <MainContent :UserPromptTag="LeoNeed" :UserPromptName="LeoNeed_btn"></MainContent>
      </v-main>
    </v-app>
  </template>


<script>
import MainContent from '../components/MainContent.vue';

export default {
  name: 'LeoNeedComponent',
  
  data: () => ({
    LeoNeed_btn: [
      "ichika",
      "saki",
      "honami",
      "shiho"
    ],

    LeoNeed: [
      "星乃一歌",
      "天馬咲希",
      "望月穂波",
      "日野森志歩"
    ]

  }),

  components: {
    MainContent,
  },
};
</script>