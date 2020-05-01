from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('referanslar/', views.referanslar, name='referanslar'),
    path('iletisim/', views.iletisim, name='iletisim'),
]