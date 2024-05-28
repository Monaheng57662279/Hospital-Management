from django.db import models

class MafetengDoctorModel(models.Model):
    salary = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = 'doctors'