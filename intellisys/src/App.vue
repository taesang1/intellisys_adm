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
          <h2 style="padding: 10px">Blog 목록 조회</h2>
          <b-table striped hover :items="items" class=""></b-table>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import layout_header from "./layout/layout_header.vue";
import layout_meun from "./layout/layout_meun.vue";

import axios from "axios";

export default {
  components: {
    layout_header,
    layout_meun,
  },
  data: function () {
    return {
      blog_list: [],
      items: [
          { No: 76, 제목: "[ET시론]디지털 전환을 바라는 C레벨에게",설명: "디지털 전환(DT:Digital Transformation)이 기업의 최대 화두다. 얼마 전까지 디지털 전환은 기업 미래전략의 상위 현안 중 하나 정도로 겨우 여겨졌는데, 코로나 사태 이후에는 생존을 위한 필수 전략 과제로 올라섰다. 새 정부도 디지털 플랫폼...",일자: "2022-04-16"},
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { age: 38, first_name: 'Jami', last_name: 'Carney' }
        ]
    };
  },
  created: function () {
    axios
      .get("http://127.0.0.1:8000/blog")
      .then((Response) => console.log((this.blog_list = Response.data[0])))
      .catch((Error) => {
        console.log(Error);
      });
  },
};
</script>
