from rest_framework import serializers

from .models import Member, Message, SheduledMessage


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'username', 'bio', 'avatar')


class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        exclude = ['user']


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('message', 'file_message')

    def create(self, validated_data):
        recepient_id = self.context.get('view').kwargs.get('recepient_id')
        user = self.context.get('request').user
        owner = Member.objects.get(user=user)
        recepient = Member.objects.get(id=recepient_id)
        validated_data['owner'] = owner
        validated_data['recepient'] = recepient
        return super().create(validated_data)


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message', 'owner', 'recepient', 'file_message', 'date_time', 'status')


class SheduledMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SheduledMessage
        fields = ('s_message', 's_file_message', 's_date_time')

    def create(self, validated_data):
        recepient_id = self.context.get('view').kwargs.get('s_recepient_id')
        user = self.context.get('request').user
        owner = Member.objects.get(user=user)
        recepient = Member.objects.get(id=recepient_id)
        validated_data['s_owner'] = owner
        validated_data['s_recepient'] = recepient
        return super().create(validated_data)