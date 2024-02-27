from django.db import models
from django.contrib.auth.models import Group

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    upload = models.FileField(upload_to ='swaggerfiles/', null=True)
    allowed_group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

