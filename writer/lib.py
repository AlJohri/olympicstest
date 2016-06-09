import os, requests
from boltons.iterutils import remap

SERVER=os.getenv('SERVER')

def preposition_phrase(x):
    return {
        "type": "preposition_phrase",
        "noun": x,
        "preposition": "over"
    }

def coordinated_phrase(players):
    return {
        "type": "coordinated_phrase",
        "conjunction": "and",
        "coordinates": [player.json() for player in players]
    }

def remove_empty_dicts(data):
    return remap(data, lambda p, k, v: v != {})

class MedalWon:

    def __init__(self, event, winners, losers=[], medal=""):
        self.event = event
        self.medal = medal
        self.winners = winners
        self.losers = losers

    def json(self):

        ret = {
            "subject": coordinated_phrase(self.winners),
            "verb": "won",
            "object": {
                "type": "noun_phrase",
                "head": self.medal + " medal",
                "determiner": "the"
            },
            "complements": [
                {
                    "type": "preposition_phrase",
                    "noun": {
                        "type": "noun_phrase",
                        "head": self.event,
                        "determiner": "the"
                    },
                    "preposition": "in"
                },
                preposition_phrase(coordinated_phrase(self.losers)) if len(self.losers) > 0 else {}
            ],
            "features": {"tense": "past"}
        }

        return remove_empty_dicts(ret)

    def realize(self):
        response = requests.post(SERVER + "/generateSentence", json={"sentence": self.json()})
        response.raise_for_status()
        return response.text

class Player:

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def json(self):
        # todo: specify as proper noun?
        return {
            "type": "noun_phrase",
            "head": self.name,
            "modifiers": [{
                "type": "preposition_phrase",
                "noun": { "type": "noun_phrase", "head": self.country },
                "preposition": "of"
            }]
        }