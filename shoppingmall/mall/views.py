from django.shortcuts import get_object_or_404, redirect, render
from .models import Mall
# Create your views here.
def home(request):
    malls = Mall.objects.all()
    return render(request, 'home.html', {'malls' : malls})

def detail(request, mall_id):
    mall = get_object_or_404(Mall, pk=mall_id)
    return render(request, 'detail.html', {'mall' : mall})

def create(request):
    if request.method == "POST":
        mall = Mall()
        mall.product = request.POST.get('product')
        mall.price = request.POST.get('price')
        mall.description = request.POST.get('description')

        mall.save()
        return redirect(request, 'home.html')
    return render(request, 'create.html')

def update(request, mall_id):
    mall = get_object_or_404(Mall, pk=mall_id)
    if request.method == "GET":

        return render(request, 'update.html', {"mall":mall})
    elif request.method == "POST":
        mall.product = request.POST.get('product')
        mall.price = request.POST.get('price')
        mall.description = request.POST.get('description')
        mall.save()
        return redirect('home')

def delete(request, mall_id):
    mall = get_object_or_404(Mall, pk=mall_id)
    pass
