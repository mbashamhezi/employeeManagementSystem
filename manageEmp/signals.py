# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.template.loader import render_to_string
# from django.contrib.auth.models import User

# @receiver(post_save, sender=User)
# def send_registration_email(sender, instance, created, **kwargs):
#     if created:
#         subject = 'Welcome to Our Company'
#         message = render_to_string('email/registration_email.html', {
#             'username': instance.username,
#             'temporary_password': instance.tpass,
#         })
#         recipient_list = [instance.email]
#         send_mail(subject, message, 'your-email-address', recipient_list, fail_silently=False)
