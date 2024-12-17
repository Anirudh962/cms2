
from django.db import models

class lessonplan(models.Model):
    lsid = models.CharField(max_length=20)
    descp = models.CharField(max_length=255)
    cosn = models.CharField(max_length=20)

    class Meta:
        db_table = 'lessonplan'