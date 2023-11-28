<template>
    <v-app>
      <v-main>
        <MainContent :UserPromptTag="NIGO_btn" :UserPromptName="NIGO"></MainContent>
      </v-main>
    </v-app>
  </template>


<script>
import MainContent from '../components/MainContent.vue';

export default {
  name: 'NIGOComponent',
  
  data: () => ({
    NIGO_btn: [
        "kanade",
        "mafuyu",
        "ena",
        "mizuki"
    ],

    NIGO: [
        "宵崎奏",
        "朝比奈まふゆ",
        "東雲絵名",
        "暁山瑞希"
    ]

  }),

  components: {
    MainContent,
  },
};
</script>