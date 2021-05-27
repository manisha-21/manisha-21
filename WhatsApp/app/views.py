from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import Register

# Create your views here.
def home(request):
    data = Register.objects.all().order_by('-id')
    return render(request,"home.html",{'data':data})

def submit(request): 
    if request.method == "POST":
        name = request.POST['name']
        msg = request.POST['msg']
        Register(name=name, msg=msg).save()
        data = Register.objects.filter(name= name, msg=msg)
        data = Register.objects.all().order_by('-id')
        return render(request,"home.html",{'data':data,'name':name})

def show(request):
    data = Register.objects.all().order_by('-id')
    return render(request,"show.html",{'data':data})

def showdata(request):
    data = Register.objects.all().order_by('-id')
    data = list(data.values())
    return JsonResponse({'data':data})    
       