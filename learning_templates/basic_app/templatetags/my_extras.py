from django import template

register = template.Library()

@register.filter(name='cut1')
def cut(value,args):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(args,'')

# register.filter('cut1',cut1)
