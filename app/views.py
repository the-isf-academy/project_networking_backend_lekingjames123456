# views.py

from banjo.urls import route_get, route_post
from .models import Player
from settings import BASE_URL

@route_post(BASE_URL + 'new', args={'player':str, 'position':str}) #creates a new player
def newplayer(args):
    if Player.objects.filter(player=args['player'], active = True).exists():
        return {'error': 'player is already in the API'}
    else:
        newplayer = Player(  #creates the new player with their name and position
            player = args['player'],
            position = args['position'],
            active = True
        )
        
        newplayer.save()

        return {'player info': newplayer.json_response()}

@route_get(BASE_URL + 'stats', args={'player':str}) #gets the stats of a player
def playerstats(args):
    if Player.objects.filter(player=args['player'], active = True).exists():
        playerstats = Player.objects.get(player=args['player'])
        playerstats.calculate_per_game_avg()

        return {'player info': playerstats.json_response()}

    else:
        return {'error': 'no player exists'}

@route_get(BASE_URL + 'stats/advanced', args={'player':str})
def advancedstats(args):
    if Player.objects.filter(player=args['player'], active = True).exists():
        advancedstats = Player.objects.get(player=args['player'])

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

    for player in Player.objects.filter(active = True):
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
def statleader(args):
    pointleader = Player.objects.filter(active = True).order_by('-points').first()
    pointleader = pointleader.player, pointleader.points

    assistleader = Player.objects.filter(active = True).order_by('-assists').first()
    assistleader = assistleader.player, assistleader.assists

    reboundleader = Player.objects.filter(active = True).order_by('-rebounds').first()
    reboundleader = reboundleader.player, reboundleader.rebounds

    blockleader = Player.objects.filter(active = True).order_by('-blocks').first()
    blockleader = blockleader.player, blockleader.blocks
        
    stealleader = Player.objects.filter(active = True).order_by('-steals').first()
    stealleader = stealleader.player, stealleader.steals

    statleaders = {
        'points': pointleader,
        'assists': assistleader,
        'rebounds': reboundleader,
        'blocks': blockleader,
        'steals': stealleader
    }

    return {'leaders': statleaders}

@route_post(BASE_URL + 'input_stats', args={'player':str, 'points':float, 'assists':float, 'rebounds':float, 'blocks':float, 'steals':float})
def addstats(args):
    if Player.objects.filter(player=args['player'], active = True).exists():
        addstats = Player.objects.get(player=args['player'])
        points_input = args['points']
        assists_input = args['assists']
        rebounds_input = args['rebounds']
        blocks_input = args['blocks']
        steals_input = args['steals']
        addstats.add_stats(points_input, assists_input, rebounds_input, blocks_input, steals_input)

        return {'success': 'stats successfully added"'}

    else:
        return {'error': 'no player exists'}

@route_post(BASE_URL + 'input_stats_advanced', args={'player':str, 'shotstaken':int, 'threestaken':int, 'plusminus':int, 'shotsmade':int, 'threesmade':int})
def addadvancedstats(args):
    if Player.objects.filter(player=args['player'], active = True).exists():
        addadvancedstats = Player.objects.get(player=args['player'])
        shots_taken = args['shotstaken']
        threes_taken = args['threestaken']
        plusminus_player = args['plusminus']
        shots_made = args['shotsmade']
        threes_made = args['threesmade']
        addadvancedstats.add_stats_advanced(shots_taken, threes_taken, plusminus_player, shots_made, threes_made)

        return {'success': 'stats successfully added"'}

    else:
        return {'error': 'no player exists'}

@route_post (BASE_URL + 'set_inactive', args={'player':str}) #sets an active player inactive
def playerinactive(args):
    if Player.objects.filter(player=args['player'], active = True).exists():
        playerinactive = Player.objects.get(player=args['player'])
        playerinactive.player_inactive()
        return {'success': 'player has been successfully deleted'}
    
    else:
        return {'error': 'no player exists'}

@route_post (BASE_URL + 'set_active', args={'player':str}) #sets an previously inactive player active
def playeractive(args):
    if Player.objects.filter(player=args['player'], active = False).exists():
        playeractive = Player.objects.get(player=args['player'])
        playeractive.player_active()
        return {'success': 'player has been successfully restored'}
        
    else:
        return {'error': 'no player exists or the player is already active'}
