from django.shortcuts import render
from blog.models import blog, category

def home(request):
    categories=category.objects.all()
    featured_posts=blog.objects.filter(is_featured=True,status='1').order_by('-updated_at')
    posts=blog.objects.filter(is_featured=False,status='1')
    context={
        'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
    }
    return render(request,'home.html',context)