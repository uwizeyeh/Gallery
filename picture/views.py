from django.shortcuts import render
from django.http  import HttpResponse
from django.db import models
from .models import Image,Location


def home(request):
    pics = Image.get_all()
    return render(request,'index.html',{"pics":pics})

def search_result(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched = Image.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{"message":message,"searched": searched})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def image(request,image_id):
    image = Image.objects.get(id = image_id)
    return render(request,"info.html", {"image":image})

def location(request,location_id):
    try:
        locations= Location.objects.get(id=location_id)
        image = Image.objects.filter(location=location_id)
    except:
        raise Http404()
    return render(request,"location.html", {"locations":locations,'image':image})
