from django.shortcuts import render, HttpResponse

# Create your views here.

def book_detail_query_string(request):
    book_id = request.GET.get('id')
    name = request.GET.get('name')
    return HttpResponse(f"id is {book_id}, name is {name}")

def book_int(request, book_id):
    return HttpResponse(f"book_id int is {book_id}")

def book_str(request, book_id):
    return HttpResponse(f"book_id str is {book_id}")

def book_slug(request, book_id):
    return HttpResponse(f"book_id slug is {book_id}")

def book_path(request, book_id):
    return HttpResponse(f"book_id path is {book_id}")
