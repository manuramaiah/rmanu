from django.contrib import admin
from .models import Register_User
from .models import Fill_Form

@admin.register(Fill_Form)
class Fill_FormAdmin(admin.ModelAdmin):
    list_display = ['id','user_name', 'date_of_birth', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'district', 'branch', 'type_of_account', 'materials_provided']
admin.site.register(Register_User)
