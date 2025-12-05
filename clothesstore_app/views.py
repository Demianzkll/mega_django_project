from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import random



# Create your views here.

def clothes_store(request):
    items = Product.objects.all()  
    return render(request, 'clothes_store.html', {'items': items})



names = [
    "T-Shirt", "Hoodie", "Jeans", "Jacket", "Shorts",
    "Sweater", "Cap", "Socks", "Sweatpants", "Shirt"
]

brands = [
    "Nike", "Adidas", "Puma", "H&M", "Zara",
    "Gucci", "LV", "Uniqlo", "Reebok", "Bershka"
]

sizes = ["XS", "S", "M", "L", "XL"]

colors = [
    "Black", "White", "Red", "Blue", "Green",
    "Yellow", "Gray", "Brown", "Orange", "Purple"
]

prices = [random.randint(200, 5000) for _ in range(10)]



def replenish_products(request, count):
    for _ in range(count):
        data = {
            "name": random.choice(names),
            "brand": random.choice(brands),
            "size": random.choice(sizes),
            "color": random.choice(colors),
            "price": random.randint(200, 5000),
        }
        
        Product.objects.create(**data)
        
    return HttpResponse(f"{count} products added successfully!")