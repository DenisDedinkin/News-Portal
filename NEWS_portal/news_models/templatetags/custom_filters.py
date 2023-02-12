from django import template

register = template.Library()

words = ['fuck']


@register.filter()
def censor(value):
    x = value.split(' ')
    value = []
    for i in x:
        if i in words:
            i = i[0] + '*' * (len(i) - 1)
        value.append(i)
    x = ' '.join(value)
    return f'{x}'
