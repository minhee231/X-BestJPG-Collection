<template>
  <v-app>
    <v-navigation-drawer  class="bg-grey-darken-2" v-model="drawer">
      <v-sheet
        color="grey-darken-4"
        class="pa-4"
      >
        <v-avatar
          class="mb-4"
          size="64"
          id="avatar"
          @mouseover="handleMouseOver"
          @mouseleave="handleMouseLeave"
          @click="goEgg"
        >
        <v-img :src="profile_image"></v-img></v-avatar>

        <div>Minhee</div>
      </v-sheet>
      
      <v-list :class="'bg-grey-darken-3'">
        <v-list-item
        v-for="link in links"
        :key="link"
        :prepend-icon="link.icon"
        :title="link.text"
        :class="'bg-grey-darken-3'"
        @click="goLink(link.link)"
        ></v-list-item>
      </v-list>
    </v-navigation-drawer>


    
    <v-main class="bg-grey-darken-1">
    <v-row>
      <v-col min-height="100vh" cols="1"></v-col> <!--공백-->
      <v-col>
        <v-sheet class="bg-grey-darken-1" min-height="1" rounded="lg">
          <v-sheet class="bg-grey-darken-1" min-height="20" style="display: flex;"></v-sheet>
          <v-card class="bg-grey-darken-3">
            <h1>페이지 소개</h1>
            <p>지정한 태그의 트윗의 이미지를 불러와 특정 좋아요 수 만큼 분류하여 보여줍니다.</p>
            <p><br>프로세카, 마이고 트윗을 불러와 분류하고 있습니다.<br></p>
            <p><br>6시간 마다 트윗 업데이트 하고 있습니다.</p>
          </v-card>
        </v-sheet>
      </v-col>

      <v-col cols="3">
      </v-col>
      <v-col cols="1">
      </v-col>
    </v-row>
  </v-main>

      
  </v-app>
</template>

<script setup>
import profile_image from '@/assets/profile.png'

import { useRouter } from 'vue-router';
const router = useRouter();

function goEgg()
{
  router.push("/Egg")
}

const  links = [
  {'icon': 'mdi-github', 'text': 'Github', 'link': 'https://github.com/minhee231/X-BestJPG-Collection'},
  {'icon': 'mdi-post', 'text': 'Tistory', 'link': 'https://minhee-goo.tistory.com/'},
  
]
</script>

<script>
  export default {
    name: 'IntorductionCompo',
    data: () => ({
      cards: ['Today', 'Yesterday'],
      drawer: null,
    }),

    methods: {
      goLink(link)
      {
        window.open(link, '_blank');
      },
        handleMouseOver() {
        document.getElementById('avatar').style.opacity = '0.7';
      },
      handleMouseLeave() {
        document.getElementById('avatar').style.opacity = '1';
      },
    },
  }
</script>