<template>
  <v-app-bar flat color="black">
    <v-container class="mx-auto d-flex align-center justify-center">
      <v-avatar 
      class="me-4"
      color="grey-darken-1"
      size="32"
      >
      <v-img
        :src="'https://imgur.com/CRoTFLD.png'"
      >
      </v-img>
      
      </v-avatar>

      <v-btn
        v-for="Header in HeaderLink"
        :key="Header"
        :text="Header"
        variant="text"
      ></v-btn>
      <v-spacer></v-spacer>

      
    </v-container>
  </v-app-bar>
</template>

<script setup>
const HeaderLink = [
  'Tweets',
  'Profile'
]
</script>

<script>
export default {
  name: 'ConstrainedHeader',
  data: () => ({
    links: [
      'Dashboard',
      'Messages',
      'Profile',
      'Updates',
    ],
  }),
}
</script>
