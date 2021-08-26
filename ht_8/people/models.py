from django.db import models


class Person(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(verbose_name='Эл. почта')

    def __str__(self):
        return f'ИМЯ: {self.first_name} ФАМИЛИЯ: {self.last_name} ' \
               f'ПОЧТА: {self.email}'
