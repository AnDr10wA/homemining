from django import forms
from .models import *
from django.core.exceptions import ValidationError

# class NewsForm(forms.ModelForm):
#
#     class Meta:
#
#         model = News
#         fields = ['title', 'slug', 'head', 'body', 'tags']
#
#         widgets = {
#             'title': forms.TextInput(attrs={'class': "form-control",'width':'50%' , 'align':"center"}),
#             'slug': forms.TextInput(attrs={'class': "form-control",'width':'50%' , 'align':"center"}),
#             'head': forms.Textarea(attrs={'class': "form-control",'width':'50%' , 'align':"center"}),
#             'body': forms.Textarea(attrs={'class': "form-control",'width':'50%' , 'align':"center"}),
#             'tags': forms.SelectMultiple(attrs={'class': "form-control",'width':'50%' , 'align':"center"}),
#
#         }
#     def clean_slug(self):
#         new_slug = self.cleaned_data['slug'].lower()
#         if new_slug == 'create':
#             raise ValidationError('Slug may not be "Create"')
#         if News.objects.filter(slug=new_slug).count():
#             raise ValidationError('Slug must be unique')
#         return new_slug
