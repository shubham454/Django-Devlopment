from django import template
register=template.Library()
#
# def first_two_upper(value):
#     """this is my filter"""
#     result = value[:2].upper()
#     return result
#
# register.filter('f2upper',first_two_upper)

@register.filter(name='f2upper')
def first_two_upper(value):
    result = value[:2].upper()
    return result+value[2:]
