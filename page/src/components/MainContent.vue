<template>
  <v-main class="bg-grey-darken-2">
    <v-row>
      <v-col min-height="100vh" cols="1"></v-col> <!--공백-->
      <v-col>
        <v-sheet class="bg-grey-darken-3" min-height="1000" rounded="lg">
          <!-- <v-btn class="bg-grey-darken-4"
            v-for="(value,key) in UserPromptTag"
            variant="text"
            :key="key"
            :text="key"
            :style="{ width: `${100 / Object.keys(UserPromptTag).length}%`, height: '60px'}"
            
          >
        </v-btn> -->
          <v-sheet class="bg-grey-darken-3" min-height="20" style="display: flex;"></v-sheet>
          <div v-for="val in SomeJson" :key="val">
            <TweetImage :ImageList="val.imgs" :arialabel="val"></TweetImage>
          </div>
        </v-sheet>
      </v-col>

      <!--셋팅 창-->
      <v-col cols="3">
        <!-- <v-sheet class="bg-grey-darken-3" min-height="30vh" rounded="lg" @click="fetchData(tag)"></v-sheet> -->
      </v-col>
      <v-col cols="1">
        <v-sheet rounded="lg" class="bg-grey-darken-2">
          <!-- 공백 -->
        </v-sheet>
      </v-col>
    </v-row>
  </v-main>
</template>

<!-- MainContent.vue -->

<script setup>
import axios from 'axios';
import TweetImage from './TweetImage.vue';


//const testjson = {"reposts": 70, "likes": 183, "bookmarks": 9, "views": 3214, "imgs": {"img0": "https://pbs.twimg.com/media/GCM8nnDagAALSrV?format=jpg&name=large"}}
//const testjson = {"replies": 3, "reposts": 228, "likes": 1348, "bookmarks": 65, "views": 23205, "imgs": {"img0": "https://pbs.twimg.com/media/GB1c9OoX0AEuoUl?format=jpg&name=large", "img1": "https://pbs.twimg.com/media/GB1c_qJXsAAwGNA?format=jpg&name=large"}}
// const tlqkf = {"Tweet0": {"replies": 2, "reposts": 315, "likes": 1318, "bookmarks": 40, "views": 15382, "imgs": {"img0": "https://pbs.twimg.com/media/GCQPOccbUAAv_Fh?format=jpg&name=large"}}, "Tweet1": {"reposts": 387, "likes": 2047, "bookmarks": 126, "views": 22963, "imgs": {"img0": "https://pbs.twimg.com/media/GCNTEdHbEAAxVqL?format=jpg&name=large"}}, "Tweet2": {"replies": 3, "reposts": 322, "likes": 1161, "bookmarks": 42, "views": 16531, "imgs": {"img0": "https://pbs.twimg.com/media/GCMl1etbUAAvxNR?format=jpg&name=large"}}, "Tweet3": {"replies": 4, "reposts": 455, "likes": 2035, "bookmarks": 55, "views": 37597, "imgs": {"img0": "https://pbs.twimg.com/media/GCMDr1jbYAAMkGE?format=jpg&name=large"}}, "Tweet4": {"reposts": 272, "likes": 1043, "bookmarks": 43, "views": 16600, "imgs": {"img0": "https://pbs.twimg.com/media/GCLOJXsbkAACnSu?format=jpg&name=large"}}, "Tweet5": {"reposts": 285, "likes": 1052, "bookmarks": 79, "views": 14589, "imgs": {"img0": "https://pbs.twimg.com/media/GCKZdZoaYAA5NlI?format=jpg&name=large"}}, "Tweet6": {"replies": 2, "reposts": 187, "likes": 1007, "bookmarks": 84, "views": 11495, "imgs": {"img0": "https://pbs.twimg.com/media/GCKWdt0aEAA-qem?format=jpg&name=large"}}, "Tweet7": {"replies": 15, "reposts": 374, "likes": 1039, "bookmarks": 72, "views": 28081, "imgs": {"img0": "https://pbs.twimg.com/media/GCIC_3-bkAAUfVd?format=jpg&name=large", "img1": "https://pbs.twimg.com/media/GCHnxAibMAATcSq?format=jpg&name=large"}}, "Tweet8": {"replies": 2, "reposts": 596, "likes": 2947, "bookmarks": 101, "views": 37365, "imgs": {"img0": "https://pbs.twimg.com/media/GCHffgCW0AAb6BU?format=jpg&name=large"}}, "Tweet9": {"reposts": 426, "likes": 1757, "bookmarks": 64, "views": 31016, "imgs": {"img0": "https://pbs.twimg.com/media/GCF5_xIbkAAjxi9?format=jpg&name=large"}}, "Tweet10": {"reposts": 277, "likes": 1119, "bookmarks": 44, "views": 17390, "imgs": {"img0": "https://pbs.twimg.com/media/GCFkQGpbQAAOaiF?format=jpg&name=large"}}, "Tweet11": {"reposts": 465, "likes": 1879, "bookmarks": 61, "views": 32015, "imgs": {"img0": "https://pbs.twimg.com/media/GCFfqjsbcAEpK2A?format=jpg&name=large"}}, "Tweet12": {"reposts": 295, "likes": 1138, "bookmarks": 46, "views": 16876, "imgs": {"img0": "https://pbs.twimg.com/media/GCEqBaybUAAkUgO?format=jpg&name=large"}}, "Tweet13": {"replies": 8, "reposts": 287, "likes": 1382, "bookmarks": 48, "views": 23818, "imgs": {"img0": "https://pbs.twimg.com/media/GCEzroYbwAAKpi4?format=jpg&name=large"}}, "Tweet14": {"replies": 3, "reposts": 327, "likes": 1426, "bookmarks": 61, "views": 19496, "imgs": {"img0": "https://pbs.twimg.com/media/GCD2HTZasAA4n1F?format=jpg&name=large"}}, "Tweet15": {"replies": 4, "reposts": 302, "likes": 1288, "bookmarks": 73, "views": 20198, "imgs": {"img0": "https://pbs.twimg.com/media/GCC6WKfbgAA71TD?format=jpg&name=large"}}, "Tweet16": {"reposts": 285, "likes": 1107, "bookmarks": 45, "views": 54410, "imgs": {"img0": "https://pbs.twimg.com/media/GAXQuGzaQAAYDoH?format=png&name=large"}}, "Tweet17": {"reposts": 289, "likes": 1031, "bookmarks": 39, "views": 16294, "imgs": {"img0": "https://pbs.twimg.com/media/GCBUKf9XoAA4wor?format=jpg&name=large"}}, "Tweet18": {"reply": 1, "reposts": 575, "likes": 2231, "bookmarks": 116, "views": 34797, "imgs": {"img0": "https://pbs.twimg.com/media/GB9IzkYa0AAxw_q?format=jpg&name=large"}}, "Tweet19": {"reply": 1, "reposts": 397, "likes": 1474, "bookmarks": 62, "views": 23025, "imgs": {"img0": "https://pbs.twimg.com/media/GB9H8oPbwAA9Pp_?format=jpg&name=large"}}, "Tweet20": {"reposts": 230, "likes": 1100, "bookmarks": 29, "views": 15700, "imgs": {"img0": "https://pbs.twimg.com/media/GB8-3fvaQAA8OT-?format=jpg&name=large"}}, "Tweet21": {"reply": 1, "reposts": 542, "likes": 1946, "bookmarks": 73, "views": 36616, "imgs": {"img0": "https://pbs.twimg.com/media/GB8lFGrakAAVISZ?format=jpg&name=large"}}, "Tweet22": {"reposts": 284, "likes": 1220, "bookmarks": 81, "views": 22094, "imgs": {"img0": "https://pbs.twimg.com/media/GB8CI20bkAAB-4b?format=jpg&name=large", "img1": "https://pbs.twimg.com/media/GB8CIR-aIAA6p54?format=jpg&name=large"}}, "Tweet23": {"reposts": 316, "likes": 1695, "bookmarks": 61, "views": 22848, "imgs": {"img0": "https://pbs.twimg.com/media/GB4Z3JYagAAaCnp?format=jpg&name=large"}}, "Tweet24": {"reply": 1, "reposts": 887, "likes": 3675, "bookmarks": 150, "views": 52726, "imgs": {"img0": "https://pbs.twimg.com/media/GB4TpOzaAAAQx7o?format=jpg&name=large"}}, "Tweet25": {"replies": 12, "reposts": 255, "likes": 1099, "bookmarks": 57, "views": 17677, "imgs": {"img0": "https://pbs.twimg.com/media/GB4FinIbgAAU4d5?format=jpg&name=large"}}, "Tweet26": {"replies": 5, "reposts": 568, "likes": 2294, "bookmarks": 136, "views": 38280, "imgs": {"img0": "https://pbs.twimg.com/media/GB315D7b0AA7lD1?format=jpg&name=large"}}, "Tweet27": {"replies": 4, "reposts": 679, "likes": 1533, "bookmarks": 89, "views": 220295, "imgs": {"img0": "https://pbs.twimg.com/media/GB3Q8dYbIAE4Lu6?format=jpg&name=large"}}, "Tweet28": {"replies": 2, "reposts": 692, "likes": 3176, "bookmarks": 190, "views": 49904, "imgs": {"img0": "https://pbs.twimg.com/media/GB1m4OhW0AAqRJX?format=jpg&name=large"}}, "Tweet29": {"replies": 3, "reposts": 228, "likes": 1348, "bookmarks": 65, "views": 23205, "imgs": {"img0": "https://pbs.twimg.com/media/GB1c9OoX0AEuoUl?format=jpg&name=large", "img1": "https://pbs.twimg.com/media/GB1c_qJXsAAwGNA?format=jpg&name=large"}}, "Tweet30": {"reposts": 406, "likes": 1328, "bookmarks": 60, "views": 28148, "imgs": {"img0": "https://pbs.twimg.com/media/GBzexlvXsAAPsBC?format=jpg&name=large"}}, "Tweet31": {"reposts": 285, "likes": 1203, "bookmarks": 34, "views": 18851, "imgs": {"img0": "https://pbs.twimg.com/media/GBywEMlaUAA42T2?format=jpg&name=large"}}, "Tweet32": {"reply": 1, "reposts": 665, "likes": 3396, "bookmarks": 158, "views": 51675, "imgs": {"img0": "https://pbs.twimg.com/media/GBw34oRWEAAkHxw?format=jpg&name=large"}}, "Tweet33": {"replies": 4, "reposts": 313, "likes": 1287, "bookmarks": 57, "views": 24950, "imgs": {"img0": "https://pbs.twimg.com/media/GBt6Mt5aoAA7Odm?format=jpg&name=large"}}, "Tweet34": {"reply": 1, "reposts": 331, "likes": 1454, "bookmarks": 66, "views": 36602, "imgs": {"img0": "https://pbs.twimg.com/media/GBtlbq1bwAAe_Ap?format=jpg&name=large"}}, "Tweet35": {"replies": 3, "reposts": 333, "likes": 1586, "bookmarks": 54, "views": 31549, "imgs": {"img0": "https://pbs.twimg.com/media/GBtT0T8a8AAA4mT?format=jpg&name=large"}}, "Tweet36": {"replies": 15, "reposts": 466, "likes": 2335, "bookmarks": 154, "views": 40526, "imgs": {"img0": "https://pbs.twimg.com/media/GBsBCCXbAAAK0cz?format=jpg&name=large"}}, "Tweet37": {"replies": 3, "reposts": 307, "likes": 1569, "bookmarks": 52, "views": 34132, "imgs": {"img0": "https://pbs.twimg.com/media/GBptIERbsAEgIql?format=jpg&name=large"}}, "Tweet38": {"reposts": 325, "likes": 1447, "bookmarks": 46, "views": 27634, "imgs": {"img0": "https://pbs.twimg.com/media/GBomh8GbwAATQwk?format=jpg&name=large"}}, "Tweet39": {"replies": 4, "reposts": 227, "likes": 1046, "bookmarks": 36, "views": 44649, "imgs": {"img0": "https://pbs.twimg.com/media/GBl7BVtbIAAXl8F?format=jpg&name=large"}}, "Tweet40": {"replies": 5, "reposts": 894, "likes": 3492, "bookmarks": 174, "views": 71799, "imgs": {"img0": "https://pbs.twimg.com/media/GBcO437akAA8VNi?format=jpg&name=large"}}}
// const fourlist = [
  //   "https://imgur.com/CRoTFLD.png",
  //   "https://imgur.com/CRoTFLD.png",
  //   "https://imgur.com/CRoTFLD.png",
  //   "https://imgur.com/CRoTFLD.png"
  // ];
  
  
  
let jsonData;
async function ffetchData(tag) {
  try {
    const response = await axios.get(`https://null4uproject.s3.ap-northeast-2.amazonaws.com/public/${tag}.json`);
    jsonData = response.data;
    // console.log(jsonData);

    return jsonData
  } catch (error) {
    console.error('Json 불러오기 실패:', error);
  }
}

jsonData = ffetchData('prsk_fa')
// console.log(jsonData)
// function fetchDataSync(tag) {
//   try {
//     const response = axios.get(`https://null4uproject.s3.ap-northeast-2.amazonaws.com/public/${tag}.json`);
//     console.log(response)
//     const jsonData = response.data;

//     // 여기에서 jsonData를 사용하거나 반환할 수 있음
//     console.log(jsonData);

//     return jsonData;
//   } catch (error) {
//     console.error('Json 불러오기 실패:', error);
//     // 에러 처리
//     throw error; // 에러를 다시 던져서 호출자에게 전달
//   }
// }
//jsonData = fetchData('prsk_fa')
//console.log(jsonData)

// for (let i=0; i < 6; i++) {
//   console.log(jsonData.)
// }


//const Json = await fetchData(UserPromptTag);


</script>



<script>
export default {
  name: 'MainCont',

  components: {
    TweetImage
  },

  props: {
    UserPromptTag: Array,
    SomeJson: Array
  },

  methods: {
    convertObjectToDictionary(objectData) {
    // JavaScript 객체를 딕셔너리로 변환하는 함수
      return Object.entries(objectData).reduce((acc, [key, value]) => {
        acc[key] = value;
        return acc;
      }, {});
    },
    async fetchData(tag) {
      try {
        // axios를 사용하여 비동기적으로 데이터를 가져옵니다.
        const response = await axios.get(`https://null4uproject.s3.ap-northeast-2.amazonaws.com/public/${tag}.json`);
        const Data = response.data;
        const jsonData = this.convertObjectToDictionary(Data);
        // console.log(jsonData);
        this.$forceUpdate();
        return jsonData;
      
      } catch (error) {
        console.error('Json 불러오기 실패:', error);
        // 에러를 다시 던져서 필요한 경우 메소드 호출자에서 처리할 수 있도록 합니다.
        throw error;
      }
    },

  }
};
</script>
