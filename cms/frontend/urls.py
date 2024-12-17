from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/insertlp/',views.insertlp, name='insertlp'),
    path('lessonplan/',views.viewlessplan,name='viewlessplan'),
    path('deleteprofile/<str:id>/', views.deleteprofile, name='deleteprofile'),
    path('editprofile/<str:id>/', views.editprofile, name='editprofile'),
    path('updatelessp/<str:id>/', views.updatelessp, name='updatelessp'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    ]