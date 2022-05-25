from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from .models import Member, Message, SheduledMessage
from .serializers import MemberSerializer, MessagesSerializer, SendMessageSerializer, \
    UserSearchSerializer, SheduledMessageSerializer


# class MainView(generics.ListAPIView):
#     serializer_class = MemberSerializer
#     queryset = Member.objects.all()


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MemberSerializer

    def get(self, request):
        user = self.request.user
        member = Member.objects.get(user=user)
        serializer = MemberSerializer(member)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class UserDetailView(generics.ListAPIView):
    serializer_class = MemberSerializer

    def get(self, request, *args, **kwargs):
        member = Member.objects.get(id=kwargs['id'])
        serializer = MemberSerializer(member)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSearchSerializer
    queryset = Member.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'name']


class SendMessagesView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SendMessageSerializer
    queryset = Message.objects.all()


class MessagesView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessagesSerializer

    def get_queryset(self):
        user = self.request.user
        recepient_id = self.kwargs['recepient_id']
        owner = Member.objects.get(user=user)
        recepient = Member.objects.get(id=recepient_id)
        messages = Message.objects.filter(owner=owner, recepient=recepient)
        return messages


class UpdateDeleteMessageView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessagesSerializer
    queryset = Message.objects.all()
    lookup_field = 'id'


class SheduledMessageView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SheduledMessageSerializer
    queryset = SheduledMessage