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
          v-for="(UnitLogo, index) in UnitLogos"
          :key="`img-${index}`"
          :src="UnitLogo"
          alt="이미지 설명"
        >
          <v-btn
            variant="text"
            :key="`btn-${UnitLogo}`"
            :style="{ width:'150px', height: '70px'}"
          >
          </v-btn>
        </v-img>

        <v-divider
          v-if="index !== UnitLogos.length - 1"
          :key="`divider-${index}`"
          class="my-2"
        ></v-divider>
        <v-img
          :src="'https://storage.sekai.best/sekai-assets/character/character_select_rip/chr_tl_1.webp'"
        ></v-img>

        <!--이스터에그 버튼-->
        <v-btn
          variant="text"
          :style="{ width:'150px', height: '80px'}"
        ></v-btn>
      </div>
      
    </v-navigation-drawer>
  </template>

  <script setup>

  import sekai_logo from '../assets/UnitLogos/Sekai_Logo.png'
  import leoneed_logo from '../assets/UnitLogos/Leoneed_Logo.png'
  import momojump_logo from '../assets/UnitLogos/MoreMoreJump_Logo.png'
  import vbs_logo from '../assets/UnitLogos/VividBadSquad_Logo.png'
  import wondershow_logo from '../assets/UnitLogos/WonderShow_Logo.png'
  import nigo_logo from '../assets/UnitLogos/NIGO_Logo.png'

  const UnitLogos = [
    sekai_logo,
    leoneed_logo,
    momojump_logo,
    vbs_logo,
    wondershow_logo,
    nigo_logo
  ];


  </script>

  <script>
  export default {
    name: 'ConstrainedTest',
  };
  </script>
