from django.shortcuts import render


def home_view(request):
    if request.method == "GET":
        return render(request, "libgen/home.html")

    if request.method == "POST":
        book = request.POST["book"]
        print(book)
        return render(request, "libgen/home.html")
