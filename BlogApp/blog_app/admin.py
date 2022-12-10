from django.contrib import admin
from .models import User,Post
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["user_name","user_email","user_password","user_phone"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["user_id","title","body","created_at"]



