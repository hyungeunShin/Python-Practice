"""
URL configuration for Django_Mem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Django_Mem import views

urlpatterns = [
    path('', views.MemList),
    path('mem_list', views.MemList),
    path('mem_detail', views.MemDetail),
    path('mem_mod', views.MemMod),
    path('mem_mod_act', views.MemModAct),
    path('mem_add', views.MemAdd),
    path('mem_add_act', views.MemAddAct),
    path('mem_del_act', views.MemDelAct),
]
