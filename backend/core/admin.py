from django.contrib import admin
from .models import Screen, Island, Playlist, Asset
from django.utils.safestring import mark_safe
# Register your models here.

class IslandInline(admin.TabularInline):
    model = Island
    extra = 0
    fields = ['id', 'name',]
    readonly_fields = ['id','name',]
    
class ScreenAdmin(admin.ModelAdmin):
    inlines = [IslandInline]
    readonly_fields = ['uuid']
admin.site.register(Screen, ScreenAdmin)
class IslandAdmin(admin.ModelAdmin):    
    list_display = ['id', 'name', 'screen']
    pass
admin.site.register(Island, IslandAdmin)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'name', 'is_active']
    readonly_fields = ['uuid', 'is_active']
    filter_horizontal = ('assets',)
    pass
admin.site.register(Playlist, PlaylistAdmin)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_disaply','name', 'type', 'duration','display_playlists']
    
    def image_disaply(self, obj):
        if obj.type == 'image':
            return mark_safe('<img src="{}" width="100" />'.format(obj.media.url))
        return ''
    
    def display_playlists(self, obj):
        return ', '.join([playlist.name for playlist in obj.playlist.all()])
    display_playlists.short_description = 'Playlists' 
admin.site.register(Asset, AssetAdmin)



