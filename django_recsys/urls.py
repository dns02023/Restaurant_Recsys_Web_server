"""django_recsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from recapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #관리자 기능을 사용하기 위한 url
    path('', views.index, name='index'),
    #홈으로 이동하기 위한 url
    #현재 사이트의 홈은 recapp의 place_list로 연결되게 설정되어 있으므로, recapp.view의 index가 실행되게 설정
    path('recapp/', include('recapp.urls')),
    #recapp 기능을 사용하기 위한 url => include로 recapp 내부에서 관리
    path('signapp/', include('signapp.urls')),
    #signapp 기능을 사용하기 위한 url => include로 signapp 내부에서 관리
]
