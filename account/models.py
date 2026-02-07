from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    birth_of_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="profile/%Y/%m/%d/",
                              blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"





