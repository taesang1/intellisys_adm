<template>
  <div>
    <h2 style="padding: 10px">Blog 목록 조회</h2>
    <p style="padding: 0px 15px; width: max-content;">총갯수: {{items.length}}</p>
    <table class="text-center">
        <tr style="color:white; background-color:rgba(78, 106, 134, 0.5);">
            <th>No</th>
            <th>제목</th>
            <th>설명</th>
            <th>일자</th>
            <th>-</th>
        </tr>
        <tr v-for="item in items" :key="item.title" style="border-bottom: 1px solid #eceeef">
            <td><span v-html="item.serial"></span></td>
            <td><span v-html="item.title"></span></td>
            <td><span v-html="item.description"></span></td>
            <td><span v-html="item.publishedAt"></span></td>
            <td style="display:flex;">
                <button style="margin-right: 10px;">편집</button>
                <button>삭제</button>
            </td>
        </tr>
    </table>
    <div class="text-center" style="margin-top: 15px;">
      <button style="margin-right: 10px;">First</button>
      <button v-for="page in pages" :key="page" style="margin-right: 10px;">{{page}}</button>
      <button>Last</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function () {
    return {
      items: [
        ],
      pages:[
      ]
    };
  },
  created: function () {
    axios
      .get("http://127.0.0.1:8000/blog")
      .then((Response) => console.log((this.items = Response.data,this.pages = set_page(Response.data.length) )))
      .catch((Error) => {
        console.log(Error);
      });
  },
};

function set_page(e){
  var p = 0
  var list = []
  if (e > 10){
    if (e%5){
      p = e/5+1
      for (var i = 1; i < p; i++){
        list.push(i)
      }
    }
    return list
  }
  return list.push(1)
}
</script>

<style>
    button{
        width: max-content;
        border: solid 1px #c0c0c0;
    }
</style>