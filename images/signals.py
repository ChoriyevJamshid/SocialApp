from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.utils.text import slugify

from images.models import Image


@receiver(m2m_changed, sender=Image.user_likes.through)
def user_like_changed(sender, instance, **kwargs):

    instance.total_likes = instance.user_likes.count()
    instance.save()


# @receiver(post_save, sender=Image)
# def post_save_image(sender, instance, created, **kwargs):
#
#     if not instance.slug:
#         slug = slugify(instance.title)
#         Image.objects.filter(id=instance.id).update(slug=slug)

