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

    
]