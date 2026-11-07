from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest

class PageView(View):
    """ Контроллер страницы вопросов"""
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'page_faq/index.html')