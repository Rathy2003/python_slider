from django.shortcuts import render

from models.model import Slider


def index(request):
    slider_list = Slider.objects.order_by("order")
    total_slider = slider_list.count()
    return render(request,"home/index.html",{
        "slider_list": slider_list,
        "total_slider_count": total_slider,
        "total_slider": list(range(total_slider)),
    })