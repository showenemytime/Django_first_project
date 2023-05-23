from django.shortcuts import render

from django.http import HttpResponse
from .models import News, Category


def index(request):
    news = News.objects.order_by('-created_at')

    context = {'news': news,
               'title': 'Список новостей',

               }

    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(id=category_id)
    context = {
        'news': news,
        'category': category,
    }

    return render(request, 'news/category.html', context)
