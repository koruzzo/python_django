from django.shortcuts import render
from django.core.paginator import Paginator
from api.models import F_Club, F_Licence

def index(request):
    # Pagination pour les clubs
    clubs = F_Club.objects.all()
    club_paginator = Paginator(clubs, 10)  # 10 éléments par page
    club_page_number = request.GET.get('club_page')
    clubs_page = club_paginator.get_page(club_page_number)

    # Pagination pour les licences
    licences = F_Licence.objects.all()
    licence_paginator = Paginator(licences, 10)  # 10 éléments par page
    licence_page_number = request.GET.get('licence_page')
    licences_page = licence_paginator.get_page(licence_page_number)

    context = {
        'clubs_page': clubs_page,
        'licences_page': licences_page,
    }
    return render(request, 'index.html', context=context)