# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Player(Model):
    player = StringField()
    position = StringField()
    points = FloatField()
    rebounds = FloatField()
    assists = FloatField()
    blocks = FloatField()
    steals = FloatField()
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
            'threes_taken': self.threestaken
            'threes_made': self.threesmade
            'FG%': self.calculate_fg_percent(),
            '3PFG%': self.calculate_3pfg_percent(),
            'Plus_minus': self.plusminus
        }


    def calculate_fg_percent(self):
        return self.shotsmade/self.shotstaken * 100
    
    
    def calculate_3pfg_percent(self):
        return self.threesmade/self.threestaken * 100

    def add_stats(self, points, assists, rebounds, blocks, steals):
        self.points += points
        self.assists += assists
        self.rebounds += rebounds
        self.blocks += blocks
        self.steals += steals
        self.matchesplayed += 1
        self.save()

    def add_stats_advanced(self, shotstaken, threestaken, shotsmade, threesmade, plusminus):
        self.shotstaken += shotstaken
        self.threestaken += threestaken
        self.shotsmade += shotsmade
        self.threesmade += threesmade
        self.plusminus += plusminus



    # def calculate_per_game_avg(self):
    #     statslist = [self.points, self.assists, self.rebounds, self.blocks, self.steals]
    #     for stats in statslist:
    #         print(stats)
    #         stats = stats / self.matchesplayed
    #         stats = round(stats, 1)
    #         print(stats)
    #         self.save()
    #         print(self.points)

    def calculate_per_game_avg(self):
        self.points = self.points / self.matchesplayed
        self.assists = self.assists / self.matchesplayed
        self.rebounds = self.rebounds / self.matchesplayed
        self.blocks = self.blocks / self.matchesplayed
        self.steals = self.steals / self.matchesplayed
        self.save()
        