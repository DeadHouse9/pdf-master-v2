from django.urls import path
from .views import *

urlpatterns = [
	path('',save_pdf,name = 'save_pdf'),
	path('save_pdf/',save_pdf,name = 'save_pdf'),
	path('page_to_pdf/',page_to_pdf,name = 'page_to_pdf'),
]