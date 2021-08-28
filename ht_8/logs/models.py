from django.db import models


class Logs(models.Model):
    path = models.CharField(verbose_name='Путь', max_length=200)
    timestamp = models.DateTimeField(verbose_name='Дата-Время')
    method = models.CharField(verbose_name='Метод',
                              max_length=200)

    def __str__(self):
        return self.path
