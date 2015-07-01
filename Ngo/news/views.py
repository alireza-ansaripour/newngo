# -*- coding: utf-8 -*-
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required, user_passes_test

from Ngo.settings import BASE_DIR

from Ngo.news.models import News, Photo, Comment
from Ngo.forms import AddArticleForm, about_form, history_form, comment_form, AddPicForm
from Ngo.templatetags.date import persian_date
from Ngo.persons.models import Expert, NGO


def home(request):
    i_news = News.get_all_important_news()
    r_news = News.get_all_regular_news()
    # return HttpResponse(expert.id)
    title = "سایت انجمن دوستی ایران و سهایر کشور ها"
    return render(request, 'home.html', {'i_news': i_news, 'r_news': r_news, 'title': title})

#


@login_required(login_url='login')
def create_article(request):
    if request.method == 'POST':
        if True:
            article = News()
            unique_id = get_random_string()
            article.title_image = request.FILES['title_image']
            article.title_image.name = str(unique_id)+'.jpg'
            article.random_int = unique_id
            article.title = request.POST['title']
            article.description = request.POST['description']
            article.text = request.POST['text']
            expert = Expert.objects.get(username=request.user.username)
            ngo = expert.ngo
            article.continent = ngo.continent
            article.ngo = ngo
            article.save()
            return redirect('http://176.9.177.17/')
        else:
            return redirect('http://176.9.177.17/')
    else:
        form = AddArticleForm()
    return render(request, 'new_article.html', {'form': form})


def edit(request):
    article = News.objects.get(id=1)
    return HttpResponse(article.text)


def show_article(request, id):
    if request.method == "POST":
        form = comment_form(request.POST)
        comment = form.save(commit=False)
        comment.news = News.objects.get(random_int=id)
        comment.save()
    news = News.objects.get(random_int=id)
    date = persian_date(news)
    form = comment_form()
    title = news.title
    comments = news.comments.all()
    return render(request, 'Show_news.html', {'news': news, 'date': date, 'form': form, 'title': title, 'comments': comments})


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
    return redirect('http://176.9.177.17/editnews/')


def user_home(request):
    return redirect('http://176.9.177.17/')


def filter_news(request, continent):
    news = News.objects.filter(continent=continent)
    return render(request, 'show_new_news.html', {'n_news': news})


def show_NGO(request, name):
    ngo = NGO.objects.get(latin_name=name)
    news = News.objects.filter(ngo=ngo)
    form = about_form()
    can_edit = False
    if request.user.is_authenticated():
        if not request.user.is_superuser:
            expert = Expert.objects.get(username=request.user.username)
            ngo_name = expert.get_Ngo().latin_name
            if ngo_name == name:
                can_edit = True
    photos = Photo.objects.filter(ngo=ngo)
    pic_form = AddPicForm()
    return render(request, 'ngo/germany.html', {'page_title': name, 'ngo': ngo, 'r_news': news, 'form': form, 'can_edit': can_edit, 'pics': photos, 'pic_form': pic_form})


def request_ngo(request, name, kind):
    if request.method == 'POST':
        ngo = NGO.objects.get(latin_name=name)
        if kind == 'about':
            text = request.POST['about']
            ngo.about = text
        if kind == 'history':
            text = request.POST['history']
            ngo.history = text

        if kind == 'country':
            text = request.POST['about']
            ngo.country = text
        ngo.save()
        return redirect('http://176.9.177.17/ngo/'+name+'/')

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
        return render(request, 'ngo/about.html', {'ngo': ngo, 'text': text, 'form': form, 'can_edit': can_edit, 'pics': photos})
    if kind == 'history':
        text = ngo.history
        form = history_form()
        return render(request, 'ngo/history.html', {'ngo': ngo, 'text': text, 'form': form, 'can_edit': can_edit, 'pics': photos})


