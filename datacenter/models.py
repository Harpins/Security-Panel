from django.db import models
from django.utils import timezone
import project.settings as settings


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        timezone.activate(settings.TIME_ZONE)
        local_time = timezone.localtime()
        enter_time = self.entered_at
        leave_time = self.leaved_at
        if not leave_time:
            return local_time - enter_time
        return leave_time - enter_time

    def set_time_format(self, sec_in_day=86400, sec_in_hr=3600, sec_in_min=60):
        time = self.get_duration().total_seconds()
        days = int(time // sec_in_day)
        hours = int(time % sec_in_day // sec_in_hr)
        mins = int(time % sec_in_day % sec_in_hr // sec_in_min)
        return f'{days} дн, {hours} ч, {mins} мин'

    def is_strange(self, time_limit_min=30, sec_in_min=60):
        time_in_sec = self.get_duration().total_seconds()
        time_in_min = int(time_in_sec // sec_in_min)
        return time_in_min >= time_limit_min

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
