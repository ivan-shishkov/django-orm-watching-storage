from django.db import models
from django.utils import timezone


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
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        if not self.leaved_at:
            return timezone.now() - self.entered_at

        return self.leaved_at - self.entered_at

    def is_long(self, minutes=60):
        duration = self.get_duration()

        duration_minutes = duration.total_seconds() // 60

        return duration_minutes >= minutes

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved='leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )


def format_duration(duration):
    days = duration.days

    hours, remainder = divmod(duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days:
        return f'{days} d. {hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        return f'{hours:02d}:{minutes:02d}:{seconds:02d}'
