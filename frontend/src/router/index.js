import { createRouter, createWebHistory } from 'vue-router'
import HomepageIndex from "@/views/homepage/HomepageIndex.vue";
import FriendIndex from "@/views/friend/FriendIndex.vue";
import CreateIndex from "@/views/create/CreateIndex.vue";
import NotFoundIndex from "@/views/error/NotFoundIndex.vue";
import LoginIndex from "@/views/user/account/LoginIndex.vue";
import RegisterIndex from "@/views/user/account/RegisterIndex.vue";
import SpaceIndex from "@/views/user/space/SpaceIndex.vue";
import ProfileIndex from "@/views/user/profile/ProfileIndex.vue";
import {useUserStore} from "@/stores/user.js";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      {
          path: '/',
          component: HomepageIndex,
          name: 'homepage-index',
          // 自定义是否需要登录才能额查看
          meta: {
            needLogin: false
          }
      },
      {
          path: '/friend/',
          component: FriendIndex,
          name: 'friend-index',
          meta: {
            needLogin: true
          }
      },
      {
          path: '/create/',
          component: CreateIndex,
          name: 'create-index',
          meta: {
            needLogin: false
          }
      },
      {
          path: '/404/',
          component: NotFoundIndex,
          name: '404',
          meta: {
            needLogin: false
          }
      },
      {
          path: '/user/account/login/',
          component: LoginIndex,
          name: 'user-account-login-index',
          meta: {
            needLogin: false
          }
      },
      {
          path: '/user/account/register/',
          component: RegisterIndex,
          name: 'user-account-register-index',
          meta: {
            needLogin: false
          }
      },
      {
          path: '/user/space/:user_id/',
          component: SpaceIndex,
          name: 'user-space-index',
          meta: {
            needLogin: false
          }
      },
      {
          path: '/user/profile/',
          component: ProfileIndex,
          name: 'user-profile-index',
          meta: {
            needLogin: true
          }
      },
      {
          // 没有找到页面就会匹配到404页面
          path: '/:pathMatch(.*)*',
          component: NotFoundIndex,
          name: 'not-found',
          meta: {
            needLogin: false
          }
      }
  ],
})

// 加入一个守卫，在跳转之前进行判断
router.beforeEach((to, from) => {
    const user = useUserStore()
    if(to.meta.needLogin && user.hasPulledUserInfo && !user.isLogin()){
        return {
            name: 'user-account-login-index'
        }
    }
    return true
})

export default router
