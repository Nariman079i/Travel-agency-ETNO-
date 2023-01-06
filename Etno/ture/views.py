from django.shortcuts import render,HttpResponse
from .models import *


def gallery(request):
    context = dict()
    context['imgs'] = Image.objects.all()
    return render(request, 'ture/gallery.html' , context=context )


def main_page(request):
    context = dict()
    context['about_info'] = """Туристический сайт ЭТНО. Дагестан, республика на северо-востоке Кавказа, расположенная на территории Северного Кавказа и Северо-Восточного Казахстана.
Дагестана – это республика, которая на протяжении многих лет привлекает к себе внимание туристов со всего мира.
Здесь есть на что посмотреть, например, исторические места, природные достопримечательности, музеи, памятники архитектуры, а также горные и морские курорты.
Так что, если вы любите активный отдых, то тур в Дагестан, это то, что вам нужно."""
    context['tours'] = Tour.objects.all()
    context['attractions'] = Attraction.objects.all()
    return render(request, 'ture/index.html' , context=context)
    

def tour(request,id):
    context = dict()
    context['tour'] = Tour.objects.get(pk=id)
    context['tour_imgs'] = Image.objects.filter(tour_id_id = id)[:6]
    context['tour_attractions'] = Attraction.objects.filter(tour_id_id = id)
    
    return render(request , 'ture/ture.html' , context=context)

def about(request):
    context = dict()
    context['about_info'] = """Туристический сайт ЭТНО. Дагестан, республика на северо-востоке Кавказа, расположенная на территории Северного Кавказа и Северо-Восточного Казахстана.
Дагестана – это республика, которая на протяжении многих лет привлекает к себе внимание туристов со всего мира.
Здесь есть на что посмотреть, например, исторические места, природные достопримечательности, музеи, памятники архитектуры, а также горные и морские курорты.
Так что, если вы любите активный отдых, то тур в Дагестан, это то, что вам нужно."""
    context['tours'] = Tour.objects.all().count()
    context['attractions'] = Attraction.objects.all().count()
    return render(request, 'ture/about.html', context=context)


