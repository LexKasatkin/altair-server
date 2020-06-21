from enum import Enum
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from django.db import models

class City(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Street(models.Model):
    district = models.ForeignKey('District', related_name='districts', on_delete=models.CASCADE)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class District(models.Model):
    city = models.ForeignKey('City', related_name='cities', on_delete=models.CASCADE)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class FlatType(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class WallMaterial(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class RealtyType(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Image(models.Model):
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='img',  max_length=None)

    def __str__(self):
        return self.name


class ResidentialComplex(models.Model):
    name = models.CharField(max_length=100)

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
                            default=SubjectsOfLawChoices.Entity)
    description = models.TextField(blank=True)
    wall_material = models.ForeignKey('WallMaterial', related_name='wall_materials', on_delete=models.CASCADE)
    street = models.ForeignKey('Street', related_name='streets', on_delete=models.CASCADE)
    house = models.CharField(max_length=30)
    flat = models.IntegerField(blank=True)
    floor = models.IntegerField(blank=True)
    max_floor = models.IntegerField(blank=True)
    flat_type = models.ForeignKey('FlatType', related_name='flat_types', on_delete=models.CASCADE)
    developer = models.ForeignKey('Developer', related_name='developers', on_delete=models.CASCADE)
    cost = models.IntegerField()
    realty_type = models.ForeignKey('RealtyType', related_name='realty_types', on_delete=models.CASCADE)
    residential_complex = models.ForeignKey('ResidentialComplex', related_name='residential_complexes', on_delete=models.CASCADE)
    square = models.FloatField()
    year_of_completion = models.IntegerField(blank=True)
    quarter = models.CharField(max_length=30,
                               choices=QuarterChoices.choices,
                               default=QuarterChoices.FirstQuarter, blank=True)
    main_image = models.ImageField(upload_to='img',  max_length=None, blank=True)
    layout = models.ImageField(upload_to='img',  max_length=None, blank=True)
    main_image_big = ImageSpecField(source='main_image',
                                      processors=[ResizeToFill(640, 480)],
                                      format='JPEG',
                                      options={'quality': 60})
    layout_big = ImageSpecField(source='layout',
                                      processors=[ResizeToFill(640, 480)],
                                      format='JPEG',
                                      options={'quality': 60})
    main_image_thumbnail = ImageSpecField(source='main_image',
                                      processors=[ResizeToFill(300, 200)],
                                      format='JPEG',
                                      options={'quality': 60})
    layout_thumbnail = ImageSpecField(source='main_image',
                                      processors=[ResizeToFill(300, 200)],
                                      format='JPEG',
                                      options={'quality': 60})
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)

    def __str__(self):
        return '%s %d %s' % (self.developer.name, self.square, self.street.name)


class Album(models.Model):
    name = models.CharField(max_length=100)
    flat = models.ForeignKey('Flat', on_delete=models.CASCADE, related_name='flats')
    image =  models.ForeignKey('Image', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.name