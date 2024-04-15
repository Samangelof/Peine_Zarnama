from django.db import models
from auths.models import CustomUser


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='sent_messages'
    )
    recipient = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='received_messages'
    )
    
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'chats'
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.sender} -> {self.recipient}: {self.text}'