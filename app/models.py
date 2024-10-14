# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Stats(Model):
    player = StringField()
    position = StringField()
    points = IntegerField()
    rebounds = IntegerField()
    assists = IntegerField()
    blocks = IntegerField()
    steals = IntegerField()
    shotstaken = IntegerField()
    shotsmade = IntegerField()
    threestaken = IntegerField()
    threesmade = IntegerField()
    matchesplayed = IntegerField()
    plusminus = IntegerField()
    mvp = IntegerField()
    active = BooleanField()

    def json_response(self):
        return {
            'player': self.player,
            'position': self.position,
            'matches_played': self.matchesplayed,
            'points': self.points,
            'assists': self.assists,
            'rebounds': self.rebounds,
            'steals': self.steals,
            'blocks': self.blocks,
            'MVPs': self.mvp,
            'active': self.active
        }
    
    def json_response_advanced(self):
        return{
            'player': self.player,
            'position': self.position,
            'matches_played': self.matchesplayed,
            'shots_taken': self.shotstaken,
            'shots_made': self.shotsmade,
            'FG%': self.calculate_fg%(),
            '3PFG%': self.calculate_3pfg%(),
            'Plus_minus': self.plusminus
        }


    def calculate_fg%(self):
        return self.shotsmade/self.shotstaken * 100
    
    
    def calculate_3pfg%(self):
            return self.threesmade/self.threestaken * 100

