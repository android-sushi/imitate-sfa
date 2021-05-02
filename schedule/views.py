from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.views import View
from django.utils import timezone
from django.contrib import messages

from .models import Company, Person, Info, Note, Schedule, Product, StockControl, Weather
from .forms import ScheduleNewForm


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


class ScheduleDetailView(View):
    def get(self, request, *args, **kwargs):
        day = timezone.now()
        schedules = Schedule.objects.filter(date=day)
        context = {
            'day': day,
            'schedules': schedules,
        }
        return render(request, 'schedule/schedule_detail/detail.html', context)


schedule_detail = ScheduleDetailView.as_view()


class ScheduleSubmitView(View):
    def get(self, request, *args, **kwargs):
        form = ScheduleNewForm()
        context = {
            'form': form,
            'purpose': '新規登録',
        }
        return render(request, 'schedule/schedule_detail/submit.html', context)

    def post(self, request, *args, **kwargs):
        obj = Schedule()
        form = ScheduleNewForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'データの保存に成功しました')
            return redirect('schedule_detail')
        else:
            context = {
                'form': form,
            }
            print(form)
            return render(request, 'schedule/schedule_detail/submit.html', context)


schedule_submit = ScheduleSubmitView.as_view()

