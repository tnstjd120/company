from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

class View_Controls(View):
    def get(self,request):

        return render(request, 'app_main/index.html')
