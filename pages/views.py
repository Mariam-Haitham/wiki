from django.shortcuts import render
from .models import Page


# Create your views here.
def page_list(request):
    
    context = {
            "page_list":  Page.objects.all(),
            }
    return render(request, "list.html", context)



def page_detail(request, page_id):
    
    context = {
            "page_detail":  Page.objects.get(id = page_id)
            }
    
    return render(request, "detail.html", context)