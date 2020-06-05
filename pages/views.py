from django.http import HttpResponseRedirect
# from django.shortcuts import redirect
from django.shortcuts import render
from .models import Soapprod, Staffrec, Creamsales
from .forms import StaffrecForm, SoapprodForm, CreamprodForm, CreamsalesForm
from django.views.generic import TemplateView

def Basep_view (request,*args, **kwargs):
     return render(request,"basep.html", {})

from pages.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):

    return render(request,'index.html',{})
def appindex (request):

    return render(request,'appindex.html',{})

def shop(request):
    return render(request,'shop.html',{})

@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout (request):
    logout (request)
    return HttpResponseRedirect(reverse('index'))
def register (request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


from django.http import JsonResponse
from pages.models import Soapprod,Creamprod
from django.core import serializers

def dashboard_with_pivot (request):
    return render(request, 'dashboard_with_pivot.html', {})
def pivot_data(request):
    dataset = Soapprod.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def soapprod_list (request):
    context = {'soapprod_list': Soapprod.objects.all()}
    return render(request, "soapprod_list.html", context)

from django.db.models import Sum
from django.db.models import Avg

def soapprod_form (request, id=0):
    a = Soapprod.objects.aggregate(Sum('Serial_White_Guava'))
    b = Soapprod.objects.aggregate(Sum('Serial_White_Premium'))
    c = Soapprod.objects.aggregate(Sum('Soft_Flower_Body_Wash'))
    d = Soapprod.objects.aggregate(Sum('Soft_Flower_Fresh'))
    e = Soapprod.objects.aggregate(Sum('Soft_Flower_Orange_Lightening'))
    f = Soapprod.objects.aggregate(Sum('Soft_Flower_Papaya_Extract'))
    g = Soapprod.objects.aggregate(Sum('Soft_Flower_Extra_Lightening'))
    h = Soapprod.objects.aggregate(Sum('Soft_Flower_Carot_Lightening'))
    i = Soapprod.objects.aggregate(Sum('Serial_White_Papaya_4in1'))

    if request.method == "GET":
        if id == 0:
            form = SoapprodForm()
        else:
            soapprod = Soapprod.objects.get(pk=id)
            form = SoapprodForm (instance=soapprod)
        return render(request, "soapprod_form.html", {'form': form, 'b':b,'a':a,'c':c,'d':d, 'e': e, 'f':f,'g':g,'h':h,'i':i})
    else:
        if id == 0:
            form = SoapprodForm(request.POST)
        else:
            soapprod = Soapprod.objects.get(pk=id)
            form = SoapprodForm(request.POST,instance= soapprod)
        if form.is_valid():
            form.save()

        return render(request, "soapprod_form.html", {'form': form})

from django.shortcuts import render, redirect   

def creamprod_list (request):
    context = {'creamprod_list': Creamprod.objects.all()}
    return render(request, "cream/creamprod_list.html", context)

def creamprod_form (request, id=0):
    aa = Creamprod.objects.aggregate(Sum('Serial_White_ExLM'))
    bb = Creamprod.objects.aggregate(Sum('Serial_White_Gold_SWM'))
    cc = Creamprod.objects.aggregate(Sum('Soft_Flower_LL'))
    dd = Creamprod.objects.aggregate(Sum('Soft_Flower_FC'))
  
    if request.method == "GET":
        if id == 0:
            form = CreamprodForm()
        else:
            creamprod = Creamprod.objects.get(pk=id)
            form = CreamprodForm (instance=creamprod)
        return render(request, "creamprod_form.html", {'form': form,'bb':bb,'aa':aa,'cc':cc,'dd':dd})
    else:
        if id == 0:
            form = CreamprodForm(request.POST)
    
        else:
            creamprod = Creamprod.objects.get(pk=id)
            form = CreamprodForm(request.POST,instance= creamprod)
        if form.is_valid():
            form.save()
        return render(request, "creamprod_form.html", {'form': form})
def creamprod_delete (request,id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Creamprod, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        # return HttpResponseRedirect("/") 
        return render(request, "cream/creamprod_list.html", context)
  
    # return render(request, "delete_view.html", context)
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
def soapprod_delete (request,id): 
 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Soapprod, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        # return HttpResponseRedirect("/") 
        return render(request, "soapprod_list.html", context)
  
    # return render(request, "delete_view.html", context)

from pages.forms import StaffrecForm , SoapsalesForm 
from .models import Staffrec, Soapsales  

def staffrec_list (request):
    context = {'staffrec_list': Staffrec.objects.all()}
    return render(request, "staff/staffrec_list.html", context)

def staffrec_form (request, staff_id=0):
    if request.method == "GET":
        if staff_id == 0:
            form = StaffrecForm()
        else:
            staffrec = Staffrec.objects.get(pk=staff_id)
            form = StaffrecForm (instance=staffrec)
        return render(request, "staff/staffrec_form.html", {'form': form})
    else:
        if staff_id == 0:
            form = StaffrecForm(request.POST)
    
        else:
            staffrec = Staffrec.objects.get(pk=staff_id)
            form = StaffrecForm(request.POST,instance= staffrec)
        if form.is_valid():
            form.save()
        return render(request, "staff/staffrec_form.html", {'form': form})

def staffrec_delete (request,staff_id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Staffrec, pk = staff_id) 
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        # return HttpResponseRedirect("/") 
        return render(request, "staff/staffrec_list.html", context)

def soapsales_list (request):
    context = {'soapsales_list': Soapsales.objects.all()}
    return render(request, "soapsales/soapsales_list.html", context)

def soapsales_form (request, id=0):
    aas = Soapsales.objects.aggregate(Sum('Serial_White_Guava'))
    bs = Soapsales.objects.aggregate(Sum('Serial_White_Premium'))
    cs = Soapsales.objects.aggregate(Sum('Soft_Flower_Body_Wash'))
    ds = Soapprod.objects.aggregate(Sum('Soft_Flower_Fresh'))
    es = Soapsales.objects.aggregate(Sum('Soft_Flower_Orange_Lightening'))
    fs = Soapsales.objects.aggregate(Sum('Soft_Flower_Papaya_Extract'))
    gs = Soapsales.objects.aggregate(Sum('Soft_Flower_Extra_Lightening'))
    hs = Soapsales.objects.aggregate(Sum('Soft_Flower_Carot_Lightening'))
    iis = Soapsales.objects.aggregate(Sum('Serial_White_Papaya_4in1'))
    
    if request.method == "GET":
        if id == 0:
            form = SoapsalesForm()
        else:
            soapprod = Soapsales.objects.get(pk=id)
            form = SoapsalesForm (instance=soapprod)
        return render(request, "soapsales/soapsales_form.html", {'form': form, 'bs':bs,'aas':aas,'cs':cs,'ds':ds, 'es': es, 'fs':fs,'gs':gs,'hs':hs,'iis':iis})
    else:
        if id == 0:
            form = SoapsalesForm(request.POST)
        else:
            soapsales = Soapsales.objects.get(pk=id)
            form = SoapsalesForm(request.POST,instance= soapsales)
        if form.is_valid():
            form.save()

        return render(request, "soapsales/soapsales_form.html", {'form': form})
def soapsales_delete (request,id): 
    context ={} 

    obj = get_object_or_404(Staffrec, pk = id) 
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 

        return render(request, "soapsales/soapsales_list.html", context)


def creamsales_list (request):
    context = {'creamsales_list': Creamsales.objects.all()}
    return render(request, "cream/creamsales_list.html", context)

def creamsales_form (request, id=0):
    aacs = Creamsales.objects.aggregate(Sum('Serial_White_ExLM'))
    bbcs = Creamsales.objects.aggregate(Sum('Serial_White_Gold_SWM'))
    cccs = Creamsales.objects.aggregate(Sum('Soft_Flower_LL'))
    ddcs = Creamsales.objects.aggregate(Sum('Soft_Flower_FC'))
    # if Creamsales.objects.filter(cream_marketer_status='groupc'):
        # aacs = Creamsales.objects.all().aggregate(product('Serial_White_ExLM')*3000) 
        # Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks') * 2)
    if request.method == "GET":
        if id == 0:
            form = CreamsalesForm()
        else:
            creamsales = Creamsales.objects.get(pk=id)
            form = CreamsalesForm (instance=creamsales)
        
        return render(request, "cream/creamsales_form.html", {'form': form,'bbcs':bbcs,'aacs':aacs,'cccs':cccs,'ddcs':ddcs})
    else:
        if id == 0:
            form = CreamsalesForm(request.POST)
    
        else:
            creamsales = Creamsales.objects.get(pk=id)
            form = CreamsalesForm(request.POST,instance= creamsales)
        if form.is_valid():
            form.save()
        return render(request, "cream/creamsales_form.html", {'form': form})
        
def creamsales_delete (request,id): 
    context ={} 
    obj = get_object_or_404(Creamsales, id = id) 
    if request.method =="POST": 
        obj.delete() 
        return render(request, "cream/creamsales_list.html", context)