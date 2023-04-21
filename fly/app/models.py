from django.db import models
from django.urls import reverse


class Module(models.Model):
    number = models.IntegerField(verbose_name='Порядковый номер')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('module', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'
        ordering = ['number',]
