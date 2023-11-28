<template>
    <v-app>
      <v-main>
        <MainContent :UserPromptTag="MoMoJump" :UserPromptName="MoMoJump_btn"></MainContent>
      </v-main>
    </v-app>
  </template>


<script>
import MainContent from '../components/MainContent.vue';

export default {
  name: 'MoMoJumpComponent',
  
  data: () => ({
    MoMoJump_btn: [
        "minori",
        "haruka",
        "airi",
        "shizuku"
    ],

    MoMoJump: [
        "花里みのり",
        "桐谷遥",
        "桃井愛莉",
        "日野森雫",
    ],
  }),

  components: {
    MainContent,
  },
};
</script>