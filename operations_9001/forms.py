from django.forms import ModelForm,TextInput,NumberInput,RadioSelect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'



class document_manager(ModelForm):
    
    
    class Meta:
        model = mod9001_document_manager 
        fields = '__all__'
        widgets={'Origin': RadioSelect(),'document_date':DateInput()}

class calibration(ModelForm):
    
    
    class Meta:
        model = mod9001_calibration 
        fields = '__all__'
        widgets={'calibration_date':DateInput()}

class mentainance(ModelForm):
    
    
    class Meta:
        model = maintenance 
        fields = '__all__'
        widgets={'date_today':DateInput(),'date':DateInput()}

class qmsplanner(ModelForm):



    
    
    class Meta:
        model = mod9001_qmsplanner 
        fields = ['planner_number','plan_date','planner','start','end','description','details','status']
        widgets={'plan_date':DateInput(),'start':DateInput(),'end':DateInput(),'due':DateInput()}

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start")
        end_date = cleaned_data.get("end")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")

class ApproveQMS(ModelForm):

    
    
    class Meta:
        model = mod9001_qmsplanner 
        #fields = '__all__'
        fields=['status','rejected','approval_date','approved_by','approval_date']
        widgets={'status': RadioSelect(),'approval_date':DateInput()}      

class VerifyQMS(ModelForm):
    
    class Meta:
        model = mod9001_qmsplanner 
        #fields = '__all__'
        fields=['verification','verification_status','verification_failed','qmsstatus','scheduled','completion']
        widgets={'completion':DateInput(),'scheduled':DateInput()}   