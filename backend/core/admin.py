from django.contrib import admin
from .models import Screen, Island, Playlist, Asset
# Register your models here.

class ScreenAdmin(admin.ModelAdmin):
    filter_horizontal = ('islands',)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        # if no islands are selected, then create a default island
        if not form.instance.islands.all():
            island = Island.objects.create(name=form.instance.name + ' Default Island')
            form.instance.islands.add(island)
            form.instance.save()
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