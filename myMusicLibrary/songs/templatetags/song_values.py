from django import template


register = template.Library()


def spliting(value, arg):
    line = value.split("\\")
    return line[:-4:-1]


register.filter("spliting", spliting)

