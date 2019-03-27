from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    thumb = models.ImageField(default='default.png', blank=True)
    




    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


    def snippet(self):

        return self.text[:50]




class Post1(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    thumb = models.ImageField(default='default.png', blank=True)
    








    
# Create your models here.


# Create your models here.
