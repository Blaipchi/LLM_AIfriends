from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from web.models.user import UserProfile


class RegisterView(APIView):
    def post(self, request):
        try:
            username = request.data['username'].strip()
            password = request.data['password'].strip()
            if not username or not password:
                return Response({
                    'result': '用户名或密码不能为空'
                })
            # 用户名不能重复
            if User.objects.filter(username=username).exists():
                return Response({
                    'result': '用户名已存在'
                })
            # 在User数据库里面创建一个user
            user = User.objects.create_user(username=username, password=password)
            user_profile = UserProfile.objects.create(user=user)
            refresh = RefreshToken.for_user(user)
            response = Response({
                'result': 'success',
                'user_id': user.id,
                'username': user.username,
                'photo': user_profile.photo.url,  # 必须要加url，否者不会返回路径
                'profile': user_profile.profile,
            })
            response.set_cookie(
                key='refresh_token',  # 设置cookie的key
                value=str(refresh),
                httponly=True,  #
                samesite='Lax',  # 设置httponly
                max_age=864000 * 7,  # 7天
            )
            return response
        except:
            return Response({
                'result': '系统异常，请稍后重试'
            })