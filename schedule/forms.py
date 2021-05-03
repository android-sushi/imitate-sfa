from django import forms
from .models import Company, Person, Info, Note, Schedule, Product, StockControl, Weather

import bootstrap_datepicker_plus as datetimepicker


class ScheduleModelForm(forms.ModelForm):
    """予定のフォーム"""
    company = forms.ModelChoiceField(
        label='会社名',
        queryset=Company.objects.all(),
        empty_label=None,)

    class Meta:
        model = Schedule
        fields = ('date', 'company', 'area', 'content', 'num_of_people')
        widgets = {
            'date': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        }


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
        widgets = {
            'date': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        }


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
