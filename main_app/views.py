from django.shortcuts import render
from .models import Cat, CatToy
from .forms import CatForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.
def index(request):
    cats = Cat.objects.all()
    return render(request, 'index.html', {'cats': cats})

def show(request, cat_id):
    res = requests.get('http://quotesondesign.com/api/3.0/api-3.0.json?filter[orderby]=rand&filter[posts_per_page]=1&callback=')
    quote = res.json()['quote']
    cat = Cat.objects.get(id=cat_id)
    cattoys = CatToy.objects.all()
    return render(request, 'show.html', {'cat': cat, 'cattoys': cattoys, 'quote': quote}) 

def new(request):
    return render(request, 'new.html', {'form': CatForm})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})

def post_cat(request):
    form = CatForm(request.POST)
    if form.is_valid():
        cat = form.save(commit=False)
        cat.user = request.user
        cat.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('The form broke!')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("Account disabled")
                    return HttpResponseRedirect('/login')
            else:
                print("Username and/or password is incorrect")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def like_cat(request):
    cat_id = request.GET.get('cat_id', None)
    likes = 0
    if cat_id:
        cat = Cat.objects.get(id = int(cat_id))
        if cat is not None:
            likes = cat.likes + 1
            cat.likes = likes
            cat.save()
    return HttpResponse(likes)

def add_toy_to_cat(request):
    cat_id = request.GET.get('cat_id', None)
    toy_id = request.GET.get('toy_id', None)
    if cat_id and toy_id:
        cat = Cat.objects.get(id = int(cat_id))
        toy = CatToy.objects.get(id = int(toy_id))
        cat.cattoys.add(toy)
    return HttpResponse("yay")
