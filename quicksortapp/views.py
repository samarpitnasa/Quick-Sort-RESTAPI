from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from . models import quicksort
import json
def get(request):
    lst=request.GET['listofno']
    a=lst.split(",")
    b=quicksort(a,0,len(a)-1)
    template = []
    for x in b:
        template.append(x)
    return HttpResponse(json.dumps(template), content_type='application/json')