from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Image(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='images_created')
    user_likes = models.ManyToManyField(User,
                                        blank=True,
                                        related_name='images_liked')

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title










