from django.shortcuts import render # type: ignore

from django.http import HttpResponse # type: ignore
# Create your views here.

def home(request):
    #return HttpResponse("Welcome to the Home Page!")
    people_list = [{"name":"Maharshi Vyas","age":20},{"name":"jay vaghela","age":25},{"name":"Harsh vaghela","age":35}]
    return render(request, 'home/index.html',context={"peoples":people_list})


def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')