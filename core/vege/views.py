from django.shortcuts import render,redirect

#import models
from .models import *

# Create your views here.
def receipes(request):
    if(request.method == 'POST'):
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        #store in database
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        return redirect('/receipes/')
    
    queryset = Receipe.objects.all()
    #searching
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = Receipe.objects.filter(receipe_name__icontains=search)

    context = { 'receipes':queryset , 'search':search}
    return render(request, 'receipes.html', context)

def delete_receipe(request, receipe_id):
    receipe = Receipe.objects.get(id=receipe_id)
    receipe.delete()
    return redirect('/receipes/')

def update_receipe(request, receipe_id):
    receipe = Receipe.objects.get(id=receipe_id)

    if(request.method == 'POST'):
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        receipe.receipe_name = receipe_name
        receipe.receipe_description = receipe_description

        if(receipe_image):
            receipe.receipe_image = receipe_image

        receipe.save()
        return redirect('/receipes/')

    context = { 'receipe_data':receipe}
    return render(request, 'update_receipes.html', context)

