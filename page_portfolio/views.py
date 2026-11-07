from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.views.generic import DetailView

class PageList(View):
    """ Контроллер страницы списка портфолио"""
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'page_portfolio/index.html')

class PageView(DetailView):
    """ Контроллер страницы портфолио"""
    context_object_name = "page"

    def get(self, request: HttpRequest, pk) -> HttpResponse:
        print(pk)
        return render(request, 'page_portfolio/item.html')