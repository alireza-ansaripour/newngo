# -*- coding: utf-8 -*-
from django import forms

from Ngo.persons.models import Expert, Admin, NGO
from Ngo.news.models import News, Photo, Comment


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='رمز')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار')

    class Meta:
        model = Expert
        fields = ['username', 'password1', 'password2', 'email']


class AddArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddArticleForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'id': 'summernote'})
        self.fields['text'].widget.attrs.update({'dir': 'rtl'})
        self.fields['title'].widget.attrs.update({'dir': 'rtl'})
        self.fields['description'].widget.attrs.update({'dir': 'rtl'})

    class Meta:
        model = News
        fields = ['title', 'description', 'text', 'title_image']


class AddPicForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['pic', 'text']

    def __init__(self, *args, **kwargs):
        super(AddPicForm, self).__init__(*args, **kwargs)
        self.fields['pic'].label = 'تصویر'
        self.fields['text'].label = 'توضیحات'
        self.fields['text'].widget.attrs.update({'dir': 'rtl'})




class AddAdmin(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='رمز')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار')

    class Meta:
        model = Admin
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(AddAdmin, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if not password2 == password1:
            raise forms.ValidationError('گذرواژه و تکرار آن یکی نیست')
        return password1

    def save(self, commit=True):
        user = super(AddAdmin, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_superuser = True
        user.first_name = ''
        user.last_name = ''
        user.email = ''
        user.is_staff = False
        user.is_active = True
        if commit:
            user.save()
        return user


class AddExpert(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='رمز')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار')

    class Meta:
        model = Expert
        fields = ['username', 'password1', 'password2', 'ngo']

    def __init__(self, *args, **kwargs):
        super(AddExpert, self).__init__(*args, **kwargs)
        self.fields['ngo'].label = 'سمن'
        self.fields['username'].label = 'نام کاربری'

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if not password2 == password1:
            raise forms.ValidationError('گذرواژه و تکرار آن یکی نیست')
        return password1

    def save(self, commit=True):
        user = super(AddExpert, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_superuser = False
        user.first_name = ''
        user.last_name = ''
        user.email = ''
        user.is_staff = True
        user.is_active = True
        if commit:
            user.save()
        return user


class Add_ngo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Add_ngo, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'نام کشور'
        self.fields['latin_name'].label = 'نام کشور به لاتین'
        self.fields['continent'].label = 'قاره'

    class Meta:
        model = NGO
        fields = ['name', 'latin_name', 'continent']


class about_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(about_form, self).__init__(*args, **kwargs)
        self.fields['about'].widget.attrs.update({'id': 'summernote'})

    class Meta:
        model = NGO
        fields = ['about']


class history_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(history_form, self).__init__(*args, **kwargs)
        self.fields['history'].widget.attrs.update({'id': 'summernote'})

    class Meta:
        model = NGO
        fields = ['history']


class comment_form(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'text']

    def __int__(self, *args, **kwargs):
            super(comment_form, self).__init__(*args, **kwargs)
            self.fields['text'].widget.attrs.update({'dir': 'rtl'})
            self.fields['name'].label = 'نام'
            self.fields['text'].label = 'متن'
