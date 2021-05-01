from django.utils import timezone
from django.db import models


class Company(models.Model):
    """会社名モデル"""
    class Meta:
        db_table = 'company'

    name = models.CharField(verbose_name='会社名', max_length=255)

    def __str__(self):
        return self.name


class Person(models.Model):
    """人名モデル"""
    class Meta:
        db_table = 'person'

    name = models.CharField(verbose_name='名前', max_length=255)
    company = models.ForeignKey(Company, verbose_name='会社名',
                                on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Info(models.Model):
    class Meta:
        db_table = 'info'

    date = models.DateField(verbose_name='日付', default=timezone.now)
    """お知らせモデル"""
    content = models.TextField(verbose_name='内容')
    name = models.ForeignKey(Person, verbose_name='名前',
                             on_delete=models.PROTECT)

    def __str__(self):
        return str(self.date)


class Note(models.Model):
    """メモモデル"""
    class Meta:
        db_table = 'note'

    content = models.TextField(verbose_name='メモ')
    name = models.ForeignKey(Person, verbose_name='名前',
                             on_delete=models.PROTECT)

    def __str__(self):
        return self.content


class Schedule(models.Model):
    """予定モデル"""
    class Meta:
        db_table = 'schedule'

    date = models.DateField(verbose_name='日付', default=timezone.now)
    company = models.ForeignKey(Company, verbose_name='会社名',
                                on_delete=models.PROTECT)
    area = models.CharField(verbose_name='場所', max_length=255)
    content = models.TextField(verbose_name='内容')
    num_of_people = models.IntegerField(verbose_name='人数')

    def __str__(self):
        return str(self.date)


class Product(models.Model):
    """商品モデル"""
    class Meta:
        db_table = 'product'

    name = models.CharField(verbose_name='商品名', max_length=255)
    stock = models.IntegerField(verbose_name='個数')

    def __str__(self):
        return self.name


class StockControl(models.Model):
    """持ち出し＆補充モデル"""
    class Meta:
        db_table = 'stock_control'

    date = models.DateField(verbose_name='日付', default=timezone.now)
    company = models.ForeignKey(Company, verbose_name='会社名',
                                on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name='商品名',
                                on_delete=models.PROTECT)
    count = models.IntegerField(verbose_name='増減')

    def __str__(self):
        return str(self.date)


class Weather(models.Model):
    """天気モデル"""
    class Meta:
        db_table = 'weather'

    date = models.DateField(verbose_name='日付', default=timezone.now)
    weather = models.CharField(verbose_name='天気', max_length=255)
    percent = models.IntegerField(verbose_name='降水確率')

    def __str__(self):
        return str(self.date)
