from enum import Enum
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from django.db import models

class City(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('Название'))

    class Meta:
        verbose_name = _('город')
        verbose_name_plural = _('города')

    def __str__(self):
        return self.name


class Street(models.Model):
    district = models.ForeignKey('District', related_name='districts', on_delete=models.CASCADE, verbose_name=_(u'Район'))
    name = models.CharField(max_length=60, verbose_name=_(u'Название'))

    class Meta:
        verbose_name = _(u'улица')
        verbose_name_plural = _(u'улицы')

    def __str__(self):
        return self.name


class District(models.Model):
    city = models.ForeignKey('City', related_name='cities', on_delete=models.CASCADE, verbose_name=_(u'Город'))
    name = models.CharField(max_length=60, verbose_name=_(u'Название'))

    class Meta:
        verbose_name = _(u'район')
        verbose_name_plural = _(u'районы')

    def __str__(self):
        return self.name


class FlatType(models.Model):
    name = models.CharField(max_length=60, verbose_name=_(u'Название'))

    class Meta:
        verbose_name = _(u'тип квартиры (количество комнат)')
        verbose_name_plural = _(u'типы квартир (количество комнат)')

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=60, verbose_name=_(u'Название'))

    class Meta:
        verbose_name = _(u'застройщик')
        verbose_name_plural = _(u'застройщики')

    def __str__(self):
        return self.name


class WallMaterial(models.Model):
    name = models.CharField(max_length=60, verbose_name=_(u'Название'))

    class Meta:
        verbose_name = _(u'материал стен')
        verbose_name_plural = _(u'материалы стен')

    def __str__(self):
        return self.name


class RealtyType(models.Model):
    name = models.CharField(max_length=60, verbose_name=_(u'Название'))

    class Meta:
        verbose_name = _(u'тип недвижимости')
        verbose_name_plural = _(u'типы недвижимости')

    def __str__(self):
        return self.name


class Image(models.Model):
    name=models.CharField(max_length=100, verbose_name=_(u'Название'))
    image = models.ImageField(upload_to='img',  max_length=None, verbose_name=_(u'Фотография'))

    class Meta:
        verbose_name = _(u'фотография')
        verbose_name_plural = _(u'фотографии')

    def __str__(self):
        return self.name


class ResidentialComplex(models.Model):
    name = models.CharField(max_length=100, verbose_name=_(u'Название'))

    class Meta:
        verbose_name = _(u'жилой комплекс')
        verbose_name_plural = _(u'жилые комплексы')

    def __str__(self):
        return self.name


class Flat(models.Model):

    class SubjectsOfLawChoices(models.TextChoices):
        Individual = 'Физическое лицо'
        Entity = 'Юридическое лицо'

    class QuarterChoices(models.TextChoices):
        FirstQuarter = 'I квартал'
        SecondQuarter = 'II квартал'
        ThirdQuarter = 'III квартал'
        FourthQuarter = 'IV квартал'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    subject_of_law = models.CharField(max_length=30,
                            choices=SubjectsOfLawChoices.choices,
                            default=SubjectsOfLawChoices.Entity,
                                      verbose_name=_(u'На кого оформлена'))
    description = models.TextField(blank=True, verbose_name=_(u'Описание'))
    wall_material = models.ForeignKey('WallMaterial', related_name='wall_materials', on_delete=models.CASCADE, verbose_name=_(u'Материал стен'))
    street = models.ForeignKey('Street', related_name='streets', on_delete=models.CASCADE, verbose_name=_('Улица'))
    house = models.CharField(max_length=30, verbose_name=_(u'Дом'))
    flat = models.IntegerField(blank=True, verbose_name=_(u'Квартира'))
    floor = models.IntegerField(blank=True, verbose_name=_(u'Этаж'))
    max_floor = models.IntegerField(blank=True, verbose_name=_(u'Максимальный этаж'))
    flat_type = models.ForeignKey('FlatType', related_name='flat_types', on_delete=models.CASCADE, verbose_name=_(u'Тип квартиры (количество комнат)'))
    developer = models.ForeignKey('Developer', related_name='developers', on_delete=models.CASCADE, verbose_name=_(u'Застройщик'))
    cost = models.IntegerField(verbose_name=_(u'Стоимость'))
    realty_type = models.ForeignKey('RealtyType', related_name='realty_types', on_delete=models.CASCADE, verbose_name=_(u'Тип недвижимости'))
    residential_complex = models.ForeignKey('ResidentialComplex', related_name='residential_complexes', on_delete=models.CASCADE, verbose_name=_(u'Жилой комплекс'))
    square = models.FloatField(verbose_name=_(u'Площадь'))
    year_of_completion = models.IntegerField(blank=True, verbose_name=_(u'Год (сдача)'))
    quarter = models.CharField(max_length=30,
                               choices=QuarterChoices.choices,
                               default=QuarterChoices.FirstQuarter, blank=True, verbose_name=_(u'Квартал (сдача)'))
    main_image = models.ImageField(upload_to='img',  max_length=None, blank=True, verbose_name=_(u'Постер'))
    layout = models.ImageField(upload_to='img',  max_length=None, blank=True, verbose_name=_(u'Планировка'))
    main_image_big = ImageSpecField(source='main_image',
                                      processors=[ResizeToFill(640, 480)],
                                      format='JPEG',
                                      options={'quality': 60})
    layout_big = ImageSpecField(source='layout',
                                      processors=[ResizeToFill(640, 480)],
                                      format='JPEG',
                                      options={'quality': 60})
    main_image_thumbnail = ImageSpecField(source='main_image',
                                      processors=[ResizeToFill(320, 240)],
                                      format='JPEG',
                                      options={'quality': 60})
    layout_thumbnail = ImageSpecField(source='layout',
                                      processors=[ResizeToFill(320, 240)],
                                      format='JPEG',
                                      options={'quality': 60})
    latitude = models.FloatField(blank=True, verbose_name=_(u'Долгота'))
    longitude = models.FloatField(blank=True, verbose_name=_(u'Широта'))

    class Meta:
        verbose_name = _(u'квартира')
        verbose_name_plural = _(u'квартиры')

    def __str__(self):
        return '%s %d кв.м. %s %s, кв.%d' % (self.developer.name, self.square, self.street.name, self.house, self.flat)


class Album(models.Model):
    name = models.CharField(max_length=100, verbose_name=_(u'Название'))
    flat = models.ForeignKey('Flat', on_delete=models.CASCADE, related_name='flats', verbose_name=_(u'Квартира'))
    image =  models.ForeignKey('Image', on_delete=models.CASCADE, related_name='images', verbose_name=_(u'Фотография'))

    class Meta:
        verbose_name = _(u'альбом')
        verbose_name_plural = _(u'альбомы')

    def __str__(self):
        return self.name