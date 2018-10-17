"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'admin/', admin.site.urls),
# 添加   使用include来将子应用users里的  全部路由  包含进工程路由中  r'^users/' 决定了users子应用的所有路由都已/users/开头
#     url(r'^users/', include('users.urls'), namespace='users'),
    url(r'^users/', include('users.urls', namespace='user')),

    # 这里的users后面的/ 要加上, 字符串的拼接
]
