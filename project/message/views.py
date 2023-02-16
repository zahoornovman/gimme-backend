from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response

from have.models import Have
from message.models import Message
from message.serializers import MessageSerializer
from user_profile.models import UserProfile, User
from want.models import Want


# Create your views here.


class ListCreateMessageView(GenericAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sender_have = None
        sender_want = None
        receiver_have = None
        receiver_want = None
        user_profile_of_user = UserProfile.objects.get(user=self.request.user)
        receiver = UserProfile.objects.get(id=self.request.data['receiver_id'])
        try:
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
            receiver_user_object = User.objects.get(id=receiver.user_id)
            receiver_email = receiver_user_object.email
            message_content = self.request.data['content']
            email_body = f'{message_content} \n Please email to this address if you are interested: {sender_email}'
            to_email=settings.EMAIL_HOST_USER
            if receiver_have:
                subject = f'New Barter Request for your Have: {receiver_have.title}'
                send_mail(
                    subject,
                    f'{email_body}',
                    to_email,
                    [receiver_email],
                    fail_silently=False,
                )
            elif receiver_want:
                subject = f'New Barter Request for your Want: {receiver_want.title}'
                send_mail(
                    subject,
                    f'{email_body}',
                    to_email,
                    [receiver_email],
                    fail_silently=False,
                )
            else:
                subject = f'New Barter Request'
                send_mail(
                    subject,
                    f'{email_body}',
                    to_email,
                    [receiver_email],
                    fail_silently=False,
                )

            serializer.save(sender_have=sender_have, sender_want=sender_want, receiver_have=receiver_have,
                            receiver_want=receiver_want, receiver=receiver, sender=user_profile_of_user)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

