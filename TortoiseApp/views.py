from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlanSerializers, PromotionSerializer
from .models import Plan, Promotion


class planViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers


class promotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
