from django.contrib import admin
from django.urls import path
from work.views.auth import Sign_in, Sign_up

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('sign-in/api-v1/', Sign_in.as_view()),
    path('sign-up/api-v1/', Sign_up.as_view()),

]
