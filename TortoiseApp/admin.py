from django.contrib import admin
from .models import Plan, Promotion


# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_display = ["planID", "planName", "amountOptions", "tenureOptions", "benefitPercentage", "benefitType"]


class PromotionAdmin(admin.ModelAdmin):
    list_display = ["start_promotion_date"]


admin.site.register(Plan, PlanAdmin)
admin.site.register(Promotion, PromotionAdmin)
