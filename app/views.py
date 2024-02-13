from django.http import HttpResponse
from django.shortcuts import render
from app.models import Player
from app.models import Club

def index(request):
    players = Player.objects.all()
    club_count = Club.objects.count()

    context = {'ball': 'grand', 'players': players, 'club_count': club_count}
    return render(request, 'index.html', context=context)
