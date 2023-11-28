<template>
    <v-app>
      <v-main>
        <MainContent :UserPromptTag="VBS_btn" :UserPromptName="VBS"></MainContent>
      </v-main>
    </v-app>
  </template>


<script>
import MainContent from '../components/MainContent.vue';

export default {
  name: 'VBSComponent',
  
  data: () => ({
    VBS_btn: [
      "kohane",
      "an",
      "akito",
      "toya"
    ],

    VBS: [
        "小豆沢こはね",
        "白石杏",
        "東雲彰人",
        "青柳冬弥",
    ]

  }),

  components: {
    MainContent,
  },
};
</script>