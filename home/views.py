from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import contact_us
from blog.models import Post
from . forms import contacts_form
from django.contrib import messages

# Create your views here.
def home(request):
    posts =  Post.objects.all()
    context = {'posts':posts}
    return render(request,'home/home.html',context)

# for contacts page
def contacts(request):
    form = contacts_form()
    query = contact_us.objects.all()
    context = {'form':form,'query':query}
    messages.error(request,' Please enter valid information!') # messages ko value types are:- error, success, warning
    return render(request,'home/contacts.html',context)

# for getting contacts page post data
def getting_contacts(request):
    if request.method=='POST':
        faram = contacts_form(request.POST)
        if faram.is_valid():
            new_data = contact_us(name=request.POST['name'],phone_no=request.POST['phone_no'],email=request.POST['email'],contact_issue=request.POST['contact_issue'])
            new_data.save()
            print(new_data)
            return redirect('contacts')
    else:
        faram = contacts_form()


def about(request):
    messages.success(request,'this is about')
    return render(request,'home/about.html')

def search(request):
    searchbox_value=request.GET['search']
    database_value =Post.objects.filter(title__icontains=searchbox_value)
    context = {'database_value':database_value}
    return render(request,'home/search.html',context)
