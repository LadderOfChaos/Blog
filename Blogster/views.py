from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Stefan',
        'title': 'First post',
        'content': 'Where it all started',
        'date_posted': 'October 11, 2020'
    },
    {
        'author': 'gg2',
        'title': 'second post',
        'content': 'Where it all started2',
        'date_posted': 'October 11, 2020'
    },
    {
        'author': 'Stefan3',
        'title': 'Third post',
        'content': 'Where it all started3',
        'date_posted': 'October 11, 2020'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'Blogster/home.html', context)


def about(request):
    return render(request,'Blogster/about.html', {
        'title': "About",
    })


def kurec(request):
    return HttpResponse('<h1>Kurec</h1>')
