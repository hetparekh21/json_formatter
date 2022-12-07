from django.urls import path
from . import views

urlpatterns = [
    path('', views.json_main, name='json_main'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('sign_up_val/', views.sign_up_val, name='sign_up_val'),
    path('login_val/', views.login_val, name='login_val'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('save/', views.save, name='save'),
]