from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from iou.views import ListUsers, UserViewSet, DebtViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import routers

routerAdd = DefaultRouter()
routerAdd.register(r'', UserViewSet, basename='user')

routerIou = DefaultRouter()
routerIou.register(r'', DebtViewSet, basename='debt')

urlpatterns = [
    path(r'users/', ListUsers.as_view()),
    path(r'add/', include(routerAdd.urls)),
    path(r'iou/', include(routerIou.urls)),
]
