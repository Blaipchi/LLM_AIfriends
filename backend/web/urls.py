from django.urls import path, re_path

from web.views.create.character.create import CreateCharacterView
from web.views.create.character.get_single import GetSingleCharacterView
from web.views.create.character.remove import CharacterRemoveView
from web.views.create.character.update import UpdateCharacterView
from web.views.index import index
from web.views.user.account.get_user_info import GetUserInfoView
from web.views.user.account.login import LoginView
from web.views.user.account.logout import LogoutView
from web.views.user.account.refresh_token import RefreshTokenView
from web.views.user.account.register import RegisterView
from web.views.user.profile.update import UpdateProfileView

urlpatterns = [
    # 这里前面加api是为了区分前端与后端的路由，以防合并后冲突，导致无法打开前端的页面
    path('api/user/account/login/', LoginView.as_view()),
    path('api/user/account/register/', RegisterView.as_view()),
    path('api/user/account/refresh_token/', RefreshTokenView.as_view()),
    path('api/user/account/logout/', LogoutView.as_view()),
    path('api/user/account/get_user_info/', GetUserInfoView.as_view()),
    path('api/user/profile/update/', UpdateProfileView.as_view()),
    path('api/create/character/create/', CreateCharacterView.as_view()),
    path('api/create/character/update/', UpdateCharacterView.as_view()),
    path('api/create/character/remove/', CharacterRemoveView.as_view()),
    path('api/create/character/get_single/', GetSingleCharacterView.as_view()),
    path('', index),

    # 兜底路由,如果上方的路由都匹配不到，就会匹配这个路由
    re_path(r'^(?!media/|static/|assets/).*$', index)
]
