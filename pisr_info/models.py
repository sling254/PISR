from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_save
from PISR.utils import unique_slug_generator
from django.urls import reverse

# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    shot_description = models.CharField(max_length=40)
    blog_text = models.TextField()
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
       return self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

def get_absolute_url(self):
    return reverse('blog:detail',kwargs={'slug':self.slug})

pre_save.connect(slug_generator, sender=Blog)
