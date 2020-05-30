from .models import TimecardModel, TimecardHistoryModel
from django.db.models.signals import pre_save, post_save
from django.db.models import signals
from django.dispatch import receiver


def clockout(sender, instance, *args, **kwargs):
    print 'signal is firing'
    instance.is_clocked_out = False
    if instance.clock_out:
        instance.is_clocked_out = True
        return instance.is_clocked_out
    return instance



post_save.connect(clockout, sender=TimecardModel)