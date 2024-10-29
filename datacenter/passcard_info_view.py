from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_object_or_404
from django.shortcuts import render


def passcard_visits(visits):
    this_passcard_visits = []
    for visit in visits:
        visit_data = {
            'entered_at': visit.entered_at,
            'duration': visit.set_time_format(),
            'is_strange': visit.is_strange(),
        }
        this_passcard_visits.append(visit_data)
    return this_passcard_visits


def passcard_info_view(request, passcode):

    passcard_instance = get_object_or_404(Passcard, passcode=passcode)
    serialized_visits = Visit.objects.filter(passcard=passcard_instance)
    this_passcard_visits = passcard_visits(serialized_visits)

    context = {
        'passcard': passcard_instance,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
