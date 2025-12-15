from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RoomSerializer,DistrictSerializer
from .models import Room, RoomImage, District
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class DistrictView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print("request",request)
        queryset = District.objects.all()
        serializer = DistrictSerializer(queryset, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    

class RoomView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):

        if pk:
            try:
                room = Room.objects.get(pk=pk)
                serializer = RoomSerializer(room)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            except Room.DoesNotExist:
                return Response(
                    {"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND
                )

        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(user=request.user)

            # Upload multiple images
            images = request.FILES.getlist("images")
            for img in images:
                RoomImage.objects.create(room=room, image=img)

            return Response(
                {"message": "Room created", "room": RoomSerializer(room).data},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is None:
            return Response(
                {"message": "Id required to update"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            room = Room.objects.get(pk=pk, user=request.user)
        except Room.DoesNotExist:
            return Response(
                {"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = RoomSerializer(room, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Room updated"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response(
                {"message": "Id required to delete"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            room = Room.objects.get(pk=pk, user=request.user)
        except Room.DoesNotExist:
            return Response(
                {"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND
            )

        room.delete()
        return Response({"message": "Room deleted"}, status=status.HTTP_204_NO_CONTENT)
