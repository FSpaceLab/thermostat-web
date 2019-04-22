from django.shortcuts import render
from django.views.generic import ListView
from .models import LogThermostat
from datetime import datetime, timedelta


class DataListView(ListView):
    context_object_name = "qset"
    model = LogThermostat
    template_name = 'ts/index.html'

    def get_queryset(self):
        start_date_text = self.request.GET.get("start_date")
        end_date_text = self.request.GET.get("end_date")

        if start_date_text and end_date_text:
            start_date = datetime.strptime(start_date_text, "%Y-%m-%d-%H-%M")
            end_date = datetime.strptime(end_date_text, "%Y-%m-%d-%H-%M")

        elif start_date_text and not end_date_text:
            start_date = datetime.strptime(start_date_text, "%Y-%m-%d-%H-%M")
            end_date = datetime.now()

        elif not start_date_text and end_date_text:
            end_date = datetime.strptime(end_date_text, "%Y-%m-%d-%H-%M")
            start_date = end_date - timedelta(hours=1)

        else:
            start_date = datetime.today() - timedelta(days=1)
            end_date = datetime.now()

        data = LogThermostat.objects.filter(time__range=(start_date, end_date))
        if len(data) >= 30:
            step = len(data) // 30
            buff = 0
            while buff <= len(data):
                if buff % step:
                    data.e
        return

