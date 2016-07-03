# chopsticks
My kids play a game called "chopsticks". It's described at https://en.wikipedia.org/wiki/Chopsticks_(hand_game)

On vacation in June 2016, I talked to my kids about trying to create a computerized version of the game, to explore building
game AI.

Written in python 3, this requires only built-in libraries (copy and random).

doit.py is just a stub with the game loop. This is what you run. (% python3 doit.py)

AI is currently working. Two instance boolean variables called self.p1AI and self.p2AI currently hardcode whether each respective player is human or AI controlled. This should probably become a parameter to __init__ someday.

self.maxdepth (also in __init__) controls how deeply to go into the game tree. On my mid-range laptop, a value of 4 has no noticeable lag but still plays reasonably well.

There are methods that begin with the word "strategy_" that allow for modularized AI strategies. For now, a randomized min/max seems to be the best bet.

Currently, there is a little RNG in the current strategy, which together with a maxdepth of 4 means the AI is beatable.

I think we can embed some heuristics that my kids have developed to make it even stronger. It's not great for now, with a max_depth of 7, which is about all my laptop can handle with tolerable delays.

Thanks to http://www.ascii-art.de/ascii/def/finger.txt for the ascii art!
