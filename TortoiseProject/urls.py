from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from TortoiseApp import views

router = DefaultRouter()
router.register('plans', views.planViewSet, basename="plans_name")
router.register('promotion', views.promotionViewSet, basename="promotions")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]