from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main ,name = 'main' ),
    path('upload/<str:pk>', views.upload, name = 'upload'),
    path('calendar/', views.calendar, name='calendar'),
    path('ourTeam/', views.ourTeam, name='ourTeam'),
    path('news/',views.news, name='news'),

]