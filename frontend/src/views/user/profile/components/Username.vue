<script setup>

import {ref, watch} from "vue";

// 接收来自父组件的参数，这里的photo 要与 Profile.vue 中定义的 username 一致
const props = defineProps(['username'])
// myusername是会变的，所以这里定义的是响应式变量
const myUsername = ref(props.username)

// 响应式变化
// 这里的watch() 方法监听了 username 参数，当 username 发生变化时，myUsername 的值也会跟着变化。
watch(() => props.username, (newValue) => {
  myUsername.value = newValue
})

defineExpose({
  myUsername
})
</script>

<template>
  <fieldset class="fieldset">
    <label class="label text-base">用户名</label>
      <input v-model="myUsername" type="text" class="input w-108">
  </fieldset>
</template>

<style scoped>

</style>