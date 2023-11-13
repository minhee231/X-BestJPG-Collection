  <template>
    <v-navigation-drawer
      model-value
      class="pt-4"
      color="grey-darken-4"
      rail-width="150"
      rail
    >
      <div>
        <v-img
          :src="'https://static.wikia.nocookie.net/1ad0b3e4-8fbd-4415-8d70-0c8c6d1fe894'"
        >
          <v-btn
            variant="text"
            :style="{ width:'150px', height: '70px'}"
            @click="toggleDropdown(0)"
          ></v-btn>
        </v-img>
        
        <v-img
          v-for="(UnitLogo, index) in UnitLogos"
          :key="`img-${index}`"
          :src="UnitLogo"
          alt="이미지 설명"
        >
          <v-btn
            variant="text"
            :style="{ width:'150px', height: '70px'}"
          >
          </v-btn>
        </v-img>

        <v-divider
          v-if="index !== UnitLogos.length - 1"
          :key="`divider-${index}`"
          class="my-2"
        ></v-divider>
      </div>
    </v-navigation-drawer>
  </template>

  <script setup>
  import { ref } from 'vue';
  const UnitLogos = [
    'https://sekai.best/images/jp/logol_outline/logo_light_sound.png',
    'https://sekai.best/images/jp/logol_outline/logo_idol.png',
    'https://sekai.best/images/jp/logol_outline/logo_street.png',
    'https://sekai.best/images/jp/logol_outline/logo_theme_park.png',
    'https://sekai.best/images/jp/logol_outline/logo_school_refusal.png'
  ];

  const dropdownState = ref(Array(UnitLogos.length + 1).fill(false));

  const toggleDropdown = (index) => {
    dropdownState[index] = !dropdownState[index];
  };
  </script>

  <script>
  export default {
    name: 'ConstrainedTest',
    data: () => ({
      links: [
        'Dashboard',
        'Messages',
        'Profile',
        'Updates',
      ],
    }),
  };
  </script>
