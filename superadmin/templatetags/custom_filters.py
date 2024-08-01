from django import template
import os

register = template.Library()


@register.filter(name='filename')
def filename(value):
    """Extracts the file name from the file path"""
    return os.path.basename(value)


@register.filter
def filename(value):
    return value.split('/')[-1]

@register.filter(name='add_class')
def add_class(field, css_class):
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={"class": css_class})
    elif isinstance(field, str):
        return field  # Return the field as is if it's already a string
    else:
        return field  # Handle other types gracefully (optional) 

@register.filter
def filename(value):
    return os.path.basename(value)

@register.filter
def only_digits(value):
    if value is None:
        return ''
    return ''.join(filter(str.isdigit, value))

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})


@register.filter
def has_key(dictionary, key):
    return key in dictionary

@register.filter
def month_name(month_number):
    months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    try:
        return months[month_number - 1]
    except IndexError:
        return ''