from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views import View
from django.utils import timezone
from django.utils.timezone import localtime
from django.contrib import messages

from .models import (
    Company, Person, Info, Note,
    Schedule, Product, StockControl, Weather
)
from .forms import (
    PersonModelForm, ScheduleModelForm, InfoModelForm, NoteModelForm,
    StockControlModelForm, ProductModelForm,
)

from .views_modules import read_weather_from_jma


class IndexView(TemplateView):
    """トップページ"""
    template_name = 'schedule/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = localtime(timezone.now())
        context['date'] = date
        context['schedules'] = Schedule.objects.filter(date=date).order_by('company')
        # context['weathers'] = Weather.objects.filter(date__gte=date)[:3]
        context['forecasts_info'] = read_weather_from_jma.main()
        context['infos'] = Info.objects.order_by('-pk')[:5]
        context['notes'] = Note.objects.order_by('-pk')[:5]
        context['stockcontrols'] = StockControl.objects.order_by('-date')[:5]
        context['products'] = Product.objects.order_by('name')[:5]
        return context


class ScheduleListView(ListView):
    """予定一覧"""
    model = Schedule
    template_name = 'schedule/schedule_detail/schedule_list.html'
    paginate_by = 10
    date = localtime(timezone.now())

    def get_queryset(self):
        queryset = self.model.objects.order_by('company').order_by('-date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = self.date
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

    def get_queryset(self):
        return self.model.objects.order_by('-date')


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


class NoteListView(ListView):
    """メモの一覧"""
    model = Note
    template_name = 'schedule/note_detail/note_list.html'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.order_by('-pk')


class NoteCreateView(CreateView):
    """メモの新規登録"""
    model = Note
    form_class = NoteModelForm
    template_name = 'schedule/note_detail/note_create.html'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class NoteEditView(UpdateView):
    """メモの編集"""
    model = Note
    form_class = NoteModelForm
    template_name = 'schedule/note_detail/note_edit.html'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class NoteDeleteView(DeleteView):
    """メモの削除"""
    model = Note
    form_class = NoteModelForm
    template_name = 'schedule/note_detail/note_delete.html'
    success_url = reverse_lazy('note_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(self.request, '削除しました')
        return result


class StockControlListView(ListView):
    """持ち出し＆補充の一覧"""
    model = StockControl
    template_name = 'schedule/sc_detail/sc_list.html'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class StockControlCreateView(CreateView):
    """持ち出し＆補充の新規登録"""
    model = StockControl
    form_class = StockControlModelForm
    template_name = 'schedule/sc_detail/sc_create.html'
    success_url = reverse_lazy('sc_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class StockControlEditView(UpdateView):
    """持ち出し＆補充の編集"""
    model = StockControl
    form_class = StockControlModelForm
    template_name = 'schedule/sc_detail/sc_edit.html'
    success_url = reverse_lazy('sc_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class StockControlDeleteView(DeleteView):
    """持ち出し＆補充の削除"""
    model = StockControl
    form_class = StockControlModelForm
    template_name = 'schedule/sc_detail/sc_delete.html'
    success_url = reverse_lazy('sc_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(self.request, '削除しました')
        return result


class ProductListView(ListView):
    """商品の一覧"""
    model = Product
    template_name = 'schedule/product_detail/product_list.html'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.order_by('name')


class ProductCreateView(CreateView):
    """商品の新規登録"""
    model = Product
    form_class = ProductModelForm
    template_name = 'schedule/product_detail/product_create.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ProductEditView(UpdateView):
    """商品の編集"""
    model = Product
    form_class = ProductModelForm
    template_name = 'schedule/product_detail/product_edit.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ProductDeleteView(DeleteView):
    """商品の削除"""
    model = Product
    form_class = ProductModelForm
    template_name = 'schedule/product_detail/product_delete.html'
    success_url = reverse_lazy('product_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(self.request, '削除しました')
        return result


# ここから

class PersonListView(ListView):
    """人名の一覧"""
    model = Person
    template_name = 'schedule/person_detail/person_list.html'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.order_by('name')


class PersonCreateView(CreateView):
    """人名の新規登録"""
    model = Person
    form_class = PersonModelForm
    template_name = 'schedule/person_detail/person_create.html'
    success_url = reverse_lazy('person_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class PersonEditView(UpdateView):
    """人名の編集"""
    model = Person
    form_class = PersonModelForm
    template_name = 'schedule/person_detail/person_edit.html'
    success_url = reverse_lazy('person_list')

    def form_valid(self, form):
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class PersonDeleteView(DeleteView):
    """人名の削除"""
    model = Person
    form_class = PersonModelForm
    template_name = 'schedule/person_detail/person_delete.html'
    success_url = reverse_lazy('person_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(self.request, '削除しました')
        return result
