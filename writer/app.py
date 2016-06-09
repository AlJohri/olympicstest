from lib import MedalWon, Player

"""
Carlo Molfetta of Italy won the gold medal in the men’s taekwondo 
80kg over Anthony Obame of Gabon. The fight ended tied on points, 9-9, 
but Molfetta was declared the winner by the judges on superiority.
"""

carlo = Player("Carlo Molfetta", "Italy")
anthony = Player("Anthony Obame", "Gabon")

medal_won = MedalWon(
    event="men's taekwondo 80kg",
    medal="gold",
    winners=[carlo],
    losers=[anthony])

print(medal_won.realize())
# "Carlo Molfetta of Italy won the gold medal in the men's taekwondo 80kg over Anthony Obame of Gabon."

# ----------------------------------------------------------------------------- #

# object of the sentence changed from "gold medal" before to "men's high jump"
"""
Ivan Ukhov of Russia won the men’s high jump with a leap of 2.38 meters, or 7 feet 9 3/4 inches.
"""

ivan = Player("Ivan Ukhov", "Russia")

medal_won = MedalWon(
    event="men’s high jump",
    medal="gold",
    winners=[ivan])
# Ivan Ukhov of Russia won the gold medal in the men’s high jump.

print(medal_won.realize())

# ----------------------------------------------------------------------------- #

"""
American Erik Kynard took silver with 2.33 meters (7 feet 7 3/4 inches).
"""

# as a second sentence, the prepositional phrase for the event goes away
# in this sentence, the direct object is the medal again

erik = Player("Erik Kynard", "America") # how to go from America -> American ?

medal_won = MedalWon(
    event="men’s high jump",
    medal="silver",
    winners=[erik])

print(medal_won.realize())
