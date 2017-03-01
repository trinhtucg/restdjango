from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)


def test_param(request, param_id):
    text = "Displaying article Number : %s" % param_id
    return HttpResponse(text)


def index(request):
    today = '20150101'
    return render(request, 'book/index.html', {'today': today})
