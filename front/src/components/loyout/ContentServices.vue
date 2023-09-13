<script setup>

import ServicesBlock from "@/components/Content/boxServices/ServicesBlock.vue";
</script>

<template>
  <main>
    <div class="container" style="margin-top: 50px">
      <div class="lonload " style="min-height: 400px;">
        <div class="center-block list-products-block">
          <div class="col-md-12 col-sm-12 col-lg-12 col-xs-12 hidden-xs full-list-products">
            <div class="col-md-2 col-lg-2 col-sm-2 col-xl-2 title-table">Название Услуги</div>
            <div class="col-md-2 col-lg-2 col-sm-2 col-xl-2 title-table">Описание</div>
          </div>
          <div id="productsMain" style="width: 100%">
            <services-block></services-block>
          </div>
        </div>
      </div>
    </div>

  </main>
</template>

<style scoped>

</style>