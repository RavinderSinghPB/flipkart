from django.http import HttpResponse
from django.urls import path


def all_products(request):
    l= ['tv','mobile','laptop','fridge','ac','shirt','paint','fashion']

    return HttpResponse(l)


urlpatterns = [
    path('all',all_products),
]