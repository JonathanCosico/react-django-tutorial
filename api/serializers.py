from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','code','host','guest_can_pause','votes_to_skip','created_at')

class CreateRoomSerializer(serializers.ModelSerializer):
    # make sure data sent in post req fits to create new room eg. /create-room {votes_to_skip: 3, }
    # when handling different request, good to user serializer
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')