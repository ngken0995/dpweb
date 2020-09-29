from django.contrib.auth.models import AbstractUser
from django.db import models

sex = [
    ('f', 'female'),
    ('m', 'male')
]

exercise = [
    ('s', 'sedentary'),
    ('m', 'Moderately Active'),
    ('a', 'Active')
]


class User(AbstractUser):
    pass

class Personal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    activeLevel= models.CharField(choices=exercise, max_length=1, default='s')
    gender = models.CharField(choices=sex, max_length=1, default='f')

class Article(models.Model):
    name = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

class Happiness(models.Model):
    scale = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creater')
    timestamp = models.DateTimeField(auto_now_add=True)

class Calorie(models.Model):
    age = models.IntegerField()
    gender = models.CharField(choices=sex, max_length=1, default='f')
    sedentary = models.IntegerField()
    moderatelyActive = models.IntegerField()
    active = models.IntegerField()

class Favorite(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    calories = models.IntegerField()
    carbs = models.CharField(max_length=64)
    fat = models.CharField(max_length=64)
    food_id = models.IntegerField()
    image = models.URLField(blank=True, null=True)
    protein = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "calories": self.calories,
            "carbs": self.carbs,
            "fat": self.fat,
            "food_id": self.food_id,
            "image": self.image,
            "protein": self.protein,
            "title": self.title,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }



    

