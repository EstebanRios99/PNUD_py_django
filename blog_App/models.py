from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class category(models.Model):
    name=models.CharField(max_length=60)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

class news(models.Model):
    title=models.CharField(max_length=60)
    text = models.TextField()
    image=models.ImageField(upload_to='blog',null=True,blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    categories=models.ManyToManyField(category)
    published_date = models.DateTimeField(
            blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='new'
        verbose_name_plural='news'
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title