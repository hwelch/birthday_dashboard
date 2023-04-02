from django.db import models
from django.contrib.auth.models import User

class Relation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255, unique=True)
    birthday = models.DateField(unique=True)
    characteristics = models.TextField()
    gift_ideas = models.TextField()
    notes = models.TextField()
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)