<template>
  <v-main class="bg-grey-darken-2">
    <v-row>
      <v-col>
        <v-sheet class="bg-grey-darken-3" min-height="100vh" rounded="lg">
          <div class="text-center">
            <v-img
              :key="imgtest"
              :src="'https://static.wikia.nocookie.net/1ad0b3e4-8fbd-4415-8d70-0c8c6d1fe894'"
              :style="{ width: '50%'}"
            ></v-img>
          </div>

        </v-sheet>
      </v-col>

      <!--셋팅 창-->
      <v-col cols="3">
        <v-sheet class="bg-grey-darken-3" min-height="30vh" rounded="lg"></v-sheet>
      </v-col>
      <v-col cols="1">
        <v-sheet rounded="lg" class="bg-grey-darken-2">
          <!-- 공백 -->
        </v-sheet>
      </v-col>
    </v-row>
  </v-main>
</template>

<script setup>
import axios from 'axios';

let jsonData = null;
let jsonData_length;

async function fetchData() {
  try {
    const response = await axios.get('https://null4uproject.s3.ap-northeast-2.amazonaws.com/public/prsk_fa.json');
    jsonData = response.data;
    jsonData_length = Object.keys(jsonData).length;

  } catch (error) {
    console.error('에러 발생:', error);
  }
}


fetchData();

console.log(jsonData_length)
</script>
