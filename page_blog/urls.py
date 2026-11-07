from django.urls import path

from .views import PageView, PageList


app_name='blog'

urlpatterns = [
    path('', PageList.as_view(), name='list'),
    path('<slug:slug>', PageView.as_view(), name='view'),
]