from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('dateValidation/', views.dateValidation, name='dateValidation'),
path('doc_manager/', views.doc_manager, name='doc_manager'),
path('calibration/', views.cali, name='calibration'),
path('maintenance/', views.maintenance, name='maintenance'),
path('qms_planner/', views.qms_planner, name='qms_planner'),
path('qms_pending/', views.qms_pending, name='qms_pending'),
path('approve_qms/<str:pk_test>/',views.approve_qms,name="approve_qms"),
path('verify_qms/<str:pk_test>/',views.verify_qms,name="verify_qms"),
path('qms_due/',views.qms_due,name="qms_due"),
path('qms_7daysToExpiryview/<str:pk_test>/',views.qms_7daysToExpiryview,name="qms_7daysToExpiryview"),
path('training_register/', views.training_register, name='training_register'),
path('training_planner/', views.training_planner, name='training_planner'),


path('trainplanner_pending/', views.trainplanner_pending, name='trainplanner_pending'),
path('approve_trainplanner/<str:pk_test>/',views.approve_trainplanner,name="approve_trainplanner"),
path('training_due/',views.training_due,name="training_due"),
path('verify_training/<str:pk_test>/',views.verify_training,name="verify_training"),
path('training_7daysToExpiryview/<str:pk_test>/',views.training_7daysToExpiryview,name="training_7daysToExpiryview"),

path('incidentRegister/', views.incidentRegister, name='incidentRegister'),
path('ajax/load_description/', views.load_description, name='ajax_load_description'),
path('ajax/load_process/', views.load_process, name='ajax_load_process'),


path('customerRegister/', views.customerRegister, name='customerRegister'),
path('incidentRegisterStaff/', views.incidentRegisterStaff, name='incidentRegisterStaff'),


]