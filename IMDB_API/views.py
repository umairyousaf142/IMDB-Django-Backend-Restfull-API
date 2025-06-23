from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class warchPlatformList(APIView):
    def get_queryset(self):
        return watchList.objects.all()  

    def get(self, request):
        watch_platforms = self.get_queryset()  
        serialized = watchListSerializer(watch_platforms, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serialized = watchListSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

class warchPlatformListUpdate(APIView):
    def get_object(self, pk):
        try:
            return watchList.objects.get(pk=pk)
        except watchList.DoesNotExist:
            return None

    def get(self, request, pk):
        watch_platform = self.get_object(pk)
        if watch_platform is None:
            return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = watchListSerializer(watch_platform)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        watch_platform = self.get_object(pk)
        if watch_platform is None:
            return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = watchListSerializer(watch_platform, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        watch_platform = self.get_object(pk)
        if watch_platform is None:
            return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
        watch_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class StreamPlatformList(APIView):
    def get_queryset(self):
        return stramPlatform.objects.all()  

    def get(self, request):
        stream_platforms = self.get_queryset()  
        serialized = streamPlatformSerializer(stream_platforms, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serialized = streamPlatformSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)



class streamPlateformUpdate(APIView):
    def get_object(self, pk):
        try:
            return stramPlatform.objects.get(pk=pk)
        except stramPlatform.DoesNotExist:
            return None

    def get(self, request, pk):
        stream_platform = self.get_object(pk)
        if stream_platform is None:
            return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = streamPlatformSerializer(stream_platform)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        stream_platform = self.get_object(pk)
        if stream_platform is None:
            return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = streamPlatformSerializer(stream_platform, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stream_platform = self.get_object(pk)
        if stream_platform is None:
            return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
        stream_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class watchListUpdate(APIView):
    def get_object(self, pk):
        try:
            return watchList.objects.get(pk=pk)
        except watchList.DoesNotExist:
            return None

    def get(self, request, pk):
        movie = self.get_object(pk)
        if movie is None:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = watchListSerializer(movie)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        movie = self.get_object(pk)
        if movie is None:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = watchListSerializer(movie, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        if movie is None:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENTr)