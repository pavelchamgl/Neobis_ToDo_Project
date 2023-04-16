from django.db import models


class DateTimeMixin:
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class ToDo(models.Model, DateTimeMixin):
    title = models.CharField('Задание', max_length=150)
    description = models.TextField('Описание')
    deadline = models.DateField('Дата завершения')
    is_complete = models.BooleanField('Выполнено', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
