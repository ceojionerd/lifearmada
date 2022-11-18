from django.shortcuts import render, redirect

# Create your views here.

def home(request):

    # categories = Category.objects.all()[0:3]
    # featured = Post.objects.filter(featured=True)
    # latest = Post.objects.order_by('-timestamp')[0:3]

    context= {
        # 'object_list': featured,
        # 'latest': latest,
        # 'categories':categories,
    }

    return render(request, 'index.html', context)

def profile(request):

    return render(request, 'profile.html')

def about(request):

    return render(request, 'about-us.html')