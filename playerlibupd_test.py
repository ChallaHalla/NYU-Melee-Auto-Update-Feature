import challonge
from challonge import api
challonge.set_credentials("halla", "BvQ5HZNCquhDuKZN544EHh27LEhlBnP0Kwxwlomf")


import json


def update(tournament, match_id, **params):
    #Update/submit the score(s) for a match.
    api.fetch(
        "PUT",
        "tournaments/%s/matches/%s" % (tournament, match_id),
        "match",
        **params)
def index(tournament):
    """Retrieve a tournament's participant list."""
    return api.fetch_and_parse(
        "GET",
        "tournaments/%s/participants" % tournament)

def matchlist(tournament, **params):
    """Retrieve a tournament's match list."""
    return api.fetch_and_parse(
        "GET",
        "tournaments/%s/matches" % tournament,
        **params)
    
with open('players.txt') as json_data:
    players=json.load(json_data)

def playerlibupdate():
    for i in range(10):
        tournament_name="nyussbm%s" %i
        for j in index(tournament_name):
            if j not in players:
                players[j]={"Wins": [], "challonge-name":"", "temp-id": {}, "Losses":[], "tag":"" }
    
