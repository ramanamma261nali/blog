
from django.contrib.auth.models import User
from django.db import models

class category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
          verbose_name_plural='categories'
    def __str__(self):
        return self.category_name
STATUS_CHOICES=(
    (0,"Draft"),
    (1,"Published")
)
class blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True,blank=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='upload/%y/%M/%d')
    short_description=models.TextField(max_length=2000)
    blog_body=models.TextField(max_length=5000)
    status=models.IntegerField(choices=STATUS_CHOICES,default=0)
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def  __str__(self):
        return self.title

