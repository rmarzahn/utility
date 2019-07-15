from django.db import models

# Create your models here.
class NewsletterUser(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True, verbose_name = 'Benutzername (optional)')
    email = models.EmailField(verbose_name = 'E-Mail')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    EMAIL_STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )
    subject = models.CharField(max_length=250)
    body = models.TextField()
    email = models.ManyToManyField(NewsletterUser)
    status = models.CharField(max_length=25, choices=EMAIL_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)