from typing import Any
from django.db import models
from .managers import (
    ScheduleManager,
    NotificationManager,
)


class BaseModel(models.Model):
    """
    Базовая модель
    """

    date_created = models.DateTimeField(
        verbose_name="Дата создания записи",
        auto_now_add=True, 
    )

    date_modified = models.DateTimeField(
        verbose_name="Дата изменения записи",
        auto_now=True,
    )

    class Meta:
        abstract=True


class Schedule(BaseModel):
    """
    Одна установка для работы с уведомлениями
    """

    class TypeSchedule(models.TextChoices):
        cron = 'cron', 'Крон метод'
        date = 'date', 'Метод даты'
        interval = 'interval', 'Интервальный метод'

    name_schedule = models.CharField(
        verbose_name="Название расписания",
        max_length=999,
        unique=True,
        null=False,
        blank=True,
    )

    type_schedule_mth = models.CharField(
        verbose_name="Тип расписания",
        max_length=8,
        null=False,
        blank=True,
        choices=TypeSchedule.choices,
    )

    date_setting = models.DateTimeField(
        verbose_name="Установленная даты",
    )

    objects: models.Manager[Any] = ScheduleManager()

    class Meta:
        db_table = "schedule"
        verbose_name = "Сводка расписания"
        verbose_name_plural = "Сводка расписаний"


class Notification(BaseModel):
    """
    Модель уведомления
    """

    class FuncType(models.TextChoices):
        """Тип уведомления"""

        _global = "_global", "Глобальный метод уведомления"
        _local = "_local", "Локальный метод уведомления"

    text = models.TextField(
        verbose_name="Текст уведомления",
        null=True,
    )

    schedule = models.ForeignKey(
        Schedule,
        verbose_name="Расписание",
        on_delete=models.CASCADE,
        related_name="notify",
    )

    objects: models.Manager[Any] = NotificationManager()

    class Meta:
        db_table = "notification"
        verbose_name = "Данные для уведомления"
        verbose_name_plural = "Данные для уведомления"


# Дописать модели
# Протестировать вью 
# Сделать логирование
# Сделать удаление процесса который очень много выполняется 
# Сделать клиент api Для взаимодействия с напоминалкой