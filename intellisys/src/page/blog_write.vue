<template>
  <div>
    <h2 style="padding: 10px">Blog 작성 페이지</h2>
    <div style="padding: 4% 10%">
      <div style="width: 40%">
        <b-form-group label="제목" label-for="title" class="mb-0">
          <b-form-input
            id="title"
            placeholder="제목을 입력해 주세요"
          ></b-form-input>
        </b-form-group>

        <b-form-group label="원문 링크" label-for="link" class="mb-0">
          <b-form-input
            id="link"
            placeholder="원문 링크를 입력해 주세요"
          ></b-form-input>
        </b-form-group>
        
        <b-form-group label="작성일" label-for="thumImg" class="mb-0">
          <input id="titleImg" type="date" />
        </b-form-group>

        <b-form-group label="썸네일 이미지" label-for="titleImg" class="mb-0">
          <input id="titleImg" type="file" />
        </b-form-group>

        <b-form-group label="본문 이미지" label-for="thumImg" class="mb-0">
          <input id="titleImg" type="file" />
        </b-form-group>

        <b-form-group label="썸네일 텍스트" label-for="thumTxt" class="mb-0">
          <b-form-input
            id="thumTxt"
            placeholder="썸네일 텍스트를 입력해 주세요"
          ></b-form-input>
        </b-form-group>

        <b-form-group label="요약" label-for="description" class="mb-0">
          <b-form-input
            id="description"
            placeholder="요약글을 입력해 주세요"
          ></b-form-input>
        </b-form-group>

        <b-form-group label="내용" label-for="textarea" class="mb-0">
          <b-form-textarea
            id="textarea"
            placeholder="내용을 입력해 주세요"
            rows="3"
            max-rows="6"
          ></b-form-textarea>
        </b-form-group>

        <button>제출</button>
      </div>
    </div>
  </div>
</template>
<style>
.mb-0 {
  padding-bottom: 20px;
}
</style>