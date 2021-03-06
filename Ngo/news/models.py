# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

from Ngo.persons.models import NGO


class News(models.Model):
    Categories = (
        ('n', 'نامشخص'),
        ('i', 'مهم'),
        ('r', 'معمولی'),
        ('a', 'آرشیو')
    )
    CATEGORIES = (
        ('as', 'آسیا'),
        ('eu', 'اروپا'),
        ('am', 'آمریکا'),
        ('au', 'استرالیا و اقیانوسیه'),
        ('af', 'آفریقا'),
    )
    ngo = models.ForeignKey(NGO)
    title = models.CharField(max_length=50)
    continent = models.CharField(max_length=2, choices=CATEGORIES, null=True)
    status = models.CharField(default='n', max_length=1, choices=Categories)
    date = models.DateField(auto_now_add=True)  # have to change to jalali calender
    text = models.TextField()  # It is better for text to be as a text file because the valume of the text is alot
    description = models.CharField(max_length=100, null=True)
    title_image = models.FileField(upload_to=settings.MEDIA_ROOT, null=True)
    random_int = models.CharField(max_length=32)

    @classmethod
    def get_all_news(cls):
        return cls.objects.all()

    @classmethod
    def get_all_related_news(cls):
        ngo = NGO.objects.get(continent=None)
        return cls.objects.filter(ngo=ngo).order_by('-date')

    @classmethod
    def get_all_new_news(cls):
        return cls.objects.filter(status='n').order_by('-date')

    @classmethod
    def get_all_important_news(cls):
        return cls.objects.filter(status='i').order_by('-date')

    @classmethod
    def get_all_regular_news(cls):
        return cls.objects.filter(status='r').order_by('-date')


class Comment(models.Model):
    time = models.DateTimeField(auto_now_add=True)  # needs to be jalali datetime
    news = models.ForeignKey(News, related_name='comments')
    name = models.CharField(max_length=50)
    text = models.TextField()


class Answer(models.Model):
    time = models.DateTimeField(auto_now_add=True)  # jalali datetime
    comment = models.ForeignKey(Comment)
    name = models.CharField(max_length=20)
    text = models.TextField()


class Photo(models.Model):

    def __init__(self, *args, **kwargs):
        super(Photo, self).__init__(*args, **kwargs)

    pic = models.FileField(upload_to=settings.MEDIA_ROOT)
    unique_id = models.CharField(max_length=32)
    ngo = models.ForeignKey(NGO)
    text = models.CharField(max_length=100)
