from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from random import choice
from string import ascii_uppercase

import pdfkit

from .forms  import BookForm, UrlForm
from .models import Book# Create your views here.

def save_pdf(request):
	if request.method == 'POST':
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = BookForm()
		books = Book.objects.all()
		return render(request,'pdf_master/save_pdf.html', {
			'books': books,
			'form': form,
		})
	return redirect('/')


def page_to_pdf(request):
	if request.method == 'POST':
		form = UrlForm(request.POST)
		if form.is_valid():
			url = form.cleaned_data['url']
			file_name = ''.join(choice(ascii_uppercase) for i in range(12))
			path = 'media/books/pdfs/'+file_name+'.pdf'
			pdfkit.from_url(url,path)
			return redirect("../../"+path)
	else: 
		form = UrlForm()
	return render(request,'pdf_master/page_to_pdf.html', {'form': form})