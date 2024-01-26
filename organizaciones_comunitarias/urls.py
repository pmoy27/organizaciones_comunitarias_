from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
        path('', views.inicio, name="index"),
    path('login/', views.login, name="login"),
]
