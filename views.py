from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Message
from .serializers import MessageSerializer
from .utils import dna_encrypt, dna_decrypt

@api_view(['POST'])
def send_message(request):
    """
    API: Send message with DNA-inspired encryption
    """
    sender = User.objects.get(username=request.data["sender"])
    receiver = User.objects.get(username=request.data["receiver"])
    encrypted, new_key = dna_encrypt(request.data["content"])
    msg = Message.objects.create(sender=sender, receiver=receiver, encrypted_content=encrypted)
    return Response({"status": "success", "encrypted": encrypted, "new_key": new_key})

@api_view(['GET'])
def receive_message(request, user_id):
    """
    API: Receive + decrypt messages
    """
    messages = Message.objects.filter(receiver_id=user_id).order_by("-timestamp")
    decrypted_msgs = []
    for msg in messages:
        decrypted = dna_decrypt(msg.encrypted_content)
        decrypted_msgs.append({
            "from": msg.sender.username,
            "message": decrypted,
            "time": msg.timestamp
        })
    return Response({"messages": decrypted_msgs})

