from datacenter.models import Visit
from django.shortcuts import render


def still_visiting(visits):
    visitors = []
    for content in visits:
        visit_data = {
            'who_entered': content.passcard,
            'entered_at': content.entered_at,
            'duration': content.time_format(),
            'is_strange': content.is_strange(),
        }
        visitors.append(visit_data)
    return visitors


def storage_information_view(request):

    non_closed_visits = Visit.objects.filter(leaved_at=None)

    remaining_visitors = still_visiting(non_closed_visits)

    context = {
        'non_closed_visits': remaining_visitors,
    }
    return render(request, 'storage_information.html', context)
