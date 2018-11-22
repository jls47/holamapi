"""holamapi URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api.resources import ProgramRequestResource
from api import views
from api.views import *

programrequest_resource = ProgramRequestResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_requests, name='view requests'),
    path('api/view/', include(programrequest_resource.urls)),
    path('api/<int:id>', id_view, name='status'),
    path('api/edit/<int:id>', edit_request, name='edit'),
    path('api/', get_request_form, name='write')
]
