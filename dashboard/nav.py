import re
from django.core.urlresolvers import reverse, resolve, NoReverseMatch
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404

class Node(object):
    """
    A node in the dashboard navigation menu
    """

    def __init__(self, label, url_name=None, url_args=None, url_kwargs=None,
                 access_fn=None, icon=None):
        self.label = label
        self.icon = icon
        self.url_name = url_name
        self.url_args = url_args
        self.url_kwargs = url_kwargs
        self.access_fn = access_fn
        self.children = []

    @property
    def is_heading(self):
        return self.url_name is None

    @property
    def url(self):
        return reverse(self.url_name, args=self.url_args,
                       kwargs=self.url_kwargs)

    def add_child(self, node):
        self.children.append(node)

    def is_visible(self, user):
        return self.access_fn is None or self.access_fn(
            user, self.url_name, self.url_args, self.url_kwargs)

    def filter(self, user):
        if not self.is_visible(user):
            return None
        node = Node(
            label=self.label, url_name=self.url_name, url_args=self.url_args,
            url_kwargs=self.url_kwargs, access_fn=self.access_fn,
            icon=self.icon
        )
        for child in self.children:
            if child.is_visible(user):
                node.add_child(child)
        return node

    def has_children(self):
        return len(self.children) > 0


def default_access_fn(user, url_name, url_args=None, url_kwargs=None):
    """
    Given a url_name and a user, this function tries to assess whether the
    user has the right to access the URL.
    """

    if url_name is None:  # it's a heading
        return True
    # get view module string
    try:
        url = reverse(url_name, args=url_args, kwargs=url_kwargs)
        view_module = resolve(url).func.__module__
    except (NoReverseMatch, Http404):
        # if there's no match, no need to display it
        return False

    return True
