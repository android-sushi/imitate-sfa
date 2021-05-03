from django import forms
from .models import (
    Company, Person, Info, Note, Schedule,
    Product, StockControl, Weather
)
from django.utils import timezone
from django.utils.timezone import localtime


class DateInput(forms.DateInput):
    input_type = 'date'


class ScheduleModelForm(forms.ModelForm):
    """予定のフォーム"""
    company = forms.ModelChoiceField(
        label='会社名',
        queryset=Company.objects.all(),
        empty_label=None, )

    class Meta:
        model = Schedule
        fields = ('date', 'company', 'area', 'content', 'num_of_people')
        widgets = {'date': DateInput()}


class InfoModelForm(forms.ModelForm):
    """お知らせのフォーム"""
    name = forms.ModelChoiceField(
        label='名前',
        queryset=Person.objects.all(),
        empty_label=None,
    )

    class Meta:
        model = Info
        fields = ('content', 'date', 'name')
        widgets = {'date': DateInput()}


class NoteModelForm(forms.ModelForm):
    """メモのフォーム"""
    name = forms.ModelChoiceField(
        label='名前',
        queryset=Person.objects.all(),
        empty_label=None,
    )

    class Meta:
        model = Note
        fields = ('content', 'name')


class StockControlModelForm(forms.ModelForm):
    """持ち出し＆補充のフォーム"""
    company = forms.ModelChoiceField(
        label='会社名',
        queryset=Company.objects.all(),
        empty_label=None,
    )
    product = forms.ModelChoiceField(
        label='商品名',
        queryset=Product.objects.all(),
        empty_label=None,
    )
    date = forms.DateField(
        label='日付',
        initial=localtime(timezone.now())
    )

    class Meta:
        model = StockControl
        fields = ('date', 'company', 'product', 'count')
        widgets = {'date': DateInput()}
