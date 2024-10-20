from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    
    visit = Visit.objects.filter(leaved_at=None)
        
    non_closed_visits = Visit.lib_maker(visit)
    
    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
