from django.db import models


class Books(models.Model):
    keyword = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    pages = models.CharField(max_length=255)
    book_format = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Books"
