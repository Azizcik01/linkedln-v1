"""
URL configuration for config project.

The `urlpatterns` list routes URLs to V1. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function V1
    1. Add an import:  from my_app import V1
    2. Add a URL to urlpatterns:  path('', V1.home, name='home')
Class-based V1
    1. Add an import:  from other_app.V1 import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('work.urls'))
]
