<script setup>
import HeaderServices from "@/components/loyout/headerServices.vue";
import ContentServices from "@/components/loyout/ContentServices.vue";
</script>

<template>
  <header-services></header-services>
  <content-services></content-services>
</template>

<style scoped>

.card:hover {
  background-color: aliceblue;
}

body::-webkit-scrollbar {
  width: 5px; /* ширина всей полосы прокрутки */
}

body::-webkit-scrollbar-track {
  background: rgba(196, 196, 196, 0.47); /* цвет зоны отслеживания */
}

.body::-webkit-scrollbar-thumb {
  background-color: rgb(136, 144, 169); /* цвет бегунка */
  border-radius: 20px; /* округлось бегунка */
  border: 3px solid rgba(162, 162, 162, 0.99); /* отступ вокруг бегунка */
}


.nav-tabs>li.active>a, .nav-tabs>li.active>a:focus, .nav-tabs>li.active>a:hover {
  color: #555;
  cursor: default;
  background-color: #fff;
  border: 1px solid #ddd;
  border-color: transparent;
  margin-bottom: -1px;
  padding-bottom: 1px;
  border-bottom: 2px solid #7079dc;
  transition: border-bottom .3s ease;
  min-height: 35px;
  padding-bottom: 10px;
}


</style>
