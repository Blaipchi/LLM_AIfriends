# 更新用户的用户名和头像
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.user import UserProfile
from web.views.utils.photo import remove_old_photo


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    # 因为涉及到信息修改，所以这里用post方法
    def post(self, request):
        try:
            user = request.user
            # 这里的get是返回一个元素，0或多余1个就会报错
            user_profile = UserProfile.objects.get(user=user)
            username = request.data.get('username').strip()
            # 这里的简介的长度，是需要自己截断的，超过500就会取前500，不够就原封不动
            profile = request.data.get('profile').strip()[:500]
            photo = request.FILES.get('photo',None)

            # 这两个判断，其实前端也会判断，但为什么这里还要判断呢
            # 有一个原则是，后端不能相信前端传来的任何信息，主要是防止恶意用户的操作
            if not username:
                return Response({
                    'result': '用户名不能为空'
                })
            if not profile:
                return Response({
                    'result': '简介不能为空'
                })
            if username != user.username and User.objects.filter(username=username).exists():
                return Response({
                    'result': '用户名已存在'
                })
            if photo:
                remove_old_photo(user_profile.photo)
                user_profile.photo = photo
            # 更新数据
            user_profile.profile = profile
            user_profile.update_time = now()
            # 这里如果不save头像是不能保存的
            user_profile.save()
            user.username = username
            user.save()
            return Response({
                'result': 'success',
                'user_id': user.id,
                'username': username,
                'profile': user_profile.profile,
                # 这里一定要加一个url
                'photo': user_profile.photo.url,

            })
        except:
            return Response({
                'result': '系统异常，稍后重试'
            })

