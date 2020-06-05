from enum import Enum

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Flat(models.Model):
    name = models.CharField(max_length=60)
    full_name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class SubjectOfLaw(models.Model):
    class SubjectsOfLawChoices(models.TextChoices):
        Individual = 'Физическое лицо'
        Entity = 'Юридическое лицо'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    name = models.CharField(max_length=30,
                            choices=SubjectsOfLawChoices.choices,
                            default=SubjectsOfLawChoices.Entity)

    def __str__(self):
        return self.name


class WallMaterial(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Record(models.Model):
    description = models.TextField()
    wall_material = models.ForeignKey('WallMaterial', related_name='wall_materials', on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name='cities', on_delete=models.CASCADE)
    district = models.ForeignKey('District', related_name='districts', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', related_name='images', on_delete=models.CASCADE)
    flat = models.ForeignKey('Flat', related_name='flats', on_delete=models.CASCADE)
    developer = models.ForeignKey('Developer', related_name='developers', on_delete=models.CASCADE)
    subject_of_law = models.ForeignKey('SubjectOfLaw', related_name='subjects_of_law', on_delete=models.CASCADE)
    cost = models.IntegerField()
    square = models.FloatField()
    deadline = models.TextField()

    def __str__(self):
        return '${self.district.name} ${self.city.name}'
