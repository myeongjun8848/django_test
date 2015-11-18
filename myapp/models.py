from django.db import models

class post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    article = models.TextField()

    def __str__(self):
        return self.title
