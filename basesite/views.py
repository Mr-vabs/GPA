from django.shortcuts import render, HttpResponse, redirect
from .models import Comment
# Create your views here.


def index(request):
    # return HttpResponse('index')
    return render(request, 'index.html')


def academics(request):
    # return HttpResponse('index')
    return render(request, 'academics.html')

def coursempe(request):
    # return HttpResponse('index')
    return render(request, 'mpe.html')

def coursemae(request):
    # return HttpResponse('index')
    return render(request, 'mae.html')

def coursecse(request):
    # return HttpResponse('index')
    return render(request, 'cse.html')


def labs(request):
    # return HttpResponse('index')
    return render(request, 'labs.html')


def committee(request):
    # return HttpResponse('index')
    return render(request, 'committee.html')


def gallery(request):
    # return HttpResponse('index')
    return render(request, 'gallary.html')


def hostel(request):
    # return HttpResponse('index')
    return render(request, 'hostel.html')


def placements(request):
    # return HttpResponse('index')
    return render(request, 'placements.html')


def alumni(request):
    # return HttpResponse('index')
    return render(request, 'alumni.html')


def library(request):
    # return HttpResponse('index')
    return render(request, 'library.html')


def about(request):
    # return HttpResponse('index')
    return render(request, 'about.html')


def contact(request):
    # return HttpResponse('index')
    return render(request, 'contact.html')


def insert(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        com = Comment(name=name, email=email, comment=comment)
        com.save()
    else:
        com = Comment()
    return redirect('index')
