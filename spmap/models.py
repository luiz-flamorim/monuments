# Create your models here.
from django.db import models

class Monument(models.Model):
    owner = models.ForeignKey('auth.User', related_name='monuments', on_delete=models.CASCADE)
    data = models.CharField(max_length=500, blank=True, null=True)
    data_more_info = models.CharField(max_length=500, blank=True, null=True)
    nome = models.CharField(max_length=500, blank=True, null=True)
    genero = models.CharField(max_length=500, blank=True, null=True)
    etinia = models.CharField(max_length=500, blank=True, null=True)
    endereco = models.CharField(max_length=500, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    tombado = models.CharField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    iphan = models.CharField(max_length=500, blank=True, null=True)
    fonte = models.CharField(max_length=500, blank=True, null=True)
    tipo = models.CharField(max_length=500, blank=True, null=True)
    material = models.CharField(max_length=500, blank=True, null=True)
    condeph = models.CharField(max_length=500, blank=True, null=True)
    conpres = models.CharField(max_length=500, blank=True, null=True)
    autor = models.CharField(max_length=500, blank=True, null=True)
    endereco_original = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome