from django.shortcuts import render;


def home_page(request):
    
    info={
        'name': "Bikram Roy",
        'age': 25,
        "address": "Dhaka, Bangladesh",
    }
    
    
    return render(request, 'home.html', info)


def about_page(request):
    
    return render(request, 'about.html')        

def contact_page(request):
    
    return render(request, 'contact.html')