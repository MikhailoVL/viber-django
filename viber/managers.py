from django.db import models


class ViberUserStatusManager(models.Manager):

    def subscribed(self, user):
        status = self.create(status=0, viber_user=user)
        return status