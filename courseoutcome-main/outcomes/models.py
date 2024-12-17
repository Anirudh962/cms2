from django.db import models

# Create your models here.
class course_outcomes(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    contact_hours = models.PositiveIntegerField()
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table="course_outcomes"

   