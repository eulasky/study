<template>
  <div>
    <h1>Article page</h1>
    <RouterLink :to="{ name: 'CreateView' }">[CREATE]</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
  import ArticleList from '@/components/ArticleList.vue'
  import { useArticleStore } from '@/stores/articles.js'
  import { onMounted } from 'vue'
  import { RouterLink } from 'vue-router'
  const store = useArticleStore()
  // 이 컴포넌트가 mount 될 때 게시글 전체 조회
  // onMounted 함수가 실행되었을 때, 나는
  // 어떠한 일을 수행하도록 하고 싶어. => 함수 실행
  
  onMounted(() => {
    store.getArticle()
  })


</script>

<style>

</style>
