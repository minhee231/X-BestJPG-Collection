<template>
  <v-sheet
    class="bg-grey-darken-4"
    max-height="600"
    min-height="600"
    rounded="lg"
    :style="getGridStyle(ImageList)"
  >
    
  <v-img
      v-for="value in ImageList"
      :key="value"
      :src="value"
      :style="{ 
        width: '100%', 
        height: '100%', 
        objectFit: 'cover', 
        maxWidth: 'none',  
        maxHeight: 'none',
        cursor: 'pointer',
        border: '1px solid gray'
      }"
      @click="openImage(value)"
    ></v-img>
    <v-dialog v-model="dialog" max-width="800">
        <v-img :src="selectedImage" width="100%" height="100%" object-fit="contain" style="border: 3px solid gray;"></v-img>
    </v-dialog>
    <div v-for="(value,key) in arialabel" :key="key">
      <div v-if="key != 'imgs'">{{ key }}: {{ value }}</div>
      <!-- 이제 이미지들 넣으면 될듯 이쁘게 -->
    </div>
  </v-sheet>
  <v-sheet class="bg-grey-darken-3" min-height="70" style="display: flex;"></v-sheet>

</template>


<script setup>


function getGridStyle(ImageList) {
      const datalen = Object.keys(ImageList).length


      let columns = 'repeat(2, 1fr)';
      let rows = 'repeat(2, 1fr)';

      if (datalen === 1) {
        columns = '1fr';
        rows = '1fr';
      } else if (datalen === 2) {
        columns = 'repeat(2, 1fr)';
        rows = '1fr';
      } else if (datalen === 3) {
        columns = 'repeat(3, 1fr)';
        rows = 'repeat(1, 1fr)';
      } else if (datalen === 4) {
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
</script>

<script>
export default {
  name: 'TweetImage',

  props: {
    ImageList: Array,
    arialabel: Array
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