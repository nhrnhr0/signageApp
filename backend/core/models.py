from typing import Iterable
from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
import uuid

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
        
        

SCREEN_LAYOUT_CHOICES = (
    ('FullScreen', _('Full Screen')),
    ('MainWith4Subs', _('Main With 4 Subs')),
)

class Screen(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name=_('UUID'), primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='', verbose_name=_('Screen Name'))
    code = models.CharField(max_length=100, unique=True, verbose_name=_('Code'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is Active'))
    
    layout = models.CharField(max_length=100, choices=SCREEN_LAYOUT_CHOICES, default='MainWith4Subs', verbose_name=_('Layout'))
    islands = models.ManyToManyField('Island', related_name='screens', verbose_name=_('Islands'), blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Screen')
        verbose_name_plural = _('Screens')



class Island(models.Model):
    name = models.CharField(max_length=100, blank=True, default='', verbose_name=_('Name'))
    playlists = models.ManyToManyField('Playlist', related_name='island', verbose_name=_('Playlists'), blank=True)
    
    class Meta:
        verbose_name = _('Island')
        verbose_name_plural = _('Islands')
    
    def __str__(self):
        return self.name + ' (' + ', '.join([p.name for p in self.playlists.all()]) + ')'
    
    
class Playlist(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name=_('UUID'), primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='', verbose_name=_('Name'))
    assets = models.ManyToManyField('Asset', related_name='playlist', verbose_name=_('Assets'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is Active'))
    start_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Start At'), default=None)
    end_at = models.DateTimeField(null=True, blank=True, verbose_name=_('End At'), default=None)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))
    class Meta:
        verbose_name = _('Playlist')
        verbose_name_plural = _('Playlists')
    
    def __str__(self):
        return self.name
    
TYPE_CHOICES = (
    ('image', 'Image'),
    ('video', 'Video'),
)
class Asset(models.Model):
    name = models.CharField(max_length=100, blank=True, default='', verbose_name=_('Name'))
    media = models.FileField(upload_to='assets/', verbose_name=_('Media'))
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='image', verbose_name=_('Type'))
    
    duration = models.IntegerField(default=10, verbose_name=_('Duration'))

    class Meta:
        verbose_name = _('Asset')
        verbose_name_plural = _('Assets')
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # based on the file ending, set the type
        if self.media:
            if self.media.name.endswith('.mp4'):
                self.type = 'video'
            else:
                self.type = 'image'
        super(Asset, self).save(*args, **kwargs)
