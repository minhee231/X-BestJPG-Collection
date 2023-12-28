<template>
    <v-app>
      <v-main>
        <SideBar/>
        <MainContent :SomeJson="json_data"></MainContent>
      </v-main>
    </v-app>
  </template>


<script>
import SideBar from '../components/TweetSideBar.vue'
import MainContent from '../components/MainContent.vue';
import axios from 'axios';

export default {
  name: 'ProjectSekaiComponent',
  
  data: () => ({
    json_data: {}

  }),
  mounted() {
    this.fetchData('mygo');
  },

  methods: {
    async fetchData(tag) {
      try {
        const response = await axios.get(`https://null4uproject.s3.ap-northeast-2.amazonaws.com/public/${tag}.json`);
        const Data = response.data;
        console.log(Data);
        this.json_data = { ...this.json_data, ...Data };
        return Data;
      
      } catch (error) {
        console.error('Json 불러오기 실패:', error);
        throw error;
      }
    },
  },

  components: {
    MainContent,
    SideBar
  },
};
</script>