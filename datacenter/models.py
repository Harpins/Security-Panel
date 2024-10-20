from django.db import models
from django.utils import timezone
import project.settings as settings
import datetime


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

    def get_duration(content):
        timezone.activate(settings.TIME_ZONE)
        local_time = timezone.localtime()
        enter_time = content.entered_at
        leave_time = content.leaved_at
        if leave_time == None:
            return local_time - enter_time
        else:
            return leave_time - enter_time

    def time_format(content):
        time = Visit.get_duration(content).total_seconds()
        days = int(time // 86400)
        hours = int(time % 86400 // 3600)
        mins = int(time % 86400 % 3600 // 60)
        return f'{days} дн, {hours} ч, {mins} мин'

    def lib_maker(visit):
        visits_list = []
        for content in visit:
            temp_lib = {'who_entered': None, 'entered_at': None,
                        'duration': None}
            temp_lib['who_entered'] = content.passcard
            temp_lib['entered_at'] = content.entered_at
            temp_lib['duration'] = Visit.time_format(content)
            temp_lib['is_strange'] = Visit.is_strange(content)
            visits_list.append(temp_lib)
        return visits_list

    def is_strange(content, time_limit_min=30):
        time_in_sec = Visit.get_duration(content).total_seconds()
        time_in_min = int(time_in_sec % 86400 % 3600 // 60)
        return time_in_min >= time_limit_min

    def is_long(visit):
        visits_list = []
        for content in visit:
            temp_lib = {'entered_at': None, 'duration': None,
                        'is_strange': None}
            temp_lib['entered_at'] = content.entered_at
            temp_lib['duration'] = Visit.time_format(content)
            temp_lib['is_strange'] = Visit.is_strange(content)
            visits_list.append(temp_lib)
        return visits_list

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
