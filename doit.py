import chopsticks
import random

game = chopsticks.Chopsticks()
game.show()
while True:
    game.next()

    # Silly misdirection added by Max
    l = ['aq','aw','sq','sw', 'qa','wa','qs','ws']
    print ("Wait! I take it back! Do " + random.choice(l) + " instead.") 
