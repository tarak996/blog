from django.contrib import admin
from . models import modelBlog
# Register your models here.
@admin.register(modelBlog)
class AdminmodelBlog(admin.ModelAdmin):
    list_display = ['id','title','summary']