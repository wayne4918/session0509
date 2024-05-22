# posts > serializers.py
# 주의! DRF는 TextField를 지원하지 않음. -> CharField로 내부적으로 긴 문자열을 받을 수 있음.

from rest_framework import serializers
from .models import Post, Comment

# 기본 serializer
class PostBaseSerializer(serializers.Serializer):
    image = serializers.ImageField(required=False)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)
    view_count = serializers.IntegerField()
    writer = serializers.IntegerField()
    bad_post = serializers.BooleanField()
    	
    def create(self, validated_data):
        writer_id = validated_data['writer']  
        writer_instance = User.objects.get(id=writer_id)  #

        post = Post.objects.create(
            content=validated_data['content'],
            view_count=validated_data['view_count'],
            writer=writer_instance,  
        )
        return post
        # return Post.objects.create(validated_data)
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class GETallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # Post 모델의 모든 필드를 포함하거나 특정 필드를 지정할 수 있습니다.

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'