from django.db import models
from django.conf import settings
from django.conf import settings

class Relationship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ex_name = models.CharField(max_length=100)
    ex_email = models.EmailField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ex_name} ({self.user.username})"

class Review(models.Model):
    relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    communication = models.IntegerField()
    details = models.IntegerField()
    conflicts = models.IntegerField()
    comments = models.TextField(blank=True)
    anonymous = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.relationship.ex_name}"