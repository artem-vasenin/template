from django.urls import path

from .views import PageView


app_name='home'

urlpatterns = [
    path('', PageView.as_view(), name='view'),
]