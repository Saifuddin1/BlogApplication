from django.urls import path
from . import views
urlpatterns = [
    path("register/",views.user_registration,name = "register"),
    path("login/",views.user_login,name = "login"),
    path("about/",views.about,name = "about"),
    path("edit/",views.edit_user_profile,name = "edit"),
    path("logout/",views.user_logout,name = "logout"),
    path("profile/",views.user_profile,name = "profile"),
    path("create_post/",views.create_post,name="create_post"),
    path("get_post/",views.get_post,name="get_post"),
    path("update_post/<int:id>",views.update_post,name="update_post"),
    path("delete_post/<int:id>",views.delete_post,name="delete_post"),
    path("post_detail/<int:id>",views.post_detail,name="post_detail"),
    path("contact",views.contact,name="contact"),

]
