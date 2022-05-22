from django.urls import path, include

from dictionary.views import index, add

app_name = "dictionary"
urlpatterns = [
    path('', index, name='index'),
    path('add', add, name='add'),
]
