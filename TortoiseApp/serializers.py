from rest_framework import serializers
from .models import Plan, Promotion
from django.contrib.auth.models import User


class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ["planID", 'userID', 'promoID', "planName", "amountOptions", "startt_promotion_date", "tenureOptions", 'end_promotion_date', "benefitPercentage", "benefitType"]


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['start_promotion_date']
