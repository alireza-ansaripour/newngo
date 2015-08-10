from django.core.files import File
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import user_passes_test
import datetime

from Ngo.forms import AddAdmin, AddExpert, Add_ngo, AddPicForm, flagForm
from Ngo.news.models import Photo
from Ngo.news.views import show_NGO
from Ngo.persons.models import Admin, Expert, NGO

def user_home(request):
    pass


# @user_passes_test(lambda u: u.is_superuser, login_url='login')
def add_admin(request):
    num = Admin.objects.count()
    if num == 0:
        if request.method == 'POST':
            form = AddAdmin(request.POST)
            form.save()
            return redirect('http://176.9.177.17/')
        else:
            form = AddAdmin()
            return render(request, 'ali.html', {'form': form})
    else:
        return HttpResponseNotFound('<h1>404 Page not found</h1>')


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def add_expert(request):
    if request.method == 'POST':
        form = AddExpert(request.POST)
        if form.is_valid():
            expert = form.save(commit=False)
            expert.save()
    else:
        form = AddExpert()
    list = Expert.objects.all().reverse()
    return render(request, 'add_user.html', {'form': form, 'list': list})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def add_NGO(request):
    list = None
    if request.method == 'POST':
        form = Add_ngo(request.POST, request.FILES)
        if form.is_valid():
            ngo = form.save(commit=False)
            ngo.Website = 'http://176.9.177.17/ngo/'+ngo.latin_name
            photo = ngo.flag
            photo.name = ngo.latin_name + '.jpg'
            ngo.flag = photo
            ngo.save()
            return redirect('http://176.9.177.17/')
    else:
        list = NGO.objects.all().order_by('name')
        form = Add_ngo()
    return render(request, 'ali.html', {'form': form, 'list': list})


@user_passes_test(lambda u: u.is_staff, login_url='login')
def add_pic(request):
    if request.method == 'POST':
        photo = Photo()
        pic = request.FILES['pic']
        name = get_random_string()
        pic.name = name + '.jpg'
        photo.pic = pic
        photo.unique_id = name
        photo.text = request.POST['text']
        expert = Expert.objects.get(username=request.user.username)
        photo.ngo = expert.ngo
        photo.save()
        return show_NGO(request, expert.ngo.latin_name)

    form = AddPicForm()
    return render(request, 'ngo/add_pic.html', {'form': form})


def delete_NGO(request, name):
    try:
        ngo = NGO.objects.get(latin_name=name)
        ngo.delete()
        return HttpResponse('deleted')
    except:
        return HttpResponse('cannot delete')


def delete_user(request, username):
    try:
        user = Expert.objects.get(username=username)
        Expert.delete()
        return HttpResponse('deleted')
    except:
        return HttpResponse('cannot delete')