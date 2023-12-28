<template>
  <v-main class="bg-grey-darken-2">
    <v-row>
      <v-col min-height="100vh" cols="1"></v-col> <!--공백-->
      <v-col>
        <v-sheet class="bg-grey-darken-3" min-height="1000" rounded="lg">
          <v-sheet class="bg-grey-darken-3" min-height="20" style="display: flex;"></v-sheet>
          <div v-for="value in json_data" :key="value">
            <TweetImage :ImageList="value.imgs" :arialabel="value"></TweetImage>
          </div>
        </v-sheet>
      </v-col>

      <v-col cols="3">
      </v-col>
      <v-col cols="1">
      </v-col>
    </v-row>
  </v-main>
</template>


<script setup>
import TweetImage from '@/components/TweetImage.vue';
</script>

<script>
export default {
  name: 'MainCont',

  components: {
    TweetImage
  },

  props: {
    json_data: Array
  },

};
</script>
