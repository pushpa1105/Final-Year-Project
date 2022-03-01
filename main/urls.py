from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main ,name = 'main' ),
    path('upload/<str:pk>', views.upload, name = 'upload'),
    path('calendar/', views.calendar, name='calendar'),
    path('calendarMonsoon/', views.calendarMonsoon, name='calendarMonsoon'),
    path('calendarWinter/', views.calendarWinter, name='calendarWinter'),
    path('calendarSpring/', views.calendarSpring, name='calendarSpring'),
    path('calendarAutumn/', views.calendarAutumn, name='calendarAutumn'),
    path('ourTeam/', views.ourTeam, name='ourTeam'),
    path('news/',views.news, name='news'),

]