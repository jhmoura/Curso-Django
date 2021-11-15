from django.db import models

class Produto(models.Model):
    nome = models.CharField(("Nome"), max_length=50)
    preco = models.DecimalField(("Preço"), max_digits=12, decimal_places=2)
    estoque = models.IntegerField(("Quantidade em estoque"))
    
    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.nome