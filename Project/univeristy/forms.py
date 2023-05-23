from django import forms
from .models import *



class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Adı")
    slug = forms.SlugField(max_length=255, label="Soyadi")
    slugg = forms.SlugField(max_length=255, label="yasi")
    is_published = forms.BooleanField(label="Təqaüd")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Haqqımda")


