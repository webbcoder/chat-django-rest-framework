from rest_framework import serializers
from .models import Room


# Serialization of chat rooms
class RoomSerializers(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('creator', 'invited', 'date')
