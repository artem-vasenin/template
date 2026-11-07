from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest

class PageView(View):
    """ Контроллер страницы контакты"""
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'page_contacts/index.html')