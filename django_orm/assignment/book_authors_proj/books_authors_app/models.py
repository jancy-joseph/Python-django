from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __repr__(self):
		return f'<\nid:{self.id}\ntitle:{self.title}\ndescription:{self.desc}\n>'
class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	notes = models.TextField()
	books = models.ManyToManyField(Book, related_name="authors")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __repr__(self):
		return f'<\nid:{self.id}\nfirst_name:{self.first_name}\nlast_name{self.last_name}\nbooks:{self.books}\n>'
