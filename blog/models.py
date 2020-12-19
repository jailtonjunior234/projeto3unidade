from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    Time = models.CharField(max_length=300)
    Historia = RichTextField()
    Jogadores = RichTextUploadingField()
    Tecnico = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.Titulo
    