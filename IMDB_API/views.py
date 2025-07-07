from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.reverse import reverse
from .serializers import *


"""entry point for Class Based Views"""

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'watchList': reverse('movie_list', request=request, format=format),
        'streamPlateForm': reverse('stream_platform_list', request=request, format=format)
    })


"""Class Based View by using mixins"""

class watchPlatformList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = watchList.objects.all()
    serializer_class = watchListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class watchPlatformListUpdate(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    
    queryset = watchList.objects.all()
    serializer_class = watchListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


class StreamPlatformList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = stramPlatform.objects.all()
    serializer_class = streamPlatformSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class streamPlateformUpdate(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    
    queryset = stramPlatform.objects.all()
    serializer_class = streamPlatformSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
# """Class Based Views for Stream Platform and Watch List"""

# class warchPlatformList(APIView):
#     def get_queryset(self):
#         return watchList.objects.all()  

#     def get(self, request):
#         watch_platforms = self.get_queryset()  
#         serialized = watchListSerializer(watch_platforms, many=True)
#         return Response(serialized.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         data = request.data
#         serialized = watchListSerializer(data=data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# class warchPlatformListUpdate(APIView):
#     def get_object(self, pk):
#         try:
#             return watchList.objects.get(pk=pk)
#         except watchList.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         watch_platform = self.get_object(pk)
#         if watch_platform is None:
#             return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
#         serialized = watchListSerializer(watch_platform)
#         return Response(serialized.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         watch_platform = self.get_object(pk)
#         if watch_platform is None:
#             return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
#         serialized = watchListSerializer(watch_platform, data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_200_OK)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         watch_platform = self.get_object(pk)
#         if watch_platform is None:
#             return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
#         watch_platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# class StreamPlatformList(APIView):
#     def get_queryset(self):
#         return stramPlatform.objects.all()  

#     def get(self, request):
#         stream_platforms = self.get_queryset()  
#         serialized = streamPlatformSerializer(stream_platforms, many=True)
#         return Response(serialized.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         data = request.data
#         serialized = streamPlatformSerializer(data=data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)



# class streamPlateformUpdate(APIView):
#     def get_object(self, pk):
#         try:
#             return stramPlatform.objects.get(pk=pk)
#         except stramPlatform.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         stream_platform = self.get_object(pk)
#         if stream_platform is None:
#             return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
#         serialized = streamPlatformSerializer(stream_platform)
#         return Response(serialized.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         stream_platform = self.get_object(pk)
#         if stream_platform is None:
#             return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
#         serialized = streamPlatformSerializer(stream_platform, data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_200_OK)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         stream_platform = self.get_object(pk)
#         if stream_platform is None:
#             return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
#         stream_platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


