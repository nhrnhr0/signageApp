from django.shortcuts import render
from .serializers import PlaylistsViewSerializer, PlaylistDetailSerializer,ScreenSerializer,ScreenDetailSerializer
from .models import Playlist, Asset, Screen
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import AssetSerializer
from django.shortcuts import redirect
# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def playlists_view(request):
    if request.method == 'POST':
        playlist = Playlist.objects.create(
            name=request.data['name']
        )
        playlist.is_active = True if request.data.get('is_active','') == 'on' else False
        playlist.save()
        serializer = PlaylistDetailSerializer(playlist)
        return Response(serializer.data)
    else:
        playlists = Playlist.objects.all()
        if request.GET.get("search",""):
            playlists = playlists.filter(name__icontains=request.GET.get("search",""))
        serializer = PlaylistsViewSerializer(playlists, many=True)
        return Response(serializer.data)


@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def playlist_detail_view(request, pk):
    if request.method == 'PUT':
        playlist = Playlist.objects.get(uuid=pk)
        playlist.is_active = True if request.data.get('is_active','') == 'on' else False
        playlist.name = request.data['name']
        playlist.save()
    playlist = Playlist.objects.prefetch_related('assets').get(uuid=pk)
    serializer = PlaylistDetailSerializer(playlist)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def playlist_upload_asset(request, pk):
    print(request.data)
    # <QueryDict: {'duration': ['11.78'], 'type': ['video'], 'file': [<TemporaryUploadedFile: vid1_cropped.mp4 (video/mp4)>]}>
    # save the data as Asset
    asset = Asset.objects.create(
        name=request.data['file'].name,
        media=request.data['file'],
        type=request.data['type'],
        duration=request.data['duration']
    )
    
    # add the asset to the playlist
    playlist = Playlist.objects.get(uuid=pk)
    playlist.assets.add(asset)
    playlist.save()
    ret = AssetSerializer(asset)
    return Response(ret.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def screens_view(request):
    screens = Screen.objects.all()
    serializer = ScreenSerializer(screens, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def screen_detail_view(request, pk):
    screen = Screen.objects.prefetch_related('islands','islands__playlists').get(uuid=pk)
    serializer = ScreenDetailSerializer(screen)
    return Response(serializer.data)
