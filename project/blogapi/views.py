from django.shortcuts import render

# Create your views here.

def return_items(request):
    return render(request, "index.html")