from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True)
    sumario = RichTextField()
    texto = RichTextUploadingField()
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

