from django.contrib import admin
from django.urls import path
from work.V1.auth import Sign_in, Sign_up

urlpatterns = [
    
    path('linkedIn/sign-in/', Sign_in.as_view()),
    path('linkedIn/sign-up/api-v1/', Sign_up.as_view()),

]
