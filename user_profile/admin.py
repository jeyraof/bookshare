from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from user_profile.models import Profile


admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False


@admin.register(User)
class UserAdminExtend(UserAdmin):
    inlines = [ProfileInline]
