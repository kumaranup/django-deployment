from django.urls import path
from userauth import views

app_name = 'userauth'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
