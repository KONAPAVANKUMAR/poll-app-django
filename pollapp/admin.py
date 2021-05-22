from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(PollModel)
class PollModelAdmin(admin.ModelAdmin):
    list_display = ("question","upvotes","downvotes")
    def get_ordering(self, request):
        return ['id']