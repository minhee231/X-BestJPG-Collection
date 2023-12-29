<template>
    <v-app>
      <v-main>
        <SideBar/>
        <MainContent :json_data="json_data"></MainContent>
      </v-main>
    </v-app>
  </template>


<script>
import SideBar from '@/components/TweetSideBar.vue'
import MainContent from '@/components/MainContent.vue';
import axios from 'axios';

export default {
  name: 'ProjectSekaiComponent',
  
  data: () => ({
    json_data: {}

  }),
  props: {
    likes: Array
  },

  mounted() {
    this.fetchData('prsk_fa',this.likes);
  
  },

  methods: {
    async fetchData(tag,likes) {
      try {
        const response = await axios.get(`https://null4uproject.s3.ap-northeast-2.amazonaws.com/public/best/best${likes}_${tag}.json`);
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