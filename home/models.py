from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe

class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    title           = models.CharField(max_length=150)
    keywords        = models.CharField(max_length=255)
    description     = models.CharField(max_length=255)
    welcome_message = models.CharField(max_length=200)
    company         = models.CharField(max_length=50)
    address         = models.CharField(blank=True, max_length=150)
    phone           = models.CharField(blank=True, max_length=15)
    fax             = models.CharField(blank=True, max_length=15)
    email           = models.CharField(blank=True, max_length=50)
    smtpserver      = models.CharField(blank=True, max_length=20)
    smtpemail       = models.CharField(blank=True, max_length=20)
    smtppassword    = models.CharField(blank=True, max_length=10)
    smtpport        = models.CharField(blank=True, max_length=5)
    icon            = models.ImageField(blank=True, upload_to='images/')
    logo            = models.ImageField(blank=True, upload_to='images/')
    facebook        = models.CharField(blank=True, max_length=50)
    instagram       = models.CharField(blank=True, max_length=50)
    twitter         = models.CharField(blank=True, max_length=50)
    aboutus         = RichTextField(blank=True)
    contact         = RichTextField(blank=True)
    references      = RichTextField(blank=True)
    status          = models.CharField(max_length=10,choices=STATUS)
    create_at       = models.DateTimeField(auto_now_add=True)
    update_at       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def icon_show(self):
        if self.icon:
            return mark_safe('<img src="{}" height="24px"/>'.format(self.icon.url))
        return self.icon
    icon_show.short_description = 'İcon'

    def logo_show(self):
        if self.logo:
            return mark_safe('<img src="{}" height="48px"/>'.format(self.logo.url))
        return self.logo
    logo_show.short_description = 'Logo'