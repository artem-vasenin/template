from django.urls import path

from .views import PageView


app_name='faq'

urlpatterns = [
    path('', PageView.as_view(), name='view'),
]