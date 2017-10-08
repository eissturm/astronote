from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
                    default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)


    def setLastUpdated(self):
        self.last_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.title
