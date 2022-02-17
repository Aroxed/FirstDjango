from auth_user.models import User
from django.contrib import admin


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
