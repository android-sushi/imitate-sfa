from django import forms
from .models import (
    Company, Person, Info, Note,
    Schedule, Product, StockControl,
)


class DateInput(forms.DateInput):
    input_type = 'date'


class ScheduleModelForm(forms.ModelForm):
    """予定のフォーム"""
    company = forms.ModelChoiceField(
        label='会社名',
        queryset=Company.objects.all(),
        empty_label=None,
    )

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


class ProductModelForm(forms.ModelForm):
    """在庫のフォーム"""
    class Meta:
        model = Product
        fields = ('name', 'date')
        widgets = {'date': DateInput()}


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

    class Meta:
        model = StockControl
        fields = ('date', 'company', 'product', 'count')
        widgets = {'date': DateInput()}


class PersonModelForm(forms.ModelForm):
    """人名のフォーム"""
    company = forms.ModelChoiceField(
        label='会社名',
        queryset=Company.objects.all(),
        empty_label=None,
    )

    class Meta:
        model = Person
        fields = ('name', 'company')


class CompanyModelForm(forms.ModelForm):
    """会社名のフォーム"""
    class Meta:
        model = Company
        fields = ('name',)
