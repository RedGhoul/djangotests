from django import template

register = template.Library()

@register.filter()
def mma(value):
    value = value + value
    return value

