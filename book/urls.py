from django.urls import path

from . import views

app_name='book'

urlpatterns=[
    path('', views.book_detail_query_string, name='index'),
    path('int/<int:book_id>', views.book_int),
    path('str/<str:book_id>', views.book_str),
    path('slug/<slug:book_id>', views.book_slug, name='book_slug'),
    path('path/<path:book_id>', views.book_path, name='book_path'),

]