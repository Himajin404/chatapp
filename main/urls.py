from django.urls import path

from .import views

# ↓今回名前空間は設定してないねん〜、、ここコメントアウトしたらできるはず！
# app_name = "chat_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    #path("login/", views.login, name="login"),
    path("login/", views.LoginView.as_view(), name="login"),  # 第 2 引数を変更。元々あるコードを書き換えてください。
    path("friends/", views.friends, name="friends"),  # 追加
    path("talk_room/<user_id>", views.talk_room, name="talk_room"),
    path("settings/", views.settings, name="settings"),
    path("username_change/", views.username_change, name="username_change"),
    path("username_change_done/", views.username_change_done, name="username_change_done"),
    path("email_change/", views.email_change, name="email_change"),
    path("email_change_done/", views.email_change_done, name="email_change_done"),
    path(
        "password_change/",
        views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change_done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),  # 追加
]

#from django.shortcuts import render
#def index(request):
    #return render(request, "main/index.html")
#def signup(request):
    #return render(request, "main/signup.html")
#def login(request):
    #return render(request, "main/login.html")