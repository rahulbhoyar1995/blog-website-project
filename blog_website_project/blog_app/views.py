from django.shortcuts import render,redirect
from .forms import ContentForm
from django.contrib import messages
from .models import Content



def home(request):
    context = {
        'data' : Content.objects.all()
    }
    return render(request, 'blog_app/home.html',context)


def about(request):
    return render(request, 'blog_app/about.html', {'title': 'About'})


def content(request):
    form = ContentForm()
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Content saved successfully.")
        return redirect('blog-home')
    context  = {"form" : form}
    
    return render(request,'blog_app/content.html',context)


def politics_data(request):
    context = {
        'data' : Content.objects.filter(category="Politics")
    }

    return render(request, 'blog_app/politics.html',context)

    




    