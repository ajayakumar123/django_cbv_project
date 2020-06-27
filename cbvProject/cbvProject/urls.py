"""cbvProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cbvApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello_view/$',views.HelloWorldView.as_view()),
    url(r'^$',views.StudentListView.as_view(),name='list_view'),
    url(r'^student_detail_view/(?P<pk>\d+)$',views.StudentDetailView.as_view(),name='detail_view'),
    url(r'^student_create_view/$',views.StudentCreateView.as_view(),name='create_view'),
    url(r'^student_update_view/(?P<pk>\d+)$',views.StudentUpdateView.as_view(),name='update_view'),
    url(r'^student_delete_view/(?P<pk>\d+)$',views.StudentDeleteView.as_view(),name='delete_view'),
]
