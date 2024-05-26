from django.contrib import admin
from .models import UserInfo, Post, UploadedFile
from django.contrib.auth.admin import UserAdmin
# Register your models here.
#admin.site.register(UserInfo)
#admin.site.register(Post)

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ["id", "content", "created_datetime", "owner", "category_enum", "show","approved"]
    pass

@admin.register(UserInfo)
class UserInfoadmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "age", "phone_number", "bio", "failed_login_num", "is_supervisor", "pendaccess"]
    pass



@admin.register(UploadedFile)
class Failadmin(admin.ModelAdmin):
    list_display = ["id", "owner", "name", "file", "category_enum", "show", "approved", "scan_result", "created_datetime"]
    pass