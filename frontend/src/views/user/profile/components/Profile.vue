<script setup>
import {ref, watch} from "vue";

// 接收来自父组件的参数，这里的photo 要与 Profile.vue 中定义的 profile 一致
const props = defineProps(['profile'])
// myusername是会变的，所以这里定义的是响应式变量
const myProfile = ref(props.profile)

// 响应式变化
watch(() => props.profile, (newValue) => {
  myProfile.value = newValue
})

defineExpose({
  myProfile
})
</script>

<template>
  <fieldset class="fieldset">
    <label class="label text-base">简介</label>
    <textarea v-model="myProfile" rows="6" class="textarea w-108"></textarea>
  </fieldset>
</template>

<style scoped>

</style>