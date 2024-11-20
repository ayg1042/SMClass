from django.contrib import admin
from member.models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  # list_display = ['id', 'name', 'nicname', 'cdate']
  list_display = ['id']

admin.site.register(Member, MemberAdmin)