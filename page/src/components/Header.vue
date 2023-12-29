<template>
    <v-app-bar flat color="black">
      <v-container class="mx-auto d-flex align-center justify-center">
        <v-avatar 
        class="me-4"
        color="grey-darken-1"
        size="32"
        >
        <v-img :src="profile_image">
        </v-img>
        
        </v-avatar>
        <v-btn
          v-for=" info in HeaderLink"
          :key="info['name']"
          :text="info['name']"
          variant="text"
          @click="navigatorTo(info.path)"
        ></v-btn>
        <v-spacer></v-spacer>

        
      </v-container>
    </v-app-bar>
</template>

<script setup>
import { useRouter } from 'vue-router';
import profile_image from '@/assets/profile.png'

const router = useRouter();
const HeaderLink = [
  {"name": 'Projcet Sekai', "path": "/project-sekai/100"},
  {"name": 'mygo', "path": "/mygo/100"},
  {"name": 'introduction', "path": "/introduction"},
  {"name": 'profile', "path": "/profile"}
];

const navigatorTo = (path) => {
  router.push(path);
};

</script>

<script>
  export default {
    name: 'MainHeader',
    data: () => ({
  
    }),
  }
</script>
