<template>
    <v-img
      v-for="(list, index) in ImageList"
      :key="index"
      :src="list"
      :style="{ 
        width: '100%', 
        height: '100%', 
        objectFit: 'cover', 
        maxWidth: 'none',  
        maxHeight: 'none',
        cursor: 'pointer',
        border: '1px solid gray'
      }"
      @click="openImage(list)"
    ></v-img>
    <v-dialog v-model="dialog" max-width="800">
        <v-img :src="selectedImage" width="100%" height="100%" object-fit="contain" style="border: 3px solid gray;"></v-img>
    </v-dialog>
  </template>
  
  <script>
  export default {
    name: 'TweetImage',
  
    props: {
      ImageList: Array
    },
  
    data() {
      return {
        dialog: false,
        selectedImage: '',
      };
    },
  
    methods: {
      openImage(list) {
        this.selectedImage = list;
        this.dialog = true;
      }
    },
  };
  </script>
  