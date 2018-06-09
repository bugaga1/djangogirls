
from django.shortcuts import render
from django.utils.datetime_safe import datetime


def post_list(request):
    return render(request, 'blog/post_list.html', {'data': datetime.now()})


