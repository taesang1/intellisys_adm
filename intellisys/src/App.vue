<template>
  <div>
    <layout_header />
    <!-- <p>{{ blog_list[0]['serial'] }}</p> -->
    <b-container class="bv-example-row" style="max-width: 100%; height: 100%">
      <b-row style="height: 100%">
        <b-col style="padding: 0px 0px; width: 190px; max-width: 190px; height: 100%">
          <layout_meun />
        </b-col>
        <b-col style="height: 100%">
          <!-- https://bootstrap-vue.org/docs/components/table#table -->
          <router-view></router-view>
          <!-- <ad/> -->
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import layout_header from "./layout/layout_header.vue";
import layout_meun from "./layout/layout_meun.vue";

export default {
  name : 'App',
  components: {
    layout_header,
    layout_meun,
  }
};

</script>
