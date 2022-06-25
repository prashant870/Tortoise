from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

from django.db import models
from django.contrib.auth.models import User


class Promotion(models.Model):
    start_promotion_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return str(self.start_promotion_date)


class Plan(models.Model):
    amountOptionsChoice = {
        ("1000", "1000"),
        ("2000", "2000"),
        ("3000", "3000"),
        ("3500", "3500"),
        ("4000", "4000"),
        ("5000", "5000"),
        ("6000", "6000"),
        ("7500", "7500"),
        ("8000", "8000"),
        ("9000", "9000"),
        ("13000", "13000"),
        ("25000", "25500")
    }
    tenureOptionsChoice = {
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12")
    }
    benefitTypeChoice = {
        ("cashback", "cashback"),
        ("extraVoucher", "extraVoucher"),
    }
    planID = models.IntegerField(primary_key=True)
    userID = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, default=1)
    promoID = models.ForeignKey(Promotion, related_name='promo1', on_delete=models.CASCADE, default=10)
    planName = models.CharField(max_length=100)
    amountOptions = models.CharField(max_length=100, choices=amountOptionsChoice)
    startt_promotion_date = models.DateField(auto_now_add=False, editable=False)
    tenureOptions = models.CharField(max_length=100, choices=tenureOptionsChoice)
    benefitPercentage = models.IntegerField(editable=False)
    end_promotion_date = models.DateField(auto_now_add=False, editable=False)
    benefitType = models.CharField(max_length=100, choices=benefitTypeChoice)

    def save(self, *args, **kwargs):
        self.startt_promotion_date = self.promoID.start_promotion_date
        self.end_promotion_date = self.promoID.start_promotion_date + relativedelta(
            months=int(self.tenureOptions))

        print("promotion_start_date = ", self.startt_promotion_date)
        print("promotion_end_date = ", self.end_promotion_date)

        if self.startt_promotion_date <= date.today() <= self.end_promotion_date :
            self.benefitPercentage = 10
        else:
            self.benefitPercentage = 0
        super().save(*args, **kwargs)
