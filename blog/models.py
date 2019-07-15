from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, default=timezone.now, help_text = 'Slug bitte identisch zum Name der Category setzen')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('post_category', args=[self.slug])

    def __str__(self):
        return self.name
    


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    thumb = models.ImageField(blank=True, null=True, verbose_name = 'Image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:500] + '...'