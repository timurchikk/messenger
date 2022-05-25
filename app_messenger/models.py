from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE, related_name='user')
    name = models.CharField(verbose_name='Name', max_length=25)
    username = models.CharField(verbose_name='Username', max_length=10)
    bio = models.TextField(verbose_name='Bio')
    avatar = models.ImageField(verbose_name='Avatar', upload_to = 'avatars/')

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        # app_label = 'messenger'

    def __str__(self):
        return self.username


class Message(models.Model):
    STATUS_CHOICES = (
        ('unreaded', 'unreaded'),
        ('readed', 'readed'),
    )

    owner = models.ForeignKey(Member, verbose_name='Owner', related_name='owner', on_delete=models.CASCADE)
    recepient = models.ForeignKey(Member, verbose_name='Recepient', related_name='recepient', on_delete=models.CASCADE)
    message = models.TextField(verbose_name='Message', null=True)
    file_message = models.FileField(verbose_name='File message', upload_to = f'messages/files/{owner}', null=True)
    date_time = models.DateTimeField(verbose_name='Date and time', default=timezone.now)
    status = models.CharField(verbose_name='Status', choices=STATUS_CHOICES, default='unreaded', max_length=10)
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'{self.owner} --> {self.recepient}'


class SheduledMessage(models.Model):
    STATUS_CHOICES = (
        ('unreaded', 'unreaded'),
        ('readed', 'readed'),
    )

    s_owner = models.ForeignKey(Member, verbose_name='S_Owner', related_name='s_owner', on_delete=models.CASCADE)
    s_recepient = models.ForeignKey(Member, verbose_name='S_Recepient', related_name='s_recepient', on_delete=models.CASCADE)
    s_message = models.TextField(verbose_name='s_Message', null=True)
    s_file_message = models.FileField(verbose_name='s_File message', upload_to = f'messages/files/{s_owner}', null=True)
    s_date_time = models.DateTimeField(verbose_name='s_Date and time', default=timezone.now)
    s_status = models.CharField(verbose_name='S_Status', choices=STATUS_CHOICES, default='unreaded', max_length=10)
  
    class Meta:
        verbose_name = 'Sheduled message'
        verbose_name_plural = 'Sheduled messages'

    def __str__(self):
        return f'{self.s_owner} --> {self.s_recepient}'