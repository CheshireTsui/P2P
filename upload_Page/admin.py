#_*_coding:utf-8 _*_
from django.contrib import admin
from upload_Page.models import ExcelFile, Rows

# Register your models here.
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "upload_time", 
    )
    list_filter = (
        "upload_time",
    )
    ordering = ("-id",)


class RowsAdmin(admin.ModelAdmin):
    list_display = (
        "id", "content", "belong_to", 
    )
    ordering = ("-id",)



admin.site.register(ExcelFile, ExcelFileAdmin)
admin.site.register(Rows, RowsAdmin)