from django.core.mail import send_mail

from rest_framework import permissions

def send_activation_email(user):
    subject = 'Thanks for registration'
    body = 'Thanks for registration in our site.\n'\
        'For account activation go for link below:\n'\
            f'http://http://demo-meerim.herokuapp.com/v1/account/activate/{user.activation_code}/'
    from_email = 'e-shop@django.kg'
    recipients = [user.email]
    send_mail(subject=subject, message=body, from_email=from_email, recipient_list=recipients)


class IsOwnerAccount(permissions.BasePermission):
    """"пермишн для проверки владельца аккаунта или суперюзера"""
    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username or bool(request.user and request.user.is_superuser)

