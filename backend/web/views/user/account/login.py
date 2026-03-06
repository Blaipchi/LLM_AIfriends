from http.client import responses

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from web.models.user import UserProfile


class LoginView(APIView):
    def post (self, request, *args, **kwargs):
        try:
            username = request.data.get('username').strip()
            password = request.data.get('password').strip()
            if not username or not password:
                return Response({
                    'result': '用户名或密码不能为空'
                })
            # 验证用户名和密码是否匹配的，如果匹配就会返回该用户名的用户对象，不匹配返回空
            user = authenticate(username=username, password=password)
            if user: # 用户名和密码正确
                user_profile = UserProfile.objects.get(user=user) # 获取一个数据，超过一个就会报错
                refresh = RefreshToken.for_user(user) # 生成jwt
                response = Response({
                    'result': 'success',
                    'user_id': user.id,
                    'username': user.username,
                    'photo': user_profile.photo.url, # 必须要加url，否者不会返回路径
                    'profile': user_profile.profile,
                })
                response.set_cookie(
                    key = 'refresh_token', # 设置cookie的key
                    value = str(refresh),
                    httponly = True, #
                    samesite = 'Lax', # 设置httponly
                    max_age = 864000 * 7, # 7天
                )
                return  response
            return Response({
                'result': '用户名或密码错误'
            })
        except:
            return Response({
                'result': '系统异常，请稍后重试'
            })