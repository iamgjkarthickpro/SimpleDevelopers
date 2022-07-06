from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Videos(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    context = models.TextField(blank=True,null=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    def __str__(self):
        return self.title