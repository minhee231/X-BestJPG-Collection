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
  name: 'WonderShowComponent',
  
  data: () => ({
    LeoNeed_btn: [
      "tsukasa",
      "emu",
      "nene",
      "rui"
    ],

    LeoNeed: [
        "天馬司",
        "鳳えむ",
        "草薙寧々",
        "神代類",
    ]

  }),

  components: {
    MainContent,
  },
};
</script>