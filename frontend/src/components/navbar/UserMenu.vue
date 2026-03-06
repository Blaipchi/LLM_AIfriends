<script setup>


 import {useUserStore} from "@/stores/user.js";
 import UserSpaceIcon from "@/components/navbar/icons/UserSpaceIcon.vue";
 import UserLogoutIcon from "@/components/navbar/icons/UserLogoutIcon.vue";
 import UserProfileIcon from "@/components/navbar/icons/UserProfileIcon.vue";

 const user = useUserStore()

 // 主动关闭菜单
 function closeMenu() {
  const element = document.activeElement
  if (element && element instanceof HTMLElement) element.blur()
 }
</script>

<template>
  <div class="dropdown dropdown-end">
    <div tabindex="0" role="button" class="avatar btn- btn-circle w-8 h-8 mr-6">
      <div class="w-8 rounded-full">
        <img :src="user.photo" alt="">
      </div>
    </div>
    <ul tabindex="-1" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-lg">
      <li>
        <RouterLink @click="closeMenu" :to="{name:'user-space-index', params:{user_id: user.id}}">
          <div class="avatar">
            <div class="w-10 rounded-full">
              <img :src="user.photo" alt="">
            </div>
          </div>
          <!--    line-clamp-1最多一行超过一行省略号      -->
          <span class="text-base font-bold line-clamp-1 break-all">{{ user.username }} </span>
        </RouterLink>
      </li>
      <li>
        <RouterLink @click="closeMenu" :to="{name:'user-space-index', params:{user_id: user.id}}" class="text-sm font-bold py-3">
          <UserSpaceIcon />
          个人空间
        </RouterLink>
      </li>
      <li>
        <RouterLink @click="closeMenu" :to="{name:'user-profile-index'}" class="text-sm font-bold py-3">
          <UserProfileIcon />
          编辑资料
        </RouterLink>
      </li>
      <li></li>
      <li>
        <a class="text-sm font-bold py-3">
          <UserLogoutIcon />
          退出登录
        </a>
      </li>
    </ul>
  </div>
</template>

<style scoped>

</style>