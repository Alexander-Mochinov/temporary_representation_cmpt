from django.urls import path
from .views import (
    interval_realization, 
    date_realization, 
    cron_realization, 
    delete_realization,
)

urlpatterns = [
    path("interval-realization/", interval_realization, name="interval_realization",),
    path("date-realization/", date_realization, name="date_realization",),
    path("cron-realization/", cron_realization, name="cron_realization",),
    path("delete-realization/", delete_realization, name="delete_realization",),

]
