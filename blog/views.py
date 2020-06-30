from django.shortcuts import render

# Create your views here.

def blog(request):
    context = {
        'title':'Post'
    }
    return render(request,'blog/blog.html', context)