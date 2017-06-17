from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

DEFAULT_EXAM_ID = 1

class Item(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    verbose_name = 'Предмет'
    verbose_name_plural = 'Предметы'
    def __unicode__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


