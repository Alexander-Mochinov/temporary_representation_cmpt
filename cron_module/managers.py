from datetime import datetime
from django.db import models


class ScheduleManager(models.Manager):
    
    def get_datetime(self) -> datetime:
        pass


class NotificationManager(models.Manager):
    
    @staticmethod
    def get_all_notify() -> 'QuerySet':
        pass

    @staticmethod
    def get_rang_notify()-> 'QuerySet':
        pass
