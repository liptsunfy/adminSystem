"""adminSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url

from CanlinkSystem import views
from django.urls import path

# https://www.cnblogs.com/Forever77/p/10129294.html
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^login/', views.login),

    path('CRHTrain', views.CRHTrain, name='CRHTrain'),  # 机车百科
    path('CRHmaps',views.maplist, name='CRHmaps'),  # 高铁地图

    ]
