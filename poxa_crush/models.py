from django.db import models

# Create your models here.
class Crush (models.Model):
    signo_opcoes = [
        ('ar', 'áries'),
        ('tr', 'touro'),
        ('gm', 'gêmeos'),
        ('cr', 'câncer'),
        ('le', 'leão'),
        ('vr', 'virgem'),
        ('lb', 'libra'),
        ('es', 'escorpião'),
        ('sg', 'sagitário'),
        ('cp', 'capricónio'),
        ('aq', 'aquário'),
        ('px', 'peixe')
    ]

    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    data = models.DateField()
    signo = models.CharField(max_length=2, choices=signo_opcoes)
    qualidade = models.CharField(max_length=100)
    defeito = models.CharField(max_length=100, default='não está comigo')
    reciproco = models.BooleanField(default=False)
    solteiro = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='',null=True)
    def __str__(self):
        return self.nome