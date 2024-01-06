from django.shortcuts import render
from .models import Dish
from .forms import SearchForm

def search(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Dish.objects.filter(name__icontains=query)

    return render(request, 'search_results.html', {'form': form, 'results': results})
