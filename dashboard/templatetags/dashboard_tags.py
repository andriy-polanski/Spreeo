from django import template
from dashboard.menu import get_nodes

register = template.Library()

def dashboard_navigation(parser, token):
    return DashboardNavigationNode()

class DashboardNavigationNode(template.Node):

    def render(self, context):
        context['nav_items'] = get_nodes(context['user'])
        return ''

register.tag("dashboard_navigation", dashboard_navigation)


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css})

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)

def silence_without_field(fn):
    def wrapped(field, attr):
        if not field:
            return ""
        return fn(field, attr)
    return wrapped

def _process_field_attributes(field, attr, process):

    # split attribute name and value from 'attr:value' string
    params = attr.split(':', 1)
    attribute = params[0]
    value = params[1] if len(params) == 2 else ''

    # decorate field.as_widget method with updated attributes
    old_as_widget = field.as_widget

    def as_widget(self, widget=None, attrs=None, only_initial=False):
        attrs = attrs or {}
        process(widget or self.field.widget, attrs, attribute, value)
        return old_as_widget(widget, attrs, only_initial)

    bound_method = type(old_as_widget)
    try:
        field.as_widget = bound_method(as_widget, field, field.__class__)
    except TypeError:  # python 3
        field.as_widget = bound_method(as_widget, field)
    return field

@register.filter("attr")
@silence_without_field
def set_attr(field, attr):

    def process(widget, attrs, attribute, value):
        attrs[attribute] = value

    return _process_field_attributes(field, attr, process)