from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import *
from .models import Room, Chat
from .serializers import RoomSerializers, ChatSerializer, ChatPostSerializer

# Create your views here.


# Chat rooms
class Rooms(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({'data': serializer.data})


class Dialog(APIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    def get(self, request):
        room = request.GET.get('room')
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializer(chat, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        dialog = ChatPostSerializer(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response({'status': 'Add'})
        else:
            return Response({'status': 'Error'})
