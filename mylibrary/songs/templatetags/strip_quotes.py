from django import template

register = template.Library()


def stripq(value, arg):
    line = value.strip("\"")
    return line


register.filter("stripq", stripq)


