"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
#from django.urls import re_path as url, include
from django.contrib import admin

urlpatterns = [
    #url('admin/', admin.site.urls),
    
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    
    #url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]   
