from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse
from django.views import View
from django.utils import timezone

from .models import Company, Person, Info, Note, Schedule, Product, StockControl, Weather


class IndexView(View):
    def get(self, request, *args, **kwargs):
        today = timezone.now()
        schedules = Schedule.objects.filter(date=today)
        weathers = Weather.objects.filter(date__gte=today)[:3]
        infos = Info.objects.all()[:5]
        notes = Note.objects.all()[:5]
        stockcontrols = StockControl.objects.all()[:5]
        context = {
            'today': today,
            'schedules': schedules,
            'weathers': weathers,
            'infos': infos,
            'notes': notes,
            'stockcontrols': stockcontrols,
        }
        return render(request, 'schedule/index.html', context)


index = IndexView.as_view()
