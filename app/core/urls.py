from django.contrib import admin
from django.urls import path, include

from rest_framework import routers


from .views import MainBannerViewSet

core_router = routers.DefaultRouter()

core_router.register(r"main_banner", MainBannerViewSet, basename="category")