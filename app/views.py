from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    if request.method == "POST":
     form = ImageForm(request.POST,request.FILES) #get images and store in form
     if form.is_valid():
      form.save()  #save into the db
    form = ImageForm()
    img = Image.objects.all()  #get all images from db
    return render(request,'app/home.html',{'img':img,'form':form}) #pass to the template