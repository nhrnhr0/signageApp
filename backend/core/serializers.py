from .models import Screen,Playlist,Asset,Island
from rest_framework import serializers


class ScreensIslandsSerializer(serializers.ModelSerializer):
    islands = serializers.SerializerMethodField()
    def get_islands(self, obj):
        ret = []
        for island in obj.islands.all():
            ret.append({
                'id': island.id,
                'name': island.name
            })
        return ret
    class Meta:
        model = Screen
        fields = ('uuid', 'name', 'is_active',  'islands')
    

class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = ('uuid', 'name', 'is_active', 'layout')
class ScreenDetailSerializer(serializers.ModelSerializer):
    islands = serializers.SerializerMethodField()
    
    def get_islands(self, obj):
        ret = []
        for island in obj.islands.all():
            playlists = []
            for playlist in island.playlists.all():
                playlists.append({
                    'uuid': playlist.uuid,
                    'name': playlist.name
                })
            ret.append({
                'id': island.id,
                'name': island.name,
                'playlists': playlists
            })
        return ret
    
    class Meta:
        model = Screen
        fields = ('uuid','code', 'name', 'is_active', 'layout', 'islands')
class ScreenInPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = ('uuid', 'name', 'is_active', 'layout')
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'
        
class IslandSerializer(serializers.ModelSerializer):
    screens = ScreenInPlaylistSerializer(many=True, read_only=True)
    class Meta:
        model = Island
        fields = ('id', 'name', 'screens')

class PlaylistsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('uuid', 'name', 'is_active', 'created_at', 'updated_at')
        
class PlaylistDetailSerializer(serializers.ModelSerializer):
    assets = AssetSerializer(many=True, read_only=True)
    islands = IslandSerializer(many=True, read_only=True)
    class Meta:
        model = Playlist
        fields = ('uuid', 'name', 'is_active', 'start_at', 'end_at', 'assets','islands')
        
        
class ScreenDisplaySerializer(serializers.ModelSerializer):
    islands = serializers.SerializerMethodField()
    
    def get_islands(self, obj):
        ret = []
        for island in obj.islands.all():
            playlists = []
            for playlist in island.playlists.all():
                assets = []
                for asset in playlist.assets.all():
                    assets.append({
                        'id': asset.id,
                        'name': asset.name,
                        'media': asset.media.url,
                        'type': asset.type,
                        'duration': asset.duration
                    })
                playlists.append({
                    'uuid': playlist.uuid,
                    'name': playlist.name,
                    'assets': assets
                })
            ret.append({
                'id': island.id,
                'name': island.name,
                'playlists': playlists
            })
        return ret
    
    class Meta:
        model = Screen
        fields = ('uuid', 'name', 'is_active', 'layout', 'islands')