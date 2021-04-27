from django.shortcuts import render
import socket
from .utils import search_book
from .models import Books


def home_view(request):
    if request.method == "GET":
        return render(request, "libgen/home.html")

    if request.method == "POST":
        search_keyword = request.POST["book"]
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        books = search_book(search_keyword)
        print(books)
        # context = {"books": books}
        for book in books:
            Books.objects.create(
                keyword=search_keyword,
                title=book["title"],
                author=book["author"],
                language=book["language"],
                pages=book["pages"],
                book_format=book["format"],
                size=book["size"],
                url=book["url"],
                ip=ip_address,
            )
        print(type(ip_address))
        return render(request, "libgen/home.html")
