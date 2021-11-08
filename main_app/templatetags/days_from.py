# Custom filter Reference: https://stackoverflow.com/questions/47622089/django-template-counting-days-from-now-to-specific-date

from datetime import datetime
from django import template


register = template.Library()

@register.filter
def days_from(post_date):
    delta = datetime.now().date() - datetime.date(post_date)
    return delta.days


# {{ post.created_at | days_from:"post_date" }} 