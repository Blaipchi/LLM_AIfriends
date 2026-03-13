from http.client import responses

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    # 强制必须登录才能访问
    permission_classes = [IsAuthenticated]
    def post(self, request):
        response = Response({
            'result': 'success'
        })
        # 推出登录就是将cookie中refresh_token删掉即可
        response.delete_cookie('refresh_token')
        return response