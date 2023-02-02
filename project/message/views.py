from django.core.mail import send_mail
from rest_framework.generics import ListCreateAPIView

from have.models import Have
from message.models import Message
from message.serializers import MessageSerializer
from user_profile.models import UserProfile, User
from want.models import Want


# Create your views here.


class ListCreateMessageView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        sender_have = None
        sender_want = None
        receiver_have = None
        receiver_want = None
        user_profile_of_user = UserProfile.objects.get(user=self.request.user)
        receiver = UserProfile.objects.get(id=self.request.data['receiver_id'])
        if self.request.data['sender']:
            if self.request.data['sender']['type'] == 'have':
                sender_have = Have.objects.get(id=self.request.data['sender']['id'])
            else:
                sender_want = Want.objects.get(id=self.request.data['sender']['id'])
        if self.request.data['receiver']:
            if self.request.data['receiver']['type'] == 'have':
                receiver_have = Have.objects.get(id=self.request.data['receiver']['id'])
            else:
                receiver_want = Want.objects.get(id=self.request.data['receiver']['id'])

        sender_email = self.request.user
        print(receiver)
        receiver_user_object = User.objects.get(id=receiver.user_id)
        print(type(receiver_user_object))
        print(receiver_user_object)
        email = receiver_user_object.email
        print(email)
        content = self.request.data['content']

        send_mail(
            f'New Barter Request',
            f'{content}' 
            f'Please email to this address if interested: {sender_email}',
            'gimme.switzerland@gmail.com',
            [email],
            fail_silently=False,
        )

        serializer.save(sender_have=sender_have, sender_want=sender_want, receiver_have=receiver_have,
                        receiver_want=receiver_want, receiver=receiver, sender=user_profile_of_user)
