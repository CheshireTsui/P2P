# _*_coding:utf-8 _*_
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, get_object_or_404
from upload_Page.models import *
import json

# Create your views here.
def show(request):
    try:
        xls = ExcelFile.objects.get(id=int(request.GET["num"]))
        name = xls.name
        ls = xls.rows_set.all()
        ls2 = list()
        for i in ls:
            s = json.loads(i.content)
            ls2.append(s)
        return render_to_response("show_page.html", {'rows': ls2, 'name': name, })
    except Exception, e:
        raise Http404