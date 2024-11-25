from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.login_register_view, name='register'),
    path('login/', views.login_register_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload-image/', views.upload_image_view, name='upload_image'),
    path('home/', views.home_view, name='home'),
    path('contact/',views.contact_view,name='contact'),
      path('services/', views.services_view, name='services'),
    path('', views.home_view, name='home'),
path('dashboard/', views.dashboard, name='dashboard'),

]
