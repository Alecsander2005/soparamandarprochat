from django.db import models

# Create your models here.


class Exemplo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    editado = models.DateTimeField(auto_now=True)
    criado = models.DateTimeField(auto_now_add=True)

    # Define como o objeto será exibido no Django Admin.
    def __str__(self) -> str:
        return f"{self.id} - {self.nome}"
