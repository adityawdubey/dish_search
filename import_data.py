import csv
from dish_search_app.models import Dish

with open('restaurants_small.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader) 
    for row in reader:
        Dish.objects.create(name=row[1])
