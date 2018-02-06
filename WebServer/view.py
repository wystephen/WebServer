# -*- coding:utf-8 -*-
# carete by steve at  2018 / 02 / 06　3:57 PM
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request,"index.html")
    # return HttpResponse("Hello world ! ")