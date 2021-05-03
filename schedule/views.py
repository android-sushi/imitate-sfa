from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views import View
from django.utils import timezone
from django.contrib import messages

from .models import (
    Company, Person, Info, Note,
    Schedule, Product, StockControl, Weather
)
from .forms import (
    ScheduleModelForm, InfoModelForm,
)


class IndexView(TemplateView):
    """トップページ"""
    template_name = 'schedule/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now()
        context['today'] = today
        context['schedules'] = Schedule.objects.filter(date=today)
        context['weathers'] = Weather.objects.filter(date__gte=today)[:3]
        context['infos'] = Info.objects.all()[:5]
        context['notes'] = Note.objects.all()[:5]
        context['stockcontrols'] = StockControl.objects.all()[:5]
        return context


class ScheduleListView(ListView):
    """予定一覧"""
    model = Schedule
    template_name = 'schedule/schedule_detail/schedule_list.html'
    day = timezone.now()

    def get_queryset(self):
        return self.model.objects.filter(date=self.day)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['day'] = self.day
        return context


class ScheduleCreateView(CreateView):
    """予定の新規登録"""
    model = Schedule
    form_class = ScheduleModelForm
    template_name = 'schedule/schedule_detail/schedule_create.html'
    success_url = reverse_lazy('schedule_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ScheduleEditView(UpdateView):
    """予定の編集"""
    model = Schedule
    form_class = ScheduleModelForm
    template_name = 'schedule/schedule_detail/schedule_edit.html'
    success_url = reverse_lazy('schedule_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ScheduleDeleteView(DeleteView):
    """予定の削除"""
    model = Schedule
    form_class = ScheduleModelForm
    template_name = 'schedule/schedule_detail/schedule_delete.html'
    success_url = reverse_lazy('schedule_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(self.request, '削除しました')
        return result


class InfoListView(ListView):
    """お知らせの一覧"""
    model = Info
    template_name = 'schedule/info_detail/info_list.html'
    paginate_by = 10


class InfoCreateView(CreateView):
    """お知らせの新規登録"""
    form_class = InfoModelForm
    template_name = 'schedule/info_detail/info_create.html'
    success_url = reverse_lazy('info_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class InfoEditView(UpdateView):
    """お知らせの編集"""
    model = Info
    form_class = InfoModelForm
    template_name = 'schedule/info_detail/info_edit.html'
    success_url = reverse_lazy('info_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class InfoDeleteView(DeleteView):
    """お知らせの削除"""
    model = Info
    form_class = InfoModelForm
    template_name = 'schedule/info_detail/info_delete.html'
    success_url = reverse_lazy('info_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(self.request, '削除しました')
        return result






