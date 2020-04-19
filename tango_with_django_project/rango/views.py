from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
    # return HttpResponse("Rango says hey there partner! '<a href=\'/rango/about/\'>About</a>'")


def about(request):
    context_dict = {'boldmessage': 'test'}
    return render(request, 'rango/about.html', context=context_dict)
    # return HttpResponse("Rango says here is the about page. '<a href=\'/rango/\'>Index</a>'")

# '<a href=\'/rango/\'>Index</a>'
# <a href=/rango/>Index</a>

# <a href=\'/rango/about/\'>About</a>'
# <a href=/rango/about/>About</a>