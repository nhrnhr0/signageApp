from typing import Iterable
from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils.text import slugify
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
        
        

SCREEN_LAYOUT_CHOICES = (
    ('FullScreen', _('Full Screen')),
    ('MainWith4Subs', _('Main With 4 Subs')),
)

MainWith4Subs = [
    'ראשי','תת תצוגה 1','תת תצוגה 2','תת תצוגה 3','תת תצוגה 4']
FullScreen = ['ראשי']

def short_urlsafe_uuid():
    return slugify(str(uuid.uuid4())[:8])


class Screen(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name=_('UUID'), primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='', verbose_name=_('Screen Name'))
    code = models.CharField(max_length=100, unique=True, verbose_name=_('Code'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is Active'))
    
    layout = models.CharField(max_length=100, choices=SCREEN_LAYOUT_CHOICES, default='MainWith4Subs', verbose_name=_('Layout'))
    # islands = models.ManyToManyField('Island', related_name='screens', verbose_name=_('Islands'), blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Screen')
        verbose_name_plural = _('Screens')
        
    def save(self, *args, **kwargs):
        # init islands based on layout
        self.init_islands()
        super(Screen, self).save(*args, **kwargs)


    def init_islands(self):
        # init islands based on layout
        from .models import Island
        islands = Island.objects.filter(screen=self)
        needed_islands = []
        if self.layout == 'MainWith4Subs':
            needed_islands = MainWith4Subs
        elif self.layout == 'FullScreen':
            needed_islands = FullScreen
        for island in islands:
            if island.name not in needed_islands:
                island.delete()
            else:
                needed_islands.remove(island.name)
        for island in needed_islands:
            Island.objects.create(name=island, screen=self)
            

class Island(models.Model):
    name = models.CharField(max_length=100, blank=True, default='', verbose_name=_('Name'))
    playlists = models.ManyToManyField('Playlist', related_name='islands', verbose_name=_('Playlists'), blank=True)
    screen = models.ForeignKey('Screen', related_name='islands', on_delete=models.CASCADE, verbose_name=_('Screen'))
    class Meta:
        verbose_name = _('Island')
        verbose_name_plural = _('Islands')
    
    def __str__(self):
        return self.name + ' (' + ', '.join([p.name for p in self.playlists.all()]) + ')'
    
    
class Playlist(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name=_('UUID'), primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='', verbose_name=_('Name'))
    assets = models.ManyToManyField('Asset', related_name='playlist', verbose_name=_('Assets'), blank=True)
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
