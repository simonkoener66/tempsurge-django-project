from django import template

register = template.Library()

@register.filter
def startswith(value, arg):
    """
    Usage:
    {% if value|startswith:"arg" %}...{% endif %}
    """

    return value.startswith(arg)