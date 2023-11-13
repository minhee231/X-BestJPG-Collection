<template>

    <v-main class="bg-grey-darken-3">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
              <v-list rounded="lg" class="bg-grey-darken-4">
                <v-list-item>
                  FanArt
                </v-list-item>

                <v-divider class="my-2"></v-divider>
                <v-list-item
                  v-for="Tagname in TagNames"
                  :key="Tagname"
                  link
                  :title="Tagname"
                ></v-list-item>

              </v-list>
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet class="bg-grey-darken-2"
              min-height="100vh"
              rounded="lg"
              title="ㅇㅇ"
            >
              아하!
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
</template>

<script setup>
  const TagNames = [
    '호시마치 스이세이',
    '사쿠라 미코',
    '아쿠땅',
    '톼삼',
  ]
</script>

<script>
  export default {
    name: 'ConstrainedComponent',
    data: () => ({
      X_FATag: [
        '#あくあーと', //스이세이
        '#miko_Art', //미코
        'あくあーと', //아쿠땅
        '#TOWART', //토와
      ],

      PixivTag: [
        '星街すいせい', // 스이세이
        'さくらみこ', //미코 
        '湊あくあ ', //아쿠땅
        '토코야미' //톼삼
      ]
    }),
  }
</script>