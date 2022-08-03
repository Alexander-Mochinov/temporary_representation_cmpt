from typing import Any
from datetime import datetime


class Reminder:
    """
    Класс для работы с заданием интервала с типами (interval, date, cron,)
        и удалением его их списка
    """

    def __init__(self, scheduler, *args, **kwargs) -> None:
        self.scheduler = scheduler


    def add_interval_mth(
        self, 
        func, 
        name_schedule: str,
        minute: int = 0,
        seconds: int = 0,
        hour: int = 0,
    ) -> dict:

        """
        Добавление интервального протокола выполнения 

        mark: Метод выполняется интервалом с установленным периодом
        """

        context = dict()
        self.scheduler.add_job(
            func, 
            'interval', 
            id=name_schedule,
            minute=minute,
            seconds=seconds,
            hour=hour,
        )
        return context

    def add_date_mth(
        self, 
        func, 
        name_schedule: str, 
        _datetime: datetime
    ) -> dict:

        """
        Добавление метода выполнения для установленной даты

        mark: Выполняется один раз в установленную дату
        """

        context = dict()
        self.scheduler.add_job(
            func,
            'date',
            id=name_schedule,
            run_date=_datetime,
        )
        return context

    def add_cron_mth(
        self, 
        func, 
        name_schedule: str, 
        day_of_week,
        minute: int = 0, 
        seconds: int = 0,
        hour: int = 0,
    ) -> dict:
        """
        Добавление метода в стек расписаний для работы с cron протоколом

        mark: Параметр day_of_week может иметь как строку с диапозонам даты недели так и само число
        """

        context = dict()
        self.scheduler.add_job(
            func, 
            'cron', 
            id=name_schedule,
            day_of_week=day_of_week, 
            minute=minute,
            seconds=seconds,
            hour=hour, 
        )
        return context

    def remove_schedule_mth(self, name_schedule: str) -> dict:
        """
        Удаление метода из стека расписаний
        """

        context = dict()
        self.scheduler.remove_job(
            name_schedule
        )

        return context
