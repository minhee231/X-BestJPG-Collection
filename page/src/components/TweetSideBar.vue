  <template>
    <v-navigation-drawer
      model-value
      class="pt-4 fixed"
      color="grey-darken-4"
      rail-width="150"
      max-height="10"
      rail
    >
      <div>
        <v-btn class="bg-grey-darken-3" variant="text" :style="{ width:'150px', height: '60px'}">likes</v-btn>
        
        <v-btn
          v-for="like in likes_button"
          :key="like"
          :text="like"
          variant="text"
          :style="{ width:'150px', height: '60px'}"
          @click="changePath(like)"
        ></v-btn>
        <v-divider class="my-2"></v-divider> <!--선-->
      </div>
      
    </v-navigation-drawer>
  </template>

<script setup>

const likes_button = [
  100,
  300,
  500,
  1000,
  3000
]

  </script>

  <script>
  export default {
    name: 'TweetSide',

    data: () => ({
  
  }),

  methods: {
    changePath(likes) {
      const current_path = this.$route.path;
      const newPath = current_path.replace(/\/(\d+)$/, `/${likes}`);
      this.$router.push({ path: newPath, params: { likes: likes } });
    }
  }
};
  </script>

<style scoped>
.fixed {
  position: fixed;
}
</style>
