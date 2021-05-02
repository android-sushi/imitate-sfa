from django import forms
from .models import Company, Person, Info, Note, Schedule, Product, StockControl, Weather

import bootstrap_datepicker_plus as datetimepicker


class ScheduleNewForm(forms.ModelForm):
    """予定の新規登録フォーム"""
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
