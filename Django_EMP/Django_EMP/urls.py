"""
URL configuration for Django_EMP project.

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
from Django_EMP import views

urlpatterns = [
    path('', views.empList),
    path('emp_list', views.empList),
    path('emp_detail', views.empDetail),
    path('emp_mod', views.empMod),
    path('emp_mod_act', views.empModAct),
    path('emp_add', views.empAdd),
    path('emp_add_act', views.empAddAct),
    path('emp_del_act', views.empDelAct),
]
