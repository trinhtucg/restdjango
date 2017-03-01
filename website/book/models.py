from asyncio.test_utils import mock_nonblocking_socket

from django.db import models

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_type = models.CharField(max_length=10)

    class Meta:
        db_table = "tb_category"

    def __str__(self):
        return self.cat_name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bookTitle = models.CharField(max_length=100)
    bookPage = models.IntegerField()

    class Meta:
        db_table = "tb_book"

    def __str__(self):
        return self.bookTitle
