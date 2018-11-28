from django.db import models

from django.urls import reverse

from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('view_blog_post', args=(self.slug,))


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    slug = models.SlugField(max_length=100)
    content = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default=None, upload_to='uploads/')
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    publish_post = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s' % self.title