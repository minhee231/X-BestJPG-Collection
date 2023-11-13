<template>
  
    <v-main class="bg-grey-darken-2">
        <v-row>
          <v-col>
            <v-sheet class="bg-grey-darken-3"
              min-height="100vh"
              rounded="lg"
            >
            <div>
            <p>{{ tweetValue }}</p>
          </div>
          
            </v-sheet>
          </v-col>

          <!-- 셋팅-->
          <v-col cols="3">
            <v-sheet
      class="bg-grey-darken-3"
      min-height="30vh"
      rounded="lg"
    >
      
    </v-sheet>
          </v-col>
        <v-col cols="1">
          <v-sheet rounded="lg" class="bg-grey-darken-2" >
              <!-- 공백 -->
          </v-sheet>
        </v-col>

      </v-row>

    </v-main>
</template>

<script setup>

</script>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      loading: true,
      jsonData: null,
    };
  },
  async mounted() {
    try {
      const response = await axios.get('https://null4uproject.s3.ap-northeast-2.amazonaws.com/public/prsk_fa.json');
      this.jsonData = response.data;
    } catch (error) {
      console.error('에러 발생:', error);
    } finally {
      this.loading = false;
    }
  },
};
</script>







