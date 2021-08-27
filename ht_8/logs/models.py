from django.db import models


class Logs(models.Model):

    CHOICES = (
        ('GT', 'GET'),
        ('PS', 'POST'),
        ('PT', 'PUT'),
        ('DL', 'DELETE'),
    )
    path = models.CharField(verbose_name='Путь')
    timestamp = models.TimeField(label='Дата-Время')
    method = models.CharField(label='Метод',
                              max_length=200, choices=CHOICES)
