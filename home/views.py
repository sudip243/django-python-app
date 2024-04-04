from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact
def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request,"index.html",context)
    # return HttpResponse("this is homepage") #this will send static request to to home page
def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"service.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phoneNo')
        desc = request.POST.get('desc')
        contact  = contact(name=name,email=email,phoneNo=phoneNo,desc=desc,date=datetime())
        contact.save()
    return render(request,"contact.html")