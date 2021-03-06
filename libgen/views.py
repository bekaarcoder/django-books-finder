from django.shortcuts import render
import socket
import django_rq
from rq import Queue
from worker import conn
from .utils import search_book, get_books
from .models import Books
import time


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
        ip_address = get_ip()
        old_books = Books.objects.filter(ip=ip_address)
        old_books.delete()

        books = get_books()
        print(books)

        # uncomment while running in local and comment the queue
        # books = search_book(search_keyword)

        # Creating a queue for background process
        # q = Queue(connection=conn)
        # task = q.enqueue(search_book, search_keyword, ip_address)
        # jobs = q.jobs
        # q_len = len(q)
        # print(f"Task queued. {q_len} jobs queued.")

        task = django_rq.enqueue(search_book, search_keyword, ip_address)

        # for book in books:
        #     Books.objects.create(
        #         keyword=search_keyword,
        #         title=book["title"],
        #         author=book["author"],
        #         language=book["language"],
        #         pages=book["pages"],
        #         book_format=book["format"],
        #         size=book["size"],
        #         url=book["url"],
        #         image=book["image_url"],
        #         ip=ip_address,
        #     )
        # all_books = Books.objects.filter(ip=ip_address)
        # context = {"books": all_books}
        context = {
            "message": "We are searching for your book. Please hang on..."
        }
        return render(request, "libgen/home.html", context)


def view_book(request, pk):
    book = Books.objects.get(id=pk)
    context = {"book": book}
    return render(request, "libgen/book-view.html", context)
