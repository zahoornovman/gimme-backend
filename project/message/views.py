import os
from email.mime.image import MIMEImage
from os.path import basename

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from have.models import Have
from message.models import Message
from message.serializers import MessageSerializer
from user_profile.models import UserProfile, User
from want.models import Want

from django.contrib.staticfiles.storage import staticfiles_storage


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

            message_content = self.request.data['content']
            email_body = f'{message_content} \n If interested please send an email to this address: {sender_email}'
            from_email = settings.EMAIL_HOST_USER
            to_email = receiver_user_object.email






            subject = f'New Barter Offer for your Request'

            msg = EmailMultiAlternatives(
                subject,
                email_body,
                from_email=from_email,
                to=[to_email]
            )

            msg.mixed_subtype = 'related'
            msg.attach_alternative(email_body, "text/html")
            img_dir = 'static'
            image = 'gimme.png'
            file_path = staticfiles_storage.path('images/gimme.png')
            print(file_path)
            email_template = get_template('../templates/index.html')
            context = {'image_path': file_path, 'message': message_content, 'sender_email': sender_email}
            html_content = email_template.render(context)
            with open(file_path, 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-ID', '<{name}>'.format(name=image))
                img.add_header('Content-Disposition', 'inline', filename=image)

            msg.attach(img)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            # image_path = staticfiles_storage.path('images/gimme.png')
            #
            # with open(image_path, 'rb') as f:
            #     image_data = f.read()
            #     # image_data = MIMEImage(f.read())
            #
            #     image_data.add_header('Content-ID', '<{}>'.format(f))
            #
            # image_file = ContentFile(image_data)
            # image_cid = 'gimme.png'
            #
            # email_template = get_template('../templates/index.html')
            # context = {'image_path': image_path, 'message': message_content, 'sender_email': sender_email}
            # html_content = email_template.render(context)
            # if receiver_have:
            #     subject = f'New Barter Request for your Offer: {receiver_have.title}'
            #     msg = EmailMultiAlternatives(subject, email_body, from_email, [to_email])
            #     msg.attach('gimme.png', image_data, 'image/png')
            #     # msg.attach(basename(image_path), image_data, 'image/png')
            #     msg.attach_alternative(html_content, "text/html")
            #     print(image_path)
            #     msg.send()
            #     # send_mail(
            #     #     subject,
            #     #     f'{email_body}',
            #     #     from_email,
            #     #     [receiver_email],
            #     #     fail_silently=False,
            #     # )
            # elif receiver_want:
            #     subject = f'New Barter Offer for your Request: {receiver_want.title}'
            #     msg = EmailMultiAlternatives(subject, email_body, from_email, [to_email])
            #     msg.attach(basename(image_path), image_data, 'image/png')
            #     msg.attach_alternative(html_content, "text/html")
            #     msg.send()
            #     # send_mail(
            #     #     subject,
            #     #     f'{email_body}',
            #     #     from_email,
            #     #     [receiver_email],
            #     #     fail_silently=False,
            #     # )
            # else:
            #     subject = f'New Barter Request'
            #     msg = EmailMultiAlternatives(subject, email_body, from_email, [to_email])
            #     msg.attach(basename(image_path), image_data, 'image/png')
            #     msg.attach_alternative(html_content, "text/html")
            #     msg.send()
            #     # send_mail(
            #     #     subject,
            #     #     f'{email_body}',
            #     #     from_email,
            #     #     [receiver_email],
            #     #     fail_silently=False,
            #     # )

            serializer.save(sender_have=sender_have, sender_want=sender_want, receiver_have=receiver_have,
                            receiver_want=receiver_want, receiver=receiver, sender=user_profile_of_user)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
