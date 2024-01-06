from django.contrib import admin
from django.urls import path, include
from dish_search_app.views import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dish_search/', include('dish_search_app.urls')),
    path('', search, name='search_results'),
]
