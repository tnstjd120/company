from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

# index.html 
class View_Controls(View):
    def get(self, request):

        data = {
            "product":[
            {"img": "TLLRo8_20200423015341300086.jpg", "name": "쪽파", "price": 150},
            {"img": "https://s3.ap-northeast-2.amazonaws.com/image.gawooplus.com/eeyo/TLLRo8_20200423015408776257.jpg", "name": "깻잎", "price": 3000},
            {"img": "https://s3.ap-northeast-2.amazonaws.com/image.gawooplus.com/eeyo/TLLRo8_20200423015431569066.jpg", "name": "양상추", "price": 5000},
            {"img": "https://s3.ap-northeast-2.amazonaws.com/image.gawooplus.com/eeyo/TLLRo8_20200423015509928747.jpg", "name": "양배추", "price": 6000},
            {"img": "https://s3.ap-northeast-2.amazonaws.com/image.gawooplus.com/eeyo/TLLRo8_20200423015529053937.jpg", "name": "홍고추", "price": 1000},
            {"img": "https://s3.ap-northeast-2.amazonaws.com/image.gawooplus.com/eeyo/TLLRo8_20200423015554407678.jpg", "name": "애호박", "price": 8000},
            {"img": "https://s3.ap-northeast-2.amazonaws.com/image.gawooplus.com/eeyo/TLLRo8_20200423015611523329.jpg", "name": "대파1단", "price": 7000},
            {"img": "https://s3.ap-northeast-2.amazonaws.com/image.gawooplus.com/eeyo/TLLRo8_20200423015628888902.jpg", "name": "상추300g", "price": 4500},
            {"img": "https://s3.ap-northeast-2.amazonaws.com/image.gawooplus.com/eeyo/TLLRo8_20200423015705496887.jpg", "name": "상추", "price": 3500},
            {"img": "https://s3.ap-northeast-2.amazonaws.com/image.gawooplus.com/eeyo/TLLRo8_20200423015740145723.jpg", "name": "감자", "price": 4000}
            ]
        }

        context = {
            'product_data' : data
        }

        return render(request, 'app_main/index.html', context)

class View_Controls_Test(View):
    def get(self, request):

        context ={
            'name':request.GET.get('name',''),
            'img':request.GET.get('img',''),
            'price':request.GET.get('price','')
        }

        return render(request, 'app_main/menu-share.html', context)

# import json
# with open('templates/app_main/eeyo.json') as json_file:
#     json_data = json.load(json_file)

#     product = json_data["product"]

    