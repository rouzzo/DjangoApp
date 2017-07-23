from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/contact.html', {'content':['Contact me at:','django@django.com', '(405) 998-456']})
