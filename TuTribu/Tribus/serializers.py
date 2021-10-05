from rest_framework import serializers

from Tribus.models import *

class TribuSerial(serializers.ModelSerializer):
    class Meta:
        model = Tribu
        fields = '__all__'


class PostSerial(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['postId', 'post_fecha_pub', 'postTribu', 'numLikes', 'numDislikes', 'numLoves', 'numHates']


class ReaccionSerial(serializers.ModelSerializer):
    class Meta:
        model = Reaccion
        fields = '__all__'


class ReaccionPostSerial(serializers.ModelSerializer):
    class Meta:
        model = ReaccionPost
        fields = '__all__'
