from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from. forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import get_user_model
from .decorators import unauthenticated_user,allowed_users

from django.contrib.auth.decorators import login_required
from datetime import date
import json
from django.db.models import Count, Q
import xlwt
from django.contrib.auth.models import User
from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
import os
import csv

# Create your views here.

##FUNCTIONS TO GENERATE IDs###########

def QMS_no():
   return str("Comp-QP-"+(date.today()).strftime("%d%m%Y"))+str(randint(0, 999))

####################################################################################
def dateValidation(request):
    return render(request,'validation.html')


@login_required(login_url='login')
def maintenance(request):
              
    form=mentainance()
                          
    if request.method=="POST":

        request.POST=request.POST.copy()
        request.POST['entered_by'] = request.user
        request.POST['date_today']=date.today()
        
        form=mentainance(request.POST)
                        
        if form.is_valid():

                
            form.save()
            return redirect('/')
            
            
          
        
    context={'form':form}
    return render(request,'maintenance.html',context)






@login_required(login_url='login')
def cali(request):
              
    form=calibration()
                          
    if request.method=="POST":

        request.POST=request.POST.copy()
        request.POST['entered_by'] = request.user
        request.POST['date_today']=date.today()
        
        form=calibration(request.POST)
                        
        if form.is_valid():

                
            form.save()
            return redirect('/')
            
            
          
        
    context={'form':form}
    return render(request,'calibration.html',context)




@login_required(login_url='login')
def doc_manager(request):

    form=document_manager()
    

    
    if request.method=="POST":

        request.POST=request.POST.copy()
        request.POST['entered_by'] = request.user
        request.POST['date_today']=date.today()
        
           
        form = document_manager(request.POST)
        print("doc manager",request.POST)
        
         
            
        
        if form.is_valid():
           
            
            form.save()
           
            return redirect('/')
            
            
        form=document_manager(request.POST)
        context={'form':form}
        
        return render(request,'document_manager.html',context)
           
        
    context={'form':form}
    return render(request,'document_manager.html',context)



@login_required(login_url='login')
def qms_planner(request):
              
    form=qmsplanner(initial={'planner_number': QMS_no()})
                          
    if request.method=="POST":

        request.POST=request.POST.copy()
        request.POST['entered_by'] = request.user
        request.POST['date_today']=date.today()
        request.POST['status'] = 5
        
        form=qmsplanner(request.POST)
                        
        if form.is_valid():

                
            form.save()
            return redirect('/')
            
            
          
        
    context={'form':form}
    return render(request,'qmsplanner.html',context)

@login_required(login_url='login')
def qms_pending(request):
    pendingcar=mod9001_qmsplanner.objects.filter(status='5') #get all qms pending approval    
    context={'pendingcar':pendingcar} 
    return render(request,'qms_pending.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['supervisor'])
def approve_qms(request,pk_test):
    pending_risk=mod9001_qmsplanner.objects.get(planner_number=pk_test)
    form=ApproveQMS(instance=pending_risk)

    if request.method=="POST":

            
            
            request.POST=request.POST.copy()
            request.POST['approved_by']=request.user
            request.POST['approval_date']=date.today()                      

            form=ApproveQMS(request.POST, instance=pending_risk)
            if form.is_valid():
                form.save()
                return redirect('/qms_pending/')

    context={'form':form}  


    return render(request,'qms_approve.html',context)



#####################################QMS VERIFICATION##############################
@login_required(login_url='login')
def opp_7daysToExpiryview(request,pk_test):

    products=mod9001_qmsplanner.objects.filter(planner_number=pk_test)
    return render(request,'qms_view_7_days_To_expiry.html',{'products':products})




def CARnumbers_7days_expire(*x):
    date_str = x[0]
    date_object = datetime.strptime(date_str, '%m/%d/%Y').date()
    delta =date_object - date.today()
    return delta.days


@login_required(login_url='login')
def qms_due(request):
    carExpire7days=mod9001_qmsplanner.objects.filter(status=1).filter(~Q(qmsstatus=1))
    thislist = []
    for i in carExpire7days:
        w=i.end
        t=w.strftime('%m/%d/%Y')
        if CARnumbers_7days_expire(t)<0:
            thislist.append(i.planner_number)
    thisdict={}
    i=0
    #creat a dictionary for all car numbers for display
    for x in thislist:
        while i<len(thislist):
            y = str(i)
            thisdict["planner_number"+y] = thislist[i]
            i+=1

        
    return render(request,'qms_due.html',{'thisdict':thisdict})



@login_required(login_url='login')
def qms_7daysToExpiryview(request,pk_test):

    products=mod9001_qmsplanner.objects.filter(planner_number=pk_test)
    return render(request,'qms_view_7_days_To_expiry.html',{'products':products})

@allowed_users(allowed_roles=['supervisor'])
def verify_qms(request,pk_test):
    open_car=mod9001_qmsplanner.objects.get(planner_number=pk_test)
    form=VerifyQMS(instance=open_car)
    if request.method=="POST":
            print("request.POST['qmsstatus']",request.POST['qmsstatus'])
            
            if request.POST['qmsstatus'] =="Rejected":
                request.POST=request.POST.copy()
                request.POST['status'] = 5 #requires approval first before next verification
                request.POST['verification']=2 #default verifiaction to Not effective
                print("request", request.POST)
            
            elif request.POST['qmsstatus'] == '1':
                print("request.POST['qmsstatus']",request.POST['qmsstatus'])
                request.POST=request.POST.copy()
                request.POST['status'] = 1 # keep status approved
            
            else:
                request.POST=request.POST.copy()






            form=VerifyQMS(request.POST, instance=open_car)
            if form.is_valid():
                form.save()
                return redirect('/qms_due/')

    context={'form':form}  


    return render(request,'qms_verify.html',context)
