from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class stramPlatform(models.Model):
    name = models.CharField(max_length = 50)
    about = models.CharField( max_length=100)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class watchList(models.Model):
    title = models.CharField( max_length=50)
    storyline = models.CharField(max_length=100)
    platform = models.ForeignKey(stramPlatform, on_delete=models.CASCADE, related_name='watchlists')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class review(models.Model):
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    desc = models.CharField(max_length=100)
    watchlist = models.ForeignKey(watchList, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rating: {self.rating:.1f}"