from django.contrib import admin
from member.models import Member
from board.models import Board
# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
  list_display = ['bno', 'btitle', 'bgroup', 'bdate']