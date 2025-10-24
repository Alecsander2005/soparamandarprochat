from django.db import models

# Create your models here.


class ExemploImagens(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='imagens/')
    editado = models.DateTimeField(auto_now=True)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.imagem.url}"
