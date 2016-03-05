# _*_coding:utf-8 _*_
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from upload_Page.models import *
import json

def home(request):
    ls = ExcelFile.objects.all().order_by('-id')
    return render_to_response("index.html", {"ls": ls, })
