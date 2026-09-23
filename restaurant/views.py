# Alvaro Sanchez Faria
# alvs@bu.edu
# views.py: displays page on browser and handles requests

from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import datetime
import time

menu = [
    "Classic Cheese Pizza",
    "Meat Lovers Pizza",
    "Veggie Pizza",
    "BBQ Pizza"
]

specials = [
    "Spicy Italian Pizza", 
    "Black Garlic Truffle Pizza",
    "Tiramisu Pizza",
    "Pineapple Pizza"
    ]

pizza_prices = {"Meat Lovers Pizza": 11, "Veggie Pizza": 7, "BBQ Pizza": 10}
classic_prices = {"None": 0, "Regular": 9, "Extra Cheese": 10}
special_prices = {"Spicy Italian Pizza": 15, "Black Garlic Truffle Pizza": 18, "Tiramisu Pizza": 15, "Pineapple Pizza": 13}

# Create your views here.
def main(request):
    '''Displays the main page to the user'''
    template_name1 = 'restaurant/main.html'
    #dictionary of context variables
    context = {
        "img_4": "img_restaurant.jpg"
    }

    return render(request, template_name1, context)

def order(request):
    '''Displays the order page to the user'''
    template_name2 = 'restaurant/order.html'
    #dictionary of context variables
    context = {
        "Special": specials[random.randint(0,3)]
    }

    return render(request, template_name2, context)

def submit(request):
    '''Processes Form Submission, and generates a result'''

    template_name = "restaurant/confirmation.html"
    print(request.POST)

    #Check if POST data was sent with the HTTP POST message:
    if request.POST:
        #extract form fields into variables:
        order = request.POST.getlist('Pizza')
        classic = request.POST.get('Classic')
        special = request.POST.get('Special')

        readytime = int(time.time()) + random.randint(30,60) * 60
        display = datetime.fromtimestamp(readytime).strftime("%I:%M %p")

        total = sum(pizza_prices.get(p,0) for p in order)
        total += classic_prices.get(classic, 0) if special else 0
        total += special_prices.get(special, 0)  if special else 0

        #create context variable for use in the templates:
        context = {
            'Pizza': order,
            'Special': special,
            'Classic': classic,
            'Time': display,
            'Total': total,
        }

    # delegate the response to the template, provide context variables:
    return render(request, template_name, context)
