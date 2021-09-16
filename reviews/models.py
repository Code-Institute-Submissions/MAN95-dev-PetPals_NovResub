from django.db import models

from profiles.models import UserProfile
from items.models import Item


class Review(models.Model):
    """
    A review model that allows users to perform
    CRUD operations on item reviews
    """

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
