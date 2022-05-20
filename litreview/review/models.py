from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from PIL import Image


class Ticket(models.Model):
    """Ticket model Fiels = title, description, user, image, time_created
    Added Methods: resize_image, clean_storage"""
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
                             to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE
                             )
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    IMAGE_MAX_SIZE = (105, 149)

    def resize_image(self):
        """Force the image format to portrait size 105*147px"""
        image = Image.open(self.image)
        image = image.resize(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        """Override the save method to resize the image when saving"""
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()

    def delete(self, filename, *args, **kwargs):
        """Override the delete method to clean image storage on delete"""
        self.clean_storage(filename)
        super().delete(*args, **kwargs)

    def clean_storage(self, filename):
        """
        Arg: filename
        Deletes the stored image if it exists.
        """
        try:
            fs = FileSystemStorage()
            fs.delete(filename)
        except Exception:
            pass


class Review(models.Model):
    """
    Ticket model Fiels = ticket, rating, headline, body, user, time_created
    """
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    """
    Ticket model Fiels = user, followed_user
    """
    user = models.ForeignKey(
                             to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='following'
                             )
    followed_user = models.ForeignKey(
                                      to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='followed_by'
                                      )

    class Meta:
        unique_together = ('user', 'followed_user')
