from django.shortcuts import redirect, render
from blog.models import blog, category


# Create your views here.

def posts_by_category(request,category_id):
    posts=blog.objects.filter(status='1',category=category_id)
    context={
       'posts':posts
    }
    return render(request,'posts_by_category.html',context)
