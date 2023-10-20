from django.db import models


class urlShortener(models.Model):
    original_url = models.CharField(max_length=200)
    shortened_url = models.CharField(max_length=10)

    def __str__(self):
        return self.shortened_url