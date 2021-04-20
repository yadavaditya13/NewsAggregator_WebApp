from django.db import models


# Create your models here.
class Headline(models.Model):

    title = models.CharField(max_length=200, primary_key=True)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title