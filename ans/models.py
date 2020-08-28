from django.db import models
from django.utils.translation import ugettext_lazy as _

# from newsletter_subscription.models import SubscriptionBase
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    from_email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=300)
    message = models.TextField(max_length=1000)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return self.name

# class Subscription(SubscriptionBase):
#     full_name = models.CharField(_('full name'), max_length=100, blank=True)