from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    def __str__(self):
        return self.category_name

class CoverImage(models.Model):
    cover_photo = models.ImageField(upload_to="images\cover")

class Author(models.Model):
    author_name = models.CharField(max_length=255)
    def __str__(self):
        return self.author_name
    
class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)
    def __str__(self):
        return self.publisher_name

class BooksInfo(models.Model):
    sr = models.AutoField(primary_key=True)
    accession_number = models.PositiveIntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    english_name = models.CharField(max_length=255)
    bangla_name = models.CharField(max_length=255)
    volumn = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    year_of_publication = models.PositiveIntegerField()
    isbn = models.PositiveIntegerField()
    call_no = models.CharField(max_length=255)
    pages = models.IntegerField()
    qty = models.BigIntegerField()
    description = models.TextField()
    price = models.IntegerField()
    location = models.CharField(max_length=255)
    book_cover = models.ImageField(upload_to='images/books')
    year_of_publication = models.IntegerField()
    
    def __str__(self):
        return self.english_name