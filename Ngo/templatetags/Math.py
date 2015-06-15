import os
from django import template
register = template.Library()

@register.filter(name='sub')
def sub(f, s):
    return s-f

@register.filter(name='count')
def increment(g):
    return g+1