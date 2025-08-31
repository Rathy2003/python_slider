import datetime
import os.path
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from models.model import Slider


# Create your views here.
def dashboard(request):
    return render(request,"ecadmin/index.html")

def index(request):
    slider_list = Slider.objects.order_by("order")
    total_slider = slider_list.count()
    return render(request,"ecadmin/slider/index.html",{
        "slider_list": slider_list,
        "total_slider": total_slider,
    })

def create_slider(request):
    if request.method == "POST":
        title = request.POST.get("title")
        link = request.POST.get("link")
        image = request.FILES.get("image")
        description = request.POST.get("description")

        new_filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_" + image.name
        filepath = os.path.join(settings.MEDIA_ROOT,"sliders",new_filename)
        with open(filepath, "wb+") as f:
            for chunk in image.chunks():
                f.write(chunk)

        slider_order = Slider.objects.count()
        slider_item = Slider(title=title,link=link,description=description,order=slider_order+1,image="/media/sliders/"+new_filename)
        slider_item.save()
        messages.success(request,"Slider created successfully")
        return redirect("ecadmin.slider.create")
    return render(request, "ecadmin/slider/create.html")

def slider_move(request,id):
    if request.method == "POST":
        first_slider = Slider.objects.get(id=id)
        temp_first_slider_order = first_slider.order
        if request.POST.get("move_up") is not None:
            first_slider.order = first_slider.order - 1
        elif request.POST.get("move_down") is not None:
            first_slider.order = first_slider.order + 1
        second_slider = Slider.objects.get(order=first_slider.order)
        second_slider.order = temp_first_slider_order
        first_slider.save()
        second_slider.save()

    return redirect("ecadmin.slider")

def delete_slider(request):
    if request.method == "POST":
        slider_id = request.POST.get("id")
        temp_slider = Slider.objects.get(id=slider_id)
        temp_file_path = temp_slider.image.split("/")
        old_file = temp_file_path[3]
        filepath = os.path.join(settings.MEDIA_ROOT, "sliders", old_file)
        if os.path.isfile(filepath):
            os.remove(filepath)
        temp_slider.delete()
        data = {
            "success": True,
            "message": "Slider deleted successfully",
        }
        return JsonResponse(data)
    return redirect("ecadmin.slider")

def edit_slide(request,id):
    if request.method == "POST":
        title = request.POST.get("title")
        link = request.POST.get("link")
        image = request.FILES.get("image")
        description = request.POST.get("description")

        slider_item = Slider.objects.get(id=id)
        slider_item.title = title
        slider_item.link = link
        slider_item.description = description

        if image is not None:
            new_filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_" + image.name
            filepath = os.path.join(settings.MEDIA_ROOT, "sliders", new_filename)
            with open(filepath, "wb+") as f:
                for chunk in image.chunks():
                    f.write(chunk)
            slider_item.image = "/media/sliders/"+new_filename
        slider_item.save()

    slider_item = Slider.objects.get(id=id)
    return render(request,"ecadmin/slider/edit.html",{
        "slider_item": slider_item,
    })