from django.contrib import admin
from django.urls import path
from work.V1.auth import Sign_in, Sign_up
from work.V1.core import ProfileView, PostView, ExperienceView

urlpatterns = [

    path('linkedIn/sign-in/', Sign_in.as_view()),
    path('linkedIn/sign-up/api-v1/', Sign_up.as_view()),
    # profile
    path('linkedIn/profile/', ProfileView.as_view()),
    path('linkedIn/profile/<int:pk>', ProfileView.as_view()),
    # post
    path('linkedIn/post/', PostView.as_view()),
    path('linkedIn/post/<int:pk>', PostView.as_view()),
    # Experience
    path('linkedIn/exp/', ExperienceView.as_view()),
    path('linkedIn/exp/<int:pk>', ExperienceView.as_view()),

]
