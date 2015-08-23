from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return '%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })
