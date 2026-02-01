from django.shortcuts import render,redirect

#import models
from .models import *

#Http Response
from django.http import HttpResponse

#Auth
from django.contrib.auth.models import User

#Error Message
from django.contrib import messages

#authentication
from django.contrib.auth import authenticate,login,logout # type: ignore

#login required decorates
from django.contrib.auth.decorators import login_required

#for Pagination
from django.core.paginator import Paginator

# custom user model call
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@login_required(login_url='/login/')
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

# Delete Receipe
def delete_receipe(request, receipe_id):
    receipe = Receipe.objects.get(id=receipe_id)
    receipe.delete()
    return redirect('/receipes/')

# Update Receipe
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

# Login Page
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check validation
        if User.objects.filter(username=username).exists() == False:
            messages.error(request, "Invalid Username.")
            return redirect("/login/")
        
        #check auth
        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request, "Invalid Credential.")
            return redirect("/login/")
        else:
            #session start
            login(request,user)
            return redirect('/receipes/')
        
    return render(request, 'login.html')


# Register Page
def register_page(request):
    if request.method == "POST":
        first_name  = request.POST.get('first_name')
        last_name   = request.POST.get('last_name')
        username    = request.POST.get('username')
        password    = request.POST.get('password')
        
        #check validation
        user = User.objects.filter(username=username)
        if(user.exists()):
            messages.add_message(request, messages.INFO, "User already exists.")
            return redirect("/register/")

        #save data
        user = User.objects.create(first_name=first_name,last_name=last_name,username=username,password=password)

        #Password Encrypt
        user.set_password(password)
        user.save()

        messages.add_message(request, messages.SUCCESS, "User account created successfully.")

        #redirect 
        return redirect("/register/")

    return render(request, 'register.html')


#logout
def logout_page(request):
    logout(request)
    return redirect('/login/')

# For Search Query
from django.db.models import Q,Sum # type: ignore

#get all student
def get_students(request):
    queryset = Student.objects.all()
    ## search logic
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains=search) | 
            Q(department__department__icontains=search) | 
            Q(student_id__student_id__icontains=search) | 
            Q(student_email__icontains=search) | 
            Q(student_age__icontains=search)
        
        )

    paginator = Paginator(queryset, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    return render(request,'reports/students.html',{"queryset": page_obj})

#show marks or report card
#from .seed import generate_report_card
def see_marks(request,student_id):
    #generate_report_card()

    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks=Sum('marks'))
    
    #find rank :  this method is wrong : store in table : manual process
    # current_rank = -1
    # ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
    # i=1
    # for rank in ranks:
    #     if student_id == rank.student_id.student_id:
    #         current_rank = i
    #         break

    #     i = i+1

    return render(request,'reports/see_marks.html',{"queryset": queryset,'total_marks':total_marks})
