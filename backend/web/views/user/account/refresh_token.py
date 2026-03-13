from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class RefreshTokenView(APIView):
    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({
                    'result': 'refresh token不存在'
                }, status= 401) # 必须加401, 用于判断
            refresh = RefreshToken(refresh_token)# 自动检查refresh token是否在有效期内，如果过期了就会报异常
            # 在用refresh token 刷新 access 的时候，会同时刷新refresh token
            # 这样只要用户在7天内登录过，就会自动延长七天有效期
            # 所以用户只要连续打开网站的时间没有超过7天的话，就不需要重新登录，提高用户的体验
            if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
                refresh.set_jti()# 刷新
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token),
                })
                response.set_cookie(
                    key = 'refresh_token', # 设置cookie的key
                    value = str(refresh),
                    httponly = True, #
                    samesite = 'Lax', # 设置httponly
                    max_age = 864000 * 7, # 7天
                )
                return response
            return Response({
                'result': 'success',
                'access': str(refresh.access_token),
            })

        except:
            return Response({
                'result': '系统异常，请稍后重试'
            }, status= 401) # 这里一定要加401, 个人习惯用用于判断cookie过期