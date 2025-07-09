from rest_framework import serializers
from .models import *


class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'

class watchListSerializer(serializers.ModelSerializer):
    reviews = reviewSerializer(read_only=True, many=True)
    class Meta:
        model = watchList
        fields = '__all__'

class streamPlatformSerializer(serializers.ModelSerializer):
    watchlists = watchListSerializer(read_only=True, many=True)
    class Meta:
        model = stramPlatform
        fields = '__all__'




# class streamPlatformSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     about = serializers.CharField(style={'base_template': 'textarea.html'})
#     website = serializers.URLField(max_length=200)
#     created = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return stramPlatform.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.about = validated_data.get('about', instance.about)
#         instance.website = validated_data.get('website', instance.website)
#         instance.save()
#         return instance



# class watchListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     storyline = serializers.CharField(style={'base_template': 'textarea.html'})
#     # platform = streamPlatformSerializer()
#     active = serializers.BooleanField(default=True)
#     created = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return watchList.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.storyline = validated_data.get('storyline', instance.storyline)
#         instance.platform = validated_data.get('platform', instance.platform)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance


