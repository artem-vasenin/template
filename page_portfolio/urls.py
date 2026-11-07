from django.urls import path

from .views import PageView, PageList


app_name='portfolio'

urlpatterns = [
    path('', PageList.as_view(), name='list'),
    path('<int:pk>', PageView.as_view(), name='view'),
]