from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def posts_list(request):
    n = ['Oleg', 'Masha', 'Olga', 'Ksu']
    return render(request, 'blog/index.html', context={'names': n})