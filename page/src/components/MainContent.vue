<template>
  <v-main class="bg-grey-darken-2">
    <v-row>
      <v-col min-height="100vh" cols="1"></v-col> <!--공백-->
      <v-col>
        <v-sheet class="bg-grey-darken-3" min-height="1000" rounded="lg">
          <v-btn class="bg-grey-darken-4"
            v-for="Name in UserPromptName"
            variant="text"
            :key="Name"
            :text="Name"
            :style="{ width: `${100 / UserPromptName.length}%`, height: '60px'}"
          ></v-btn>
          <v-sheet class="bg-grey-darken-3" min-height="20" style="display: flex;"></v-sheet>
          <v-sheet
            class="bg-grey-darken-4"
            max-height="600"
            min-height="600"
            rounded="lg"
            :style="getGridStyle(fourlist)"
          >
          <TweetImage :ImageList="fourlist"></TweetImage>
          </v-sheet>
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
import TweetImage from './TweetImage'

let jsonData = null;
let jsonData_length;

const fourlist = [
"https://imgur.com/CRoTFLD.png",
"https://imgur.com/CRoTFLD.png",
"https://imgur.com/CRoTFLD.png",
"https://imgur.com/CRoTFLD.png"
];

function getGridStyle(fourlist) {
      const length = fourlist.length;
      let columns = 'repeat(2, 1fr)';
      let rows = 'repeat(2, 1fr)';

      if (length === 1) {
        columns = '1fr';
        rows = '1fr';
      } else if (length === 2) {
        columns = 'repeat(2, 1fr)';
        rows = '1fr';
      } else if (length === 3) {
        columns = 'repeat(3, 1fr)';
        rows = 'repeat(1, 1fr)';
      } else if (length === 4) {
        columns = 'repeat(2, 1fr)';
        rows = 'repeat(2, 1fr)';
      }

      return {
        width: '90%',
        margin: '0 auto',
        display: 'grid',
        gridTemplateColumns: columns,
        gridTemplateRows: rows,
        border: '1px solid white',
      };
    }

async function fetchData(tag) {
  try {
    const response = await  axios.get(`https://null4uproject.s3.ap-northeast-2.amazonaws.com/public/${tag}.json`);
    jsonData = response.data;
    
    jsonData_length = Object.keys(jsonData).length;
    
    return jsonData;

  } catch (error) {
    console.error('Json 불러오기 실패:', error);
  }
}


console.log(jsonData_length)
console.log(jsonData)
fetchData("prsk_fa");

</script>

<script>
export default {
  name: 'MainCont',

  components: {
    TweetImage
  },

  props: {
    UserPromptTag: Array,
    UserPromptName: Array
  },

  computed: {
    getGridStyle(fourlist) {
      const length = fourlist.length;
      let columns = 'repeat(2, 1fr)';
      let rows = 'repeat(2, 1fr)';

      if (length === 1) {
        columns = '1fr';
        rows = '1fr';
      } else if (length === 2) {
        columns = 'repeat(2, 1fr)';
        rows = '1fr';
      } else if (length === 3) {
        columns = 'repeat(2, 1fr)';
        rows = 'repeat(2, 1fr)';
      } else if (length === 4) {
        columns = 'repeat(2, 1fr)';
        rows = 'repeat(2, 1fr)';
      }

      return {
        width: '90%',
        margin: '0 auto',
        display: 'grid',
        gridTemplateColumns: columns,
        gridTemplateRows: rows,
        border: '1px solid white',
      };
    },
  }
};
</script>
