from django.shortcuts import render
from django.contrib import messages
from .models import Carousel
from .forms import CarouselModelForm

# Create your views here.
def index(request):
  context = dict()
  context ['images'] = Carousel.objects.filter(status="published")
  return render(request, 'home/index.html', context)
  

def carousel_list(request):
  context = dict()
  context['carousel'] = Carousel.objects.all() 
  return render(request, 'manage/carousel_list.html', context)


def carousel_update(request, pk):
  context = dict()
  context['item'] = Carousel.objects.get(pk=pk)
  return render(request, 'manage/carousel_create.html', context)


def carousel_create(request):
  context = dict()
  context['form'] = CarouselModelForm()
  #item = Carousel.objects.first()
  #context['form'] = CarouselModelForm(instance=item)
  if request.method == "POST":
    print (request.POST)
    print (request.FILES['cover_image'])
    #carousel = Carousel.objects.create(
    #  title=request.POST.get('title')
    #)
    form = CarouselModelForm(request.POST, request.FILES)
    print(form)
    if form.is_valid():
      form.save()
    messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
  return render(request, 'manage/carousel_create.html', context)  
