from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(document_standard)
admin.site.register(document_type)
admin.site.register(document_format)
admin.site.register(document_location)
admin.site.register(mod9001_document_manager)
admin.site.register(maintenance)
admin.site.register(schedule)
admin.site.register(equipment)
admin.site.register(mod9001_qmsplanner)
admin.site.register(status)
admin.site.register(prod_description)
admin.site.register(qmsstatus)

admin.site.register(noteffective)

admin.site.register(train_status)
admin.site.register(train_objective)
admin.site.register(train_desc)


