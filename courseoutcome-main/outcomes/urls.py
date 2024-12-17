from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/insertco/',views.insertco, name='insertco'),
    path('view_co/',views.view_co,name='view_co'),
    path('deleteprofile/<str:course_name>/', views.deleteprofile, name='deleteprofile'),
    path('editprofile/<str:course_name>/', views.editprofile, name='editprofile'),
    path('updateco/<str:course_name>/', views.updateco, name='updateco'),
]