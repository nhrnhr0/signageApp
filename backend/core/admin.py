from django.contrib import admin
from .models import Screen, Island, Playlist, Asset
# Register your models here.

class IslandInline(admin.TabularInline):
    model = Island
    extra = 0
    fields = ['id', 'name',]
    readonly_fields = ['id','name',]
    
class ScreenAdmin(admin.ModelAdmin):
    inlines = [IslandInline]
admin.site.register(Screen, ScreenAdmin)
class IslandAdmin(admin.ModelAdmin):    

    pass
admin.site.register(Island, IslandAdmin)
class PlaylistAdmin(admin.ModelAdmin):
    filter_horizontal = ('assets',)
    pass
admin.site.register(Playlist, PlaylistAdmin)
class AssetAdmin(admin.ModelAdmin):
    
    pass
admin.site.register(Asset, AssetAdmin)