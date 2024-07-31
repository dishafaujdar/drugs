from django.shortcuts import render

# Create your views here.
def all_store(request):
    return render(request, 'stores/all_stores.html')
