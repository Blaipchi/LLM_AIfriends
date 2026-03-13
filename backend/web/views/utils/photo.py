# os工具包用来管理文件
import os

from django.conf import settings


# 该函数的作用是，用户在上传完新头像后，要将旧的头像删掉，省数据库资源
# 但是如果是默认头像，就不会删除
def remove_old_photo(photo):
    if photo and photo.name != 'user/photos/default.png':
        old_path = settings.MEDIA_ROOT / photo.name
        if os.path.exists(old_path):
            os.remove(old_path)