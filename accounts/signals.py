from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

# @receiver(post_save, sender=User)
# def post_save_create_profile_receiver(sender, instance, created, **kwargs):
#     print(created)
#     if created:
#         UserProfile.objects.create(user=instance)
#         # print('user profile is created!')
#     else:
#         try:
#             profile = UserProfile.objects.get(user=instance)
#             profile.save()
#         except:
#             # create user profile if it doesn't exist
#             UserProfile.objects.create(user=instance)
#         #     print("Profile didn't exist, but I created one")
#         # print('user is updated')


# post_save.connect(post_save_create_profile_receiver, sender=User)

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass
    # print(instance.username, 'this user is being saved')
