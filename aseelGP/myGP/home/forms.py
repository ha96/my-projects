from django import forms
from django.contrib.auth.models import User
from .models import UserInfo
import re
from .models import Post, PostCategoryEnum, UploadedFile
import string

from django.core import validators


class UserForm(forms.ModelForm):
    password = forms.CharField(min_length=9, widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('email', 'password')

    def clean(self):

        # data from the form is fetched using super function
        super(UserForm, self).clean()

        # extract the username and text field from the data
        password = self.cleaned_data.get('password')

        # conditions to be met for the username length

        if len(password) < 8:
            self._errors['password'] = self.error_class([
                'your password length too short must be at least 8 '])

        if len(password) > 14:
            self._errors['password'] = self.error_class([
                'your password length too long must be less than or equal 14'])

        if not re.findall('\d', password):
            self._errors['password'] = self.error_class([
                'The password must contain at least 1 digit, 0-9.'])

        if not re.findall('[A-Z]', password):
            self._errors['password'] = self.error_class([
                'The password must contain at least 1 uppercase letter, A-Z.'])

        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            self._errors['password'] = self.error_class([
                "The password must contain at least 1 special character: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"])

        if not re.search("[a-z]", password):
            self._errors['password'] = self.error_class([
                'The password must contain at least 1 lowercase letter, a-z.'])

        #common pass done in seting file using buld in django method
        # return any errors if found
        return self.cleaned_data


class UserAddForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('full_name', 'age', 'phone_number', 'bio')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'category_enum']

    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    category_enum = forms.ChoiceField(
        choices=[(choice.value, choice.name) for choice in PostCategoryEnum],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        max_content_length = 63206  # Set the maximum content length to 63,206 characters

        if len(content) > max_content_length:
            raise forms.ValidationError(f"Content must be at most {max_content_length} characters long.")

        return content


class FileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['name', 'file', 'category_enum']
