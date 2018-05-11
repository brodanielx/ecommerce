from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.db import models
from django.db.models.signals import pre_save, post_save

from accounts.signals import user_logged_in
from .signals import object_viewed_signal
from .utils import get_client_ip

User = settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
    user            = models.ForeignKey(User, blank=True, null=True) # User instance
    ip_address      = models.CharField(max_length=220, blank=True, null=True)
    content_type    = models.ForeignKey(ContentType) # User, Product, Order, Cart, Address
    object_id       = models.PositiveIntegerField()  # User id, Product id, Order id, Cart id, Address id
    content_object  = GenericForeignKey('content_type', 'object_id') # Product instance
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed on %s" %(self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'

def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    new_view_obj = ObjectViewed.objects.create(
            user = request.user,
            content_type = c_type,
            object_id = instance.id,
            ip_address = get_client_ip(request)
    )

object_viewed_signal.connect(object_viewed_receiver)


class UserSession(models.Model):
    user            = models.ForeignKey(User, blank=True, null=True) # User instance
    ip_address      = models.CharField(max_length=220, blank=True, null=True)
    session_key     = models.CharField(max_length=100, blank=True, null=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    active          = models.BooleanField(default=True)
    ended           = models.BooleanField(default=False)

def user_logged_in_reciever(sender, instance, request, *args, **kwargs):
    print(instance)
    user = instance
    ip_address = get_client_ip(request)
    session_key = request.session.session_key
    UserSession.objects.create(
        user = user,
        ip_address = ip_address,
        session_key = session_key
    )

user_logged_in.connect(user_logged_in_reciever)
