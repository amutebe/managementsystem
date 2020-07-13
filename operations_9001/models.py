from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from random import randint
from django import forms
from django.conf import settings

# Create your models here.
def car_no():
    now = datetime.now()
    t=(now.strftime('%H'))+(now.strftime('%M'))+(now.strftime('%S'))
    return str((date.today()).strftime("%d%m%Y"))+str(randint(0, 999))

class document_standard(models.Model):

    description=models.CharField("Standard", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class document_type(models.Model):

    description=models.CharField("Document type", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class document_format(models.Model):

    description=models.CharField("Document format", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description
class document_location(models.Model):

    description=models.CharField("Document location", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class equipment(models.Model):

    description=models.CharField("Equipment", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class schedule(models.Model):

    description=models.CharField("Maintenence schedule", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class mod9001_document_manager(models.Model):
    document_date=models.DateField("Date:")
    document_number=models.CharField("Document no.:",max_length=200,default="TEGA-Q-"+car_no(),primary_key=True)
    standard= models.ForeignKey('document_standard',on_delete=models.CASCADE,verbose_name='Standard:',related_name='standard')
    Origin=(('1','Internal'),('2','External'))
    origin=models.CharField(max_length=200,null=True, choices=Origin)
    doc_type= models.ForeignKey('document_type',on_delete=models.CASCADE,verbose_name='Document Type:',related_name='type')
    document_id =models.TextField("Document ID:",null=True,blank=True, help_text='Ref No.')
    doc_name =models.TextField("Document Name:",null=True,blank=True, help_text='Document Name')

    clause =models.TextField("Document ID:",null=True,blank=True, help_text='Document ID')
    format= models.ForeignKey('document_format',on_delete=models.CASCADE,verbose_name='Format:',related_name='format')
    version =models.TextField("Version No:",null=True,blank=True, help_text='Version')
    location= models.ForeignKey('document_location',on_delete=models.CASCADE,verbose_name='Location:',related_name='location')
    owner= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Owner:',related_name='owner')
    Retention=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','>5'))
    retention=models.CharField(max_length=200,null=True, choices=Retention)
    Status=(('1','Current'),('2','Obsolete'))
    status=models.CharField(max_length=200,null=True, choices=Status)
    document = models.FileField("Please upload relevant document",upload_to ='uploads/',null=True,blank=True)

class mod9001_calibration(models.Model):
    calibration_date=models.DateField("Date:")
    calibration_number=models.CharField("Calibration no.:",max_length=200,default="TEGA-C-"+car_no(),primary_key=True)
    type =models.TextField("Calibration type:",null=True,blank=True, help_text='Calibration type')
    device_id =models.TextField("Device ID:",null=True,blank=True, help_text='Device ID')
    manufacturer =models.TextField("Manufacturer:",null=True,blank=True, help_text='Device Manufacturer')
    range =models.TextField("Range:",null=True,blank=True, help_text='Range')
    calibrated_by= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Done by:',related_name='doneby')
    standard= models.ForeignKey('document_standard',on_delete=models.CASCADE,verbose_name='Standard:',related_name='calstandard')
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='cal_entered_by',on_delete=models.SET_NULL)
    date_today=models.DateField("Date created:",default=datetime.now)

class maintenance(models.Model):
    maintenance_number=models.CharField("Maintenance no.:",max_length=200,default="TEGA-M-"+car_no(),primary_key=True)
    date_today=models.DateField("Date:")
    equipment= models.ForeignKey('equipment',on_delete=models.CASCADE,verbose_name='Equipment:',related_name='Equipment')
    id =models.TextField("ID:",null=True,blank=True, help_text='Enter ID or Serial #')
    manufacturer =models.TextField("Manufacturer:",null=True,blank=True, help_text='Manufacturer')
    date=models.DateField("Manufacture Date:")
    location =models.TextField("Location:",null=True,blank=True, help_text='Location')
    user= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='user:',related_name='user')
    schedule= models.ForeignKey('Schedule',on_delete=models.CASCADE,verbose_name='Schedule:',related_name='Schedule')
    detials =models.TextField("Details:",null=True,blank=True, help_text='Details')
    maintenanceby=(('1','Internal technician'),('2','External technician'))
    maintenanceby=models.CharField(max_length=200,null=False, choices=maintenanceby)
    name =models.TextField("Name of Techncian:",null=True,blank=True, help_text='Name')
    parts =models.TextField("Parts replaced:",null=True,blank=True, help_text='Parts replaced')
    notes =models.TextField("Notes:",null=True,blank=True, help_text='Notes')
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='maintenance_entered_by',on_delete=models.SET_NULL)
    date_today=models.DateField("Date created:",default=datetime.now)

class prod_description(models.Model):

    description=models.CharField("Program Description", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description 


class status(models.Model):

    description=models.CharField("Status", max_length=50,null=True,blank=True,)
    def __str__(self):
        return self.description 

class qmsstatus(models.Model):

    description=models.CharField("Status", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description


class noteffective(models.Model):
    description=models.CharField("Reason not effective", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description





class mod9001_qmsplanner(models.Model):
    planner_number=models.CharField("Planner no.:",max_length=200,default="Comp-QP-"+car_no(),primary_key=True)
    plan_date=models.DateField("Plan Date:")
    planner = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='qms_by',on_delete=models.SET_NULL)
    start=models.DateField("Start Date:")
    end=models.DateField("End Date:")
    description= models.ForeignKey('prod_description',on_delete=models.CASCADE,verbose_name='Program description:',related_name='progdesc')
    details =models.TextField("Additional Description:",null=True,blank=True, help_text='Additional Description')
    status=models.ForeignKey('issues_9001.approval_status', on_delete=models.SET_NULL,verbose_name='Status:',null=True,blank=True)
    rejected=models.TextField("Reason for rejecting:",null=True,blank=True, help_text='If rejected, please give a reason')
    approval_date=models.DateField("Date Approved:",null=True,blank=True)
    approved_by=models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='qmsApprov_by',on_delete=models.SET_NULL)
    verification=models.ForeignKey('issues_9001.RISK_OPPverification', on_delete=models.SET_NULL,verbose_name='Verification:',null=True,blank=True)
    verification_status=models.CharField(max_length=200, null=True,blank=True)
    verification_failed=models.TextField("Reason for rejecting:",null=True,blank=True, help_text='If rejected, please give a reason')
    due=models.DateField("When:",null=True,blank=True)
    qmsstatus=models.ForeignKey(qmsstatus, on_delete=models.SET_NULL,null=True,verbose_name='Verification Status:')
    completion=models.DateField("Completion Date:",null=True,blank=True)
    scheduled=models.DateField("Rescheduled Date:",null=True,blank=True)
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='qms_entered_by',on_delete=models.SET_NULL)
    date_today=models.DateField("Date created:",default=datetime.now)


class mod9001_trainingregister(models.Model):
    training_number=models.CharField("Training no.:",max_length=200,default="Comp-TR-"+car_no(),primary_key=True)
    train_date=models.DateField("Training Date:",null=True)
    Nature=(('1','Planned'),('2','Not Planned'))
    nature=models.CharField(max_length=200,null=True, choices=Nature)
    training_desc=models.TextField("Training Description:",null=True,blank=True)
    trainingplanid=models.TextField("Training Plan ID:",null=True,blank=True)
    training=models.TextField("Training:",null=True,blank=True)
    location=models.TextField("Location:",null=True,blank=True)
    trainer = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='reg_by',on_delete=models.SET_NULL)
    trainee=models.TextField("Trainee:",null=True,blank=True)
    tainee_dept=models.ForeignKey('accounts.Department', on_delete=models.CASCADE,verbose_name='Trainee Department ID:',related_name='traineeDepartment')
    completion_date=models.DateField("Completion Date:")
    yesno=(('1','Yes'),('2','No'))
    job=models.CharField("Employee Job performance level has raised ",max_length=200,null=True, choices=yesno)
    skills=models.CharField("Training skills applied by trainee ",max_length=200,null=True, choices=yesno)
    indicators=models.CharField("Indicators exist that prove the employee benefited from the acquired skills in this Training course",max_length=200,null=True, choices=yesno)
    able=models.CharField("Employee Able to train others",max_length=200,null=True, choices=yesno)
    decision=(('1','Effective'),('2','Not Effective'))
    decision=models.CharField("Evaluation Decision:",max_length=200,null=True, choices=decision)
    reason=models.ForeignKey('noteffective', on_delete=models.CASCADE,verbose_name='If Not Effective, other reason:',related_name='noteffectreason',null=True)
    reasonother=models.TextField("If Not Effective, reason",null=True,blank=True)
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='training_entered_by',on_delete=models.SET_NULL)
    date_today=models.DateField("Date created:",default=datetime.now)







    












   
    
    
    
















