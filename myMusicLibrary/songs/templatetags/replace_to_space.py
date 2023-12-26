from django import template


register = template.Library()


def rep(value, arg):
    line = value.replace("%20", " ")
    return line


register.filter("rep", rep)
