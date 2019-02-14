from django.db import models
from .validators import validate_file_extension
 

class Book(models.Model):
	title = models.CharField(max_length = 100)
	author = models.CharField(max_length = 100)
	pdf = models.FileField(upload_to='books/pdfs/',validators=[validate_file_extension])


	def __str__(self):
		return self.title
# Create your models here.
