from django.db import models
from projects.models import Project

# Create your models here.
class Swagger(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    upload = models.FileField(upload_to ='swaggerfiles/')

    def __str__(self):
        return self.project.name