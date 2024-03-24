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
from django.utils import timezone
import datetime
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
    uuid = models.CharField(default=short_urlsafe_uuid, editable=False, unique=True, verbose_name=_('UUID'), primary_key=True, max_length=50)
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
        
        super(Screen, self).save(*args, **kwargs)
        self.init_islands()


    def init_islands(self):
        # init islands based on layout
        from .models import Island
        islands = Island.objects.filter(screen=self)
        needed_islands = []
        if self.layout == 'MainWith4Subs':
            needed_islands = MainWith4Subs
        elif self.layout == 'FullScreen':
            needed_islands = FullScreen
        
        print('needed_islands', needed_islands, ' layout', self.layout, 'screen', self.name, 'islands', islands)
            
        for island_name in needed_islands:
            island = Island.objects.filter(name=island_name, screen=self).first()
            if not island:
                island = Island.objects.create(name=island_name, screen=self)
            islands = Island.objects.filter(screen=self)
            if island not in islands:
                islands.add(island)
            

class Island(models.Model):
    name = models.CharField(max_length=100, blank=True, default='', verbose_name=_('Name'))
    playlists = models.ManyToManyField('Playlist', related_name='islands', verbose_name=_('Playlists'), blank=True)
    screen = models.ForeignKey('Screen', related_name='islands', on_delete=models.CASCADE, verbose_name=_('Screen'))
    class Meta:
        verbose_name = _('Island')
        verbose_name_plural = _('Islands')
    
    def __str__(self):
        return self.name + ' (' + ', '.join([p.name for p in self.playlists.all()]) + ')'
    



# SCHEDULE_TYPE_CHOICES = (
#     ('OnOff', _('On/Off')),
#     ('BetweenDates', _('Between dates')),
# )
# class Schedule(models.Model):
#     type = models.CharField(max_length=100, verbose_name=_('Type'), choices=SCHEDULE_TYPE_CHOICES)
#     data = models.JSONField(verbose_name=_('Data'))
#     class Meta:
#         verbose_name = _('Schedule')
#         verbose_name_plural = _('Schedules')

class Playlist(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name=_('UUID'), primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='', verbose_name=_('Name'))
    assets = models.ManyToManyField('Asset', related_name='playlist', verbose_name=_('Assets'), blank=True)
    # is_active = models.BooleanField(default=False, verbose_name=_('Is Active'))
    schedule = models.JSONField(verbose_name=_('Schedule'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))
    
    def is_active(self):
        if not self.schedule:
            return False
        now = datetime.datetime.now()
        if self.schedule.get('type') == 'onOff':
            return self.schedule.get('data',False)
        elif self.schedule.get('type') == 'betweenDates':
            # if data.start is None, we ignore start time check
            # if data.end is None, we ignore end time check
            start = self.schedule.get('data',{}).get('start',None)
            end = self.schedule.get('data',{}).get('end',None)
            if start:
                start = datetime.datetime.fromisoformat(start)
                
                if start > now:
                    return False
            if end:
                end = datetime.datetime.fromisoformat(end)
                if end < now:
                    return False
            return True
        return False
    is_active.boolean = True
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
