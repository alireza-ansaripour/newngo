from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class NGO(models.Model):
    name = models.CharField(max_length=100)
    CATEGORIES = (
        ('as', 'آسیا'),
        ('er', 'اروپا'),
        ('am', 'آمریکا'),
        ('au', 'استرالیا و اقیانوسیه'),
        ('af', 'آفریقا'),
    )

    def __str__(self):
        return self.name

    continent = models.CharField(max_length=2, choices=CATEGORIES)
    Website = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=20)
    history = models.TextField()
    about = models.TextField()
    country = models.TextField()


class Expert(User):  # karshenas

    class Meta:
        verbose_name = 'کارشناس'
        verbose_name_plural = 'کارشناسان'

    ngo = models.ForeignKey(NGO)

    def __init__(self, *args, **kwargs):
        super(Expert, self).__init__(*args, **kwargs)
        self.is_staff = True

    def get_Ngo(self):
        return self.ngo


class Admin(User):

    def __init__(self, *args, **kwargs):
        super(Admin, self).__init__(*args, **kwargs)
        self.is_staff = True
        self.is_superuser = True
