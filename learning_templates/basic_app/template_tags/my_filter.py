from django import template

register=template.Library()

# Using the Decorator
@register.filter(name='cut')
def cut(value,arg):

    """
    This Cuts out the all the value of "arg" form the string.

    """
    return value.replace(arg,'')

# Register the filer by passin the name of the filer and function name.
# Name will be use in the template to call it out.
# If Decorator is used no need to call out explictilty like below
# register.filter('cut',cut)
