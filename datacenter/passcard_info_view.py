from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_object_or_404
from django.shortcuts import render


def passcard_info_view(request, passcode):

    passcard = Passcard.objects.all()[0]

    visits_list = Visit.objects.filter(passcard=get_object_or_404(
        Passcard.objects.all(), passcode=passcode))

    this_passcard_visits = Visit.is_long(visits_list)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
