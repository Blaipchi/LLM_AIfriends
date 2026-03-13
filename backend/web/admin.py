from django.contrib import admin
# Register your models here.
from web.models.user import UserProfile
from web.models.character import Character

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # 这里的作用主要是，避免打开页面的时候直接卡死的问题
    raw_id_fields = ('user',) # 逗号千万不能删！！

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)