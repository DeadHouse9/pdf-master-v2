from django import forms

from .models import Book

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title','author','pdf')

class UrlForm(forms.Form):
	url = forms.URLField(label='',
		widget=forms.TextInput(attrs={'placeholder': 'Введите url желаемой web страницы...'}))
