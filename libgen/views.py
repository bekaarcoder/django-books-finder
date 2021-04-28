from django.shortcuts import render
import socket
from .utils import search_book
from .models import Books


def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def home_view(request):
    if request.method == "GET":
        ip_address = get_ip()
        books = Books.objects.filter(ip=ip_address)

        if books.exists():
            context = {"books": books}
            return render(request, "libgen/home.html", context)

        return render(request, "libgen/home.html")

    if request.method == "POST":
        search_keyword = request.POST["book"]
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        old_books = Books.objects.filter(ip=ip_address)
        old_books.delete()
        books = search_book(search_keyword)
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
                image=book["image_url"],
                ip=ip_address,
            )
        all_books = Books.objects.filter(ip=ip_address)
        context = {"books": all_books}
        return render(request, "libgen/home.html", context)


def view_book(request, pk):
    book = Books.objects.get(id=pk)
    context = {"book": book}
    return render(request, "libgen/book-view.html", context)
