from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserAccount, User


# @receiver(post_save, sender=UserAccount)
# def user_account_updater(sender, instance, **kwargs):
#     print(instance.phone_number)
# user = User.objects.get(phone_number =l instance.phone_number)
# print(user)


# @receiver(post_save, sender=User)
# def user_create(sender, instance, created,**kwargs):

#         account = UserAccount.objects.create(phone_number = instance.phone_number, username = instance.username)

#         instance.account = account
#         instance.save()
