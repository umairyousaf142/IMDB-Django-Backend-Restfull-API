from django.db import models

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
    platform = models.ForeignKey(stramPlatform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title