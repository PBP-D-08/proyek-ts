from django.db import models
from authentication.models import User
from homepage.models import Donation
from donation_app.models import UserDonation

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    # models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    
    money_donated = models.IntegerField(default=0)
    # history = models.ForeignKey(UserDonation, on_delete=models.CASCADE, related_name="user_profile")

# class Donated(models.Model):
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="donated")
#     donation = models.ForeignKey(
#         Donation, on_delete=models.CASCADE, related_name="donated"
#     )

