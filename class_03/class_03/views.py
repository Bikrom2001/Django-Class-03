from django.shortcuts import render;


def home_page(request):
    
    info={
        'name': "Bikram Roy",
        'age': 25,
        "address": "Dhaka, Bangladesh",
    }
    
    
    return render(request, 'home.html', info)