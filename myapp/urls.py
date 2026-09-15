from django.urls import path
from . import views

urlpatterns = [
    path('',views.splash, name='splash'),
    path('home/', views.home, name='home'),
    path('complaint/', views.complaint, name='complaint'),
    path('success/', views.success, name='success'),
    path('status/', views.status, name='status'),
]