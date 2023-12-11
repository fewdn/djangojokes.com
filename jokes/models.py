from django.conf import settings
from django.db import models
from django.urls import reverse
from common.utils.text import unique_slug

# Create your models here.
class Joke(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    # If Category class does not come before Joke class, use a string ForeignKey('Category',...)
    # By default a related manager uses sometag.<name>_set 
    # sometag.joke_set on a Tag would return the related manager for jokes with that tag
    # Specifying a name for the related manager can help with clarity. Using related_name="jokes"
    #   turns sometag.joke_set   into   sometag.jokes  when accessing the related manager
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='jokes')
    #many-to-many fields are required, use blank=True to make it optional
    tags = models.ManyToManyField('Tag', blank=True, related_name='jokes') 
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def get_absolute_url(self):
        return reverse('jokes:detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.question
    

class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['category']


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:tag', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['tag']
