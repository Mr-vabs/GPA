
from django.contrib import admin
from django.urls import path, include
from basesite import views

urlpatterns = [
    path('', views.index, name='index'),
    path('academics', views.academics, name='academics'),
    path('labs', views.labs, name='labs'),
    path('committee', views.committee, name='committee'),
    path('gallery', views.gallery, name='gallery'),
    path('hostel', views.hostel, name='hostel'),
    path('placements', views.placements, name='placements'),
    path('alumni', views.alumni, name='alumni'),
    path('library', views.library, name='library'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('coursempe', views.coursempe, name='coursempe'),
    path('coursemae', views.coursemae, name='coursemae'),
    path('coursecse', views.coursecse, name='coursecse'),
    path('insert', views.insert, name="insert")
]
