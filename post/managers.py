from django.db import models


class PostManager(models.Manager):

    def published(self, *args, **kwargs):
        queryset = super(PostManager, self).get_queryset(*args, **kwargs).filter(status='published')
        return queryset
