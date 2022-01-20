import django_filters
from django import forms
# import django.forms
from blog.models import Post
from django_filters import CharFilter,DateFilter

class PostFilter(django_filters.FilterSet):
	from_date=DateFilter(field_name='date',lookup_expr='gte',label='from date',widget=forms.DateInput(attrs={'type':'date'}))
	to_date=DateFilter(field_name='date',lookup_expr='lte',label='from date',widget=forms.DateInput(attrs={'type':'date'}))
	title=CharFilter(field_name='content',lookup_expr='icontains',label='title')
	post=CharFilter(field_name='title',lookup_expr='icontains',label='content')

	class Meta:
		model=Post
		fields=['author']
