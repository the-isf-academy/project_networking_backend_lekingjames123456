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

@route_get(BASE_URL + 'stats/advanced', args={'player_name':str})
def advancedstats(args):
    if player.objects.filter(player=args['player_name']).exists():
        playerstats = Player.objects.get(player=args['player_name'])

        return {'advanced info': advancedstats.json_response_advanced()}

    else:
        return {'error': 'no player exists'}


@route_get(BASE_URL + 'players')
def allplayers(args):
    allplayers = {
        'point guard': [],
        'shooting guard': [],
        'small forward': [],
        'power forward': [],
        'center': []
    }

    for player in Player.objects.all():
        if player.position == 'point guard':
            allplayers['point guard'].append(player.player)
        if player.position == 'shooting guard':
            allplayers['shooting guard'].append(player.player)
        if player.position == 'small forward':
            allplayers['small forward'].append(player.player)
        if player.position == 'power forward':
            allplayers['power forward'].append(player.player)
        if player.position == 'center':
            allplayers['center'].append(player.player)

    return {'positions': allplayers}

@route_get(BASE_URL + 'leaders')
def statleaders(args):
    pointleader = Player.objects.order_by('-points').first()
    pointleader = pointleader.player

    assistleader = Player.objects.order_by('-assists').first()
    assistleader = assistleader.player

    reboundleader = Player.objects.order_by('-rebounds').first()
    reboundleader = reboundleader.player

    blockleader = Player.objects.order_by('-blocks').first()
    blockleader = blockleader.player
        
    stealleader = Player.objects.order_by('-steals').first()
    stealleader = stealleader.player

    statleaders = {
        'points': pointleader,
        'assists': assistleader,
        'rebounds': reboundleader,
        'blocks': blockleader,
        'steals': stealleader
    }

    return {'leaders': statleaders}



