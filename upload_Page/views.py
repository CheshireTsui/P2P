#_*_coding:utf-8 _*_
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from upload_Page.models import *
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

@csrf_exempt
def upload(request):
    if request.method == "POST":
        try:
            xls = ExcelFile()
            if request.POST["fname"] != '': 
                xls.name = request.POST["fname"]
                print '[*] NAME: ' + request.POST["fname"]
            xls.file = request.FILES['file']
            xls.save()
            return HttpResponseRedirect("/show?num=%d"%xls.id)
        except Exception, e:
            raise Http404
    return render_to_response("upload_page.html")
