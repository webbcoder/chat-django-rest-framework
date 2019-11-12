from rest_framework import serializers
from .models import User, Room, Chat


# Serialization of users
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


# Serialization of chat rooms
class RoomSerializers(serializers.ModelSerializer):
    creator = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ('creator', 'invited', 'date')


# Serialization of chat
class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Chat
        fields = ('user', 'text', 'date')


class ChatPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('room', 'text',)


