from datacenter.models import Visit
from django.shortcuts import render


def is_still_visiting(visits):
    visitors = []
    for visit in visits:
        visit_data = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': visit.set_time_format(),
            'is_strange': visit.is_strange(),
        }
        visitors.append(visit_data)
    return visitors


def storage_information_view(request):

    non_closed_visits = Visit.objects.filter(leaved_at=None)

    remaining_visitors = is_still_visiting(non_closed_visits)

    context = {
        'non_closed_visits': remaining_visitors,
    }
    return render(request, 'storage_information.html', context)
