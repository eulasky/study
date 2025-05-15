<template>
  <div>
    <!-- Q. store.addTodo(todoText) 이렇게 써도 된다? O/X -->
    <!-- 정답은 O -->
    <!-- 써도 되지만, 별도의 함스를 따로 정의해서 작성할 것이다. -->
    <form @submit.prevent="onAddTodo">
      <!-- 양방향 바인딩으로, 사용자가 입력한 값을 사용하자. -->
      <input type="text" v-model="todoText">
      <button>CREATE</button>
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter.js'
  const store = useCounterStore()
  
  const todoText = ref('')

  // 보통은 onAddTodo로 해서 비슷하게 만들어서 구분해주기도 함
  const onAddTodo = function () {
    // 추가 로직 작성하려고...
    // 이 컴포넌트를 위한 함수로써 기능하도록
    store.addTodo(todoText.value)
    todoText.value = '' 
    // 이걸 못하게 되기 때문에 따로 정의 하는 것임
  }
</script>

<style scoped>

</style>