from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('spe_maths/', views.spe_maths, name="spe_maths"),
    path('spe_nsi/', views.spe_nsi, name="spe_nsi"),
    path('spe_pc/', views.spe_pc, name="spe_pc"),
]    
