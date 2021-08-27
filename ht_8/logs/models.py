from django.db import models


class Logs(models.Model):

    CHOICES = (
        ('GT', 'GET'),
        ('PS', 'POST'),
        ('PT', 'PUT'),
        ('DL', 'DELETE'),
    )
    path = models.CharField(verbose_name='Путь', max_length=200)
    timestamp = models.TimeField(verbose_name='Дата-Время')
    method = models.CharField(verbose_name='Метод',
                              max_length=200, choices=CHOICES)
