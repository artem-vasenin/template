from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.views.generic import DetailView

class PageList(View):
    """ Контроллер страницы списка новостей"""
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'page_blog/index.html')

class PageView(DetailView):
    """ Контроллер страницы новости"""
    context_object_name = "page"

    def get(self, request: HttpRequest, slug) -> HttpResponse:
        print(slug)
        return render(request, 'page_blog/item.html')