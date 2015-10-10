# -*- coding: utf-8 -*-

from django import forms
from Ngo.persons.models import Expert, Admin, NGO
from Ngo.news.models import News, Photo, Comment


class flagForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ['flag']


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
        self.fields['title'].label = 'عنوان'
        self.fields['text'].label = 'متن خبر'
        self.fields['description'].label = 'توضیحات'
        self.fields['title_image'].label = 'تصویر عنوان'

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
        self.fields['ngo'].label = 'انجمن دوستی'
        self.fields['username'].label = 'نام کاربری'
        for k, field in self.fields.items():
            if 'required' in field.error_messages:
                field.error_messages['required'] = 'نباید خالی باشد'

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
        self.fields['flag'].label = 'پرجم کشور'
        for k, field in self.fields.items():
            if 'required' in field.error_messages:
                field.error_messages['required'] = 'نباید خالی باشد'

    class Meta:
        model = NGO
        fields = ['name', 'latin_name', 'continent', 'flag']

    def clean_latin_name(self):
        name = self.cleaned_data['latin_name']
        if not name.isalpha():
            raise forms.ValidationError('نام را به لاتین وارد کنید')

        number = NGO.objects.filter(latin_name=name).count()
        if number != 0:
            raise forms.ValidationError('این نام لاتین را قبلا وارد کرده اید')
        return name





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

    def __init__(self, *args, **kwargs):
            super(comment_form, self).__init__(*args, **kwargs)
            self.fields['text'].widget.attrs.update({'dir': 'rtl'})
            self.fields['name'].widget.attrs.update({'dir': 'rtl'})
            self.fields['name'].label = 'نام'
            self.fields['text'].label = 'متن'

    def clean_name(self):
        name = self.cleaned_data['name']
        print('name '+name)
        if name == '':
            raise forms.ValidationError('نباید خالی باشد')


class country_form(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ['country']

    def __init__(self, *args, **kwargs):
        super(history_form, self).__init__(*args, **kwargs)


class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='رمز کنونی')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='رمز جدید')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار')

    class Meta:
        model = Expert
        fields = ['password', 'password1', 'password2']

    def setUser(self, user):
        self.user = user

    def clean_password(self):
        password = self.cleaned_data['password']
        if not self.user.check_password(password):
            raise forms.ValidationError('رمز عبور نادرست است')
        return password

    def clean_password2(self):
        pass1 = self.cleaned_data['password1']
        pass2 = self.cleaned_data['password2']
        if pass1 != pass2:
            raise forms.ValidationError('رمز عبور و تکرار آن یکی نیست')
        return pass1


class EditNgoForm(forms.ModelForm):

    class Meta:
        model = NGO
        fields = ['name', 'latin_name', 'continent', 'flag']

    def __init__(self, *args, **kwargs):
        super(EditNgoForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'نام کشور'
        self.fields['latin_name'].label = 'نام لاتین کشور'
        self.fields['continent'].label = 'قاره'
        for k, field in self.fields.items():
            if 'required' in field.error_messages:
                field.error_messages['required'] = 'نباید خالی باشد'

    def clean_latin_name(self):
        name = self.cleaned_data['latin_name']
        if not name.isalpha():
            raise forms.ValidationError('نام را به لاتین وارد کنید')
        number = NGO.objects.filter(latin_name=name).count()
        if number != 0:
            raise forms.ValidationError('این نام لاتین را قبلا وارد کرده اید')

        return name