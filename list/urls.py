from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='home'),
    path('edit/<str:pk>/',views.editcontact, name='edit'),
    path('delete/<str:pk>/',views.deletecontact, name='delete'),
    path('register/',views.register, name='register'),
    path('login/',views.loginpage, name='login'),
    path('logout/',views.logoutpage, name='logout'),
]

