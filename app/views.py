# views.py

from banjo.urls import route_get, route_post
from .models import Player
from settings import BASE_URL

@route_post(BASE_URL + 'new', args={'player_name':str, 'player_position':str})
def newplayer(args):
    newplayer = Player(
        player = args['player_name'],
        position = args['player_position'],
        active = True
    )

    newplayer.save()

    return {'player info': newplayer.json_response()}

@route_get(BASE_URL + 'stats', args={'player_name':str})
def playerstats(args):
    if Player.objects.filter(player=args['player_name']).exists():
        playerstats = Player.objects.get(player=args['player_name'])

        return {'player info': playerstats.json_response()}

    else:
        return {'error': 'no player exists'}

@route_get(BASE_URL + 'players')
def allplayers():
    allplayers = {
        'point guard': []
        'shooting guard': []
        'small forward': []
        'power forward': []
        'center': []
    }

    for players in Player.objects.all():
        if position == 'point guard':
            allplayers['point guard'].append('player')
        if position == 'shooting guard':
            allplayers['shooting guard'].append('player')
        if position == 'small forward':
            allplayers['small forward'].append('player')
        if position == 'power forward':
            allplayers['power forward'].append('player')
        if position == 'center':
            allplayers['center'].append('player')

    return {'positions': allplayers}

    
