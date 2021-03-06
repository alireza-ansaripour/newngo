# -*- coding: utf-8 -*-
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required, user_passes_test
from Ngo.settings import BASE_DIR
from Ngo.news.models import News, Photo
from Ngo.forms import AddArticleForm, about_form, history_form, comment_form, AddPicForm, AdminAddArticleForm, EditArticleForm
from Ngo.persons.models import Expert, NGO


def home(request):
    i_news = News.get_all_important_news()
    r_news = News.get_all_regular_news()
    related_news = News.get_all_related_news()
    title = "پایگاه اینترنتی انجمن های دوستی ایران و سایر کشور ها"
    return render(request, 'home.html',
                  {'i_news': i_news, 'r_news': r_news, 'title': title, 'related_news': related_news})


@login_required(login_url='login')
def create_article(request):
    if request.method == 'POST':
        user = request.user
        expert = Expert.objects.get(username=user.username)
        ngo = expert.ngo
        if ngo.latin_name == "test":
            form = AdminAddArticleForm(request.POST)
            if form.is_valid():
                news = form.save(commit=False)
                unique_id = get_random_string()
                news.random_int = unique_id
                expert = Expert.objects.get(username=request.user.username)
                ngo = expert.ngo
                news.ngo = ngo
                news.continent = ngo.continent
                news.save()
                return redirect('/')
        else:
            form = AddArticleForm(request.POST, request.FILES)
            if form.is_valid():
                news = form.save(commit=False)
                unique_id = get_random_string()
                news.random_int = unique_id
                photo = news.title_image
                photo.name = unique_id + '.jpg'
                expert = Expert.objects.get(username=request.user.username)
                ngo = expert.ngo
                news.ngo = ngo
                news.continent = ngo.continent
                news.save()
                return redirect('/')
    user = request.user
    expert = Expert.objects.get(username=user.username)
    ngo = expert.ngo
    if ngo.latin_name == "test":
        form = AdminAddArticleForm()
    else:
        form = AddArticleForm()
    return render(request, 'new_article.html', {'form': form})


def edit(request):
    article = News.objects.get(id=1)
    return HttpResponse(article.text)


def show_article(request, id):
    # if request kind is post a comment form is sent
    if request.method == "POST":
        can_edit = False
        news = News.objects.get(random_int=id)
        if request.user.is_authenticated():
            if not request.user.is_superuser:
                expert = Expert.objects.get(username=request.user.username)
                if expert.ngo.name == news.ngo.name:
                    can_edit = True

        if not can_edit:
            return HttpResponse('not done')

        form = EditArticleForm(request.POST, request.FILES)
        if form.is_valid():
            news.title = form.cleaned_data['title']
            news.description = form.cleaned_data['description']
            if form.cleaned_data['title_image'] is not None:
                news.title_image = form.cleaned_data['title_image']
            news.text = form.cleaned_data['text']
            news.save()
    if request.method == 'DELETE':
        news = News.objects.get(random_int=id)
        news.delete()
        return HttpResponse('done')

    news = News.objects.get(random_int=id)
    form = comment_form()
    title = news.title
    comments = news.comments.all()
    ngo = news.ngo
    can_edit = False
    if request.user.is_authenticated():
        if not request.user.is_superuser:
            expert = Expert.objects.get(username=request.user.username)
            if ngo == expert.ngo:
                can_edit = True

    editForm = EditArticleForm(
        initial={'title': news.title, 'description': news.description, 'title_image': news.title_image})


    related_news = News.get_all_related_news()
    return render(request, 'Show_news.html',
                  {'news': news, 'form': form, 'title': title, 'comments': comments, 'can_edit': can_edit,
                   'editForm': editForm, 'related_news': related_news})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def show_new_news(request):
    n_news = News.get_all_new_news()
    return render(request, 'show_new_news.html', {'n_news': n_news})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def update_news(request, id, status):
    news = News.objects.get(random_int=id)
    if status != 'd':
        news.status = status
        news.save()
        if status == 'a':
            return show_news(request)
    else:
        os.remove(BASE_DIR + '/media/' + news.random_int + '.jpg')
        news.delete()
    return show_new_news(request)


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def show_news(request):
    r_news = News.get_all_regular_news()
    i_news = News.get_all_important_news()
    return render(request, 'edit_news.html', {'r_news': r_news, 'i_news': i_news})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def delete_news(request, id):
    News.objects.get(random_int=id).delete()
    return redirect('/editnews/')


def user_home(request):
    return redirect('/')


def filter_news(request, continent):
    news = News.objects.filter(continent=continent).exclude(status='n').order_by('-date')

    related_news = News.get_all_related_news()
    return render(request, 'show_new_news.html', {'n_news': news, 'related_news': related_news})


def show_NGO(request, name):
    ngo = NGO.objects.get(latin_name=name)
    news = News.objects.filter(ngo=ngo).order_by("-date")
    form = about_form()
    can_edit = False
    if request.user.is_authenticated():
        if not request.user.is_superuser:
            expert = Expert.objects.get(username=request.user.username)
            ngo_name = expert.get_Ngo().latin_name
            if ngo_name == name:
                can_edit = True
    photos = Photo.objects.filter(ngo=ngo).order_by('-date')[0:4]
    title = ngo.name
    return render(request, 'ngo/germany.html',
                  {'page_title': name, 'ngo': ngo, 'r_news': news, 'form': form, 'can_edit': can_edit, 'pics': photos,
                   'title': title})


def request_ngo(request, name, kind):
    if request.method == 'POST':

        if request.user.is_authenticated():
            ngo = NGO.objects.get(latin_name=name)
            expert = Expert.objects.get(username=request.user.username)
            if expert.ngo == ngo:
                text = request.POST['data']
                if kind == 'country':
                    ngo.country = text
                    print(text)
                if kind == 'about':
                    ngo.about = text
                if kind == 'history':
                    ngo.history = text
                ngo.save()
                return redirect('/ngo/' + name + '/')
        return redirect('/login/')

    ngo = NGO.objects.get(latin_name=name)
    photos = Photo.objects.filter(ngo=ngo)
    can_edit = False
    if request.user.is_authenticated():
        if not request.user.is_superuser:
            expert = Expert.objects.get(username=request.user.username)
            ngo_name = expert.get_Ngo().latin_name
            if ngo_name == name:
                can_edit = True
    if kind == 'about':
        text = ngo.about
        form = about_form()
        title = ngo.name
        return render(request, 'ngo/about.html',
                      {'ngo': ngo, 'text': text, 'form': form, 'can_edit': can_edit, 'pics': photos, 'title': title})
    if kind == 'history':
        text = ngo.history
        form = history_form()
        title = ngo.name
        return render(request, 'ngo/history.html',
                      {'ngo': ngo, 'text': text, 'form': form, 'can_edit': can_edit, 'pics': photos, 'title': title})


