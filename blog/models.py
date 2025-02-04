from django.db import models

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=120)
    rank = models.BooleanField(default=True)
    explane = models.CharField(max_length=200)
    x = models.TextField()
    facebook = models.TextField()
    insta =models.TextField()
    linkein =models.TextField()
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=120)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
class Tag(models.Model):
    title = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class SpecialService(models.Model):
    title = models.CharField(max_length=120)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=120)
    desc1 = models.TextField()
    desc2 = models.TextField()
    desc3 = models.TextField()
    special_service = models.ForeignKey(SpecialService, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)
    img1 = models.ImageField(upload_to="blog", default="default.jpg")
    img2 = models.ImageField(upload_to="blog", default="default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def truncate_chars(self):
        return self.desc[:200] 
    
class Comments(models.Model):
    service = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    message = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.service.title
    