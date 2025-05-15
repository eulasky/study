<template>
  <div>
    <!-- 나중에는 for문으로 반복
      우선 화면 구성을 위해서 3개를 직접 보여주기
    -->
    <!-- 
      v-for는 반복문을 실행한 것일 뿐이고, 
      TodoListItem 컴포넌트에게 todo 정보를 prop 시켜 주자!
    -->
    <TodoListItem
      v-for="todo in store.todos"
      :key="todo.id"
      :todo="todo"
    />
  </div>
</template>

<script setup>
  import TodoListItem from '@/components/TodoListItem.vue'
  import { useCounterStore } from '@/stores/counter.js'

  const store = useCounterStore()

</script>

<style scoped>

</style>