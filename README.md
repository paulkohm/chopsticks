# chopsticks
My kids play a game called "chopsticks". It's described at https://en.wikipedia.org/wiki/Chopsticks_(hand_game)

On vacation in June 2016, I talked to my kids about trying to create a computerized version of the game, to explore building
game AI.

Written in python 3, this requires only built-in libraries (copy and random).

The AI has been sort-of implemented in this version. It doesn't actually register moves, but for every single turn (both players), it calculates the best move and suggests it.

There are methods that begin with the word "strategy_" that allow for modularized AI strategies. For now, a randomized min/max seems to be the best bet.

I think we can embed some heuristics that my kids have developed to make it even stronger. It's not great for now, with a max_depth of 7, which is about all my laptop can handle with tolerable delays.

Thanks to http://www.ascii-art.de/ascii/def/finger.txt for the ascii art!
