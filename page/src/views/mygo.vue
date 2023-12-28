<template>
    <v-app>
      <v-main>
        <SideBar/>
        <MainContent :UserPromptTag="LeoNeed"></MainContent>
      </v-main>
    </v-app>
  </template>


<script>
import SideBar from '../components/TweetSideBar.vue'
import MainContent from '../components/MainContent.vue';

export default {
  name: 'MygoComponent',
  
  data: () => ({

  }),

  components: {
    MainContent,
    SideBar
  },
};
</script>