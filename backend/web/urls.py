from django.urls import path
from web.views.index import index
from web.views.user.account.login import LoginView
from web.views.user.account.logout import LogoutView
from web.views.user.account.refresh_token import RefreshTokenView
from web.views.user.account.register import RegisterView

urlpatterns = [
    # 这里前面加api是为了区分前端与后端的路由，以防合并后冲突，导致无法打开前端的页面
    path('api/user/account/login/', LoginView.as_view()),
    path('api/user/account/register/', RegisterView.as_view()),
    path('api/user/account/refresh_token/', RefreshTokenView.as_view()),
    path('api/user/account/logout/', LogoutView.as_view()),


    path('', index),
]
