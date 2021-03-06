import os
from django.core.files import File
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import user_passes_test
import datetime

from Ngo.forms import AddAdmin, AddExpert, Add_ngo, AddPicForm, flagForm, ChangePasswordForm, EditNgoForm
from Ngo.news.models import Photo
from Ngo.news.views import show_NGO
from Ngo.persons.models import Admin, Expert, NGO
from Ngo.settings import BASE_DIR


def user_home(request):
    pass


# @user_passes_test(lambda u: u.is_superuser, login_url='login')
def add_admin(request):
    num = Admin.objects.count()
    if num == 0:
        if request.method == 'POST':
            form = AddAdmin(request.POST)
            form.save()
            return redirect('/')
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
    list = NGO.objects.all().order_by('name')
    if request.method == 'DELETE':
        pass
    if request.method == 'POST':
        form = Add_ngo(request.POST, request.FILES)
        if form.is_valid():
            ngo = form.save(commit=False)
            ngo.Website = '/ngo/'+ngo.latin_name
            photo = ngo.flag
            photo.name = ngo.latin_name + '.jpg'
            ngo.flag = photo
            ngo.save()
            return redirect('/')
    else:
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
        return redirect('/ngo/'+expert.ngo.latin_name)

    form = AddPicForm()
    return render(request, 'ngo/add_pic.html', {'form': form})


@user_passes_test(lambda u: u.is_staff, login_url='login')
def delete_pic(request, id):
    user = request.user
    pic = Photo.objects.get(unique_id=id)
    ngo = pic.ngo
    experts = ngo.expert_set.all()
    can_delete = False
    for expert in experts:
        if user.username == expert.username:
            can_delete = True

    if can_delete:
        pic.delete()
        return HttpResponse('deleted')

    return HttpResponse('not deleted')


@user_passes_test(lambda x: x.is_superuser)
def delete_NGO(request, name):
    try:
        ngo = NGO.objects.get(latin_name=name)
        ngo.delete()
        return HttpResponse('deleted')
    except:
        return HttpResponse('cannot delete')


@user_passes_test(lambda x: x.is_superuser)
def delete_user(request, username):
    try:
        user = Expert.objects.get(username=username)
        user.delete()
        return HttpResponse('deleted')
    except Exception as e:
        return HttpResponse(str(e))


@user_passes_test(lambda x: not x.is_superuser and x.is_staff)
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        form.setUser(request.user)
        if form.is_valid():
            user = Expert.objects.get(username=request.user.username)
            user.set_password(form.cleaned_data['password1'])
            user.save()
    else:
        form = ChangePasswordForm()
    return render(request, 'change_pass.html', {'form': form})


@user_passes_test(lambda x: x.is_superuser)
def edit_Ngo(request, ngo):
    if request.method == 'POST':
        form = EditNgoForm({'name': ngo}, request.POST, request.FILES)
        if form.is_valid():
            ngo = NGO.objects.get(latin_name=ngo)
            ngo.name = form.cleaned_data['name']
            ngo.latin_name = form.cleaned_data['latin_name']
            ngo.Website = '/ngo/' + ngo.latin_name + '/'
            ngo.continent = form.cleaned_data['continent']
            pic = ngo.flag
            try:
                os.remove(os.path.join(BASE_DIR, "media/flags/", ngo.latin_name+".jpg"))
            except Exception as e :
                print(e)

            pic = form.cleaned_data['flag']
            pic.name = form.cleaned_data['latin_name'] + '.jpg'
            ngo.flag = pic
            ngo.save()
            return redirect('/')
    else:
        ngo = NGO.objects.get(latin_name=ngo)
        form = EditNgoForm({'name': ngo.latin_name}, initial={'name': ngo.name, 'latin_name': ngo.latin_name, 'continent': ngo.continent})
    return render(request, 'ngo/edit_ngo.html', {'form': form})
