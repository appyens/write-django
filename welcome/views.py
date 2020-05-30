from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
# Create your views here.


def hello_world(request):
    return HttpResponse("No template response", content_type='text/html')


def home(request):
    return render(request, 'welcome/home.html', {})


def index(request):
    friends = ["Vilas", "Anurag", "Prashant", "Chandan"]
    return render(request, 'welcome/index.html', context={"my_name": "Vilas", "friends": friends, 'time': datetime.now()})


def request_demo(request, user="Anurag"):
    print(request.path)
    print(request.scheme)
    print(request.method)
    print(request.headers)
    print(request.body)
    print(user)

    if request.method == 'GET':
        username = request.GET.get('userid', None)
        password = request.GET.get('password', None)
        print(username, password)
    if request.method == 'POST':
        username = request.POST.get('userid', None)
        password = request.POST.get('password', None)
        print(username, password)
        return redirect('index')
    return render(request, 'welcome/request.html', {'user': user})


def static_demo(request):
    return render(request, 'welcome/static.html')
