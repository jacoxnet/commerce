from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    # Categories of AuctionItems
    # Known categories now are 
    #   Household
    #   Electronics
    #   Computers
    #   Tools
    #   Autos
    type = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.type

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bidAmount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

class AuctionItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    listedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    bids = models.ManyToManyField(Bid, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)
    pic = models.URLField(max_length = 200)
    
    def __str__(self):
        s = str(self.category) + " " + self.name
        if self.completed:
            s += " (completed)"
        else:
            s += " (active)"
        return s
