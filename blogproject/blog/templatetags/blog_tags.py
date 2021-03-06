from django import template
from ..models import Post, Category, Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num=4):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')
    # return Post.objects.annotate(num_posts_month=Count('month')).filter(num_posts_month__gt=0)

@register.simple_tag
def get_categories():
    # return Category.objects.all()
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    return  Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)