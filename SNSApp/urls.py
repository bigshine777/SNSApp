from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path("", include("main.urls")),  # "main" アプリの URL を読み込む
    path("admin/", admin.site.urls),  # Django 管理画面
]

