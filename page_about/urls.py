from django.urls import path

from .views import PageView


app_name='about'

urlpatterns = [
    path('', PageView.as_view(), name='view'),
]