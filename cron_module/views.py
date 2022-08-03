from pytz import utc

from django.http import HttpResponse
from django.conf import settings 
from apscheduler.schedulers.background import BackgroundScheduler

from cron_module import Reminder, Notification
from temporary_representation.misc import (
    ExceptionState,
)


scheduler = BackgroundScheduler(
    jobstores=settings.jobstores, 
    executors=settings.executors, 
    job_defaults=settings.job_defaults, 
    timezone=utc,
)
scheduler.start()

reminder = Reminder(scheduler)
notification_func = Notification()


def interval_realization(request) -> HttpResponse:
    """
    """
    context = dict()

    func_type = request.GET.get("func_type", None)
    name_schedule = request.GET.get("name_schedule", None)
    minute = request.GET.get("minute", None)
    seconds = request.GET.get("seconds", None)
    hour = request.GET.get("hour", None)
    text = request.GET.get("text", "--")

    if func_type and name_schedule and minute and seconds and hour and text:
        context = ExceptionState.method_processing(
            text_notify=text,
            function=reminder.add_interval_mth,
            params={
                "func": notification_func.main_notification(func_type),
                "name_schedule": name_schedule,
                "minute": minute,
                "seconds": seconds,
                "hour": hour,
            }
        )
    return HttpResponse(context)


def date_realization(request) -> HttpResponse:
    """
    """
    context = dict()

    func_type = request.GET.get("func_type", None)
    name_schedule = request.GET.get("name_schedule", None)
    _datetime = request.GET.get("datetime", None)
    text = request.GET.get("text", "--")

    if func_type and name_schedule and _datetime and text:
        context = ExceptionState.method_processing(
            text_notify=text,
            function=reminder.add_date_mth,
            params={
                "func": notification_func.main_notification(func_type),
                "name_schedule": name_schedule,
                "_datetime": _datetime,
            }
        )
    return HttpResponse(context)


def cron_realization(request) -> HttpResponse:
    """
    """
    context = dict()

    func_type = request.GET.get("func_type", None)
    name_schedule = request.GET.get("name_schedule", None)
    day_of_week = request.GET.get("day_of_week", None)
    minute = request.GET.get("minute", None)
    seconds = request.GET.get("seconds", None)
    hour = request.GET.get("hour", None)
    text = request.GET.get("text", "--")

    if func_type and name_schedule and day_of_week and minute and seconds and hour and text:
        context = ExceptionState.method_processing(
            text_notify=text,
            function=reminder.add_cron_mth,
            params={
                "func": notification_func.main_notification(func_type),
                "name_schedule": name_schedule,
                "day_of_week": day_of_week,
                "minute": minute,
                "seconds": seconds,
                "hour": hour,
            }
        )

    return HttpResponse(context)


def delete_realization(request) -> HttpResponse:
    """
    
    """
    context = dict()
    name_schedule = request.GET.get("name_schedule", None)
    
    if name_schedule:
        context = ExceptionState.method_processing(
            function=reminder.remove_schedule_mth,
            params={
                "name_schedule": name_schedule,
            }
        )

    return HttpResponse(context)
