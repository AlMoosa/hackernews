from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class User(AbstractUser):
    fullname = models.CharField(max_length=255, verbose_name="Полное имя")

    def __str__(self):
        return self.username + " --- "+ self.fullname


def upload_to(instance, filename):
    return 'profile_images/{0}/{1}'.format(instance.user.pk, filename)


class Profile(models.Model):
    CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    info = models.TextField(max_length=500, blank=True, null=True)
    age = models.PositiveSmallIntegerField(default=1)
    gender = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    default_profile_image = 'profile.jpg'
    avatar = models.ImageField(
        default=default_profile_image,
        upload_to=upload_to,
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class News(models.Model):
    title = models.TextField()
    # body = models.TextField()
    link = models.TextField()
    likes = models.ManyToManyField(User, related_name='news_likes', blank=True)

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('news_edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('news_delete', kwargs={'pk': self.pk})

    def get_like_url(self):
        return reverse('news_like', kwargs={'pk': self.pk})
 
    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('index')