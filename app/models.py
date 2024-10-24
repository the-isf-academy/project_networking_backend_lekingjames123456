# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Player(Model): #the model and what it contains
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
    active = BooleanField()

    def json_response(self): #this is what the user sees after they trigger a json response from the endpoints
        return {
            'player': self.player,
            'position': self.position,
            'matches_played': self.matchesplayed,
            'points': self.points,
            'assists': self.assists,
            'rebounds': self.rebounds,
            'steals': self.steals,
            'blocks': self.blocks,
            'active': self.active
        }
    
    def json_response_advanced(self): #this is what the user sees after they trigger a json response from the endpoints
        return{
            'player': self.player,
            'position': self.position,
            'matches_played': self.matchesplayed,
            'shots_taken': self.shotstaken,
            'shots_made': self.shotsmade,
            'threes_taken': self.threestaken,
            'threes_made': self.threesmade,
            'FG%': self.calculate_fg_percent(),
            '3PFG%': self.calculate_3pfg_percent(),
            'Plus_minus': self.plusminus
        }


    def calculate_fg_percent(self): #takes the shots made and divides it by the shots taken, then multiplies it by 100 to make it a percentage
        return self.shotsmade/self.shotstaken * 100
    
    
    def calculate_3pfg_percent(self): #takes the three pointers made and divides it by the three pointers taken, then multiplies it by 100 to make it a percentage
        return self.threesmade/self.threestaken * 100

    def add_stats(self, points, assists, rebounds, blocks, steals): #takes the stats the user inputs, then adds it to the existing stats
        self.points += points
        self.assists += assists
        self.rebounds += rebounds
        self.blocks += blocks
        self.steals += steals
        self.matchesplayed += 1
        self.save()

    def add_stats_advanced(self, shotstaken, threestaken, plusminus, shotsmade, threesmade): #takes the advanced stats the user inputs, then adds it to the existing advanced stats
        self.shotstaken += shotstaken
        self.threestaken += threestaken
        self.plusminus += plusminus
        self.shotsmade += shotsmade
        self.threesmade += threesmade
        self.matchesplayed += 1
        
        self.save()



    # def calculate_per_game_avg(self):                             #didn't work, but worth a try
    #     statslist = [self.points, self.assists, self.rebounds, self.blocks, self.steals]
    #     for stats in statslist:
    #         print(stats)
    #         stats = stats / self.matchesplayed
    #         stats = round(stats, 1)
    #         print(stats)
    #         self.save()
    #         print(self.points)

    def calculate_per_game_avg(self): #calculates their per game averages by taking how many points they have scored in total and divides it by how many matches they have played
        if self.points > 0: #makes sure that it's not dividing 0 by 0
            self.points = self.points / self.matchesplayed
            self.points = round(self.points, 2) #rounds it to 2 decimal places
        else:
            self.points = 0

        if self.assists > 0: #makes sure that it's not dividing 0 by 0
            self.assists = self.assists / self.matchesplayed
            self.assists = round(self.assists, 2) #rounds it to 2 decimal places
        else:
            self.assists = 0

        if self.rebounds > 0: #makes sure that it's not dividing 0 by 0
            self.rebounds = self.rebounds / self.matchesplayed
            self.rebounds = round(self.rebounds, 2) #rounds it to 2 decimal places
        else:
            self.rebounds = 0

        if self.blocks > 0: #makes sure that it's not dividing 0 by 0
            self.blocks = self.blocks / self.matchesplayed
            self.blocks = round(self.blocks, 2) #rounds it to 2 decimal places
        else:
            self.blocks = 0

        if self.steals > 0: #makes sure that it's not dividing 0 by 0       
            self.steals = self.steals / self.matchesplayed
            self.steals = round(self.steals, 2) #rounds it to 2 decimal places
        else:
            self.steals = 0

        self.save()
        

    def player_inactive(self): #sets a player inactive
        if self.active == True:
            self.active = False

        self.save()

    def player_active(self): #sets a player active after they are made inactive
        if self.active == False:
            self.active = True

        self.save()