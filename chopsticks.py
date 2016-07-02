import showpair
from copy import copy

DEBUG = False

class Chopsticks(object):

    def __init__(self):
        self.state = [1, 1, 1, 1]
        #self.state = [1, 4, 0, 1]
        self.p1sturn = True
        self.maxdepth = 6
        self.pastmoves = {}

    def debugprint(self, toprint):
        if DEBUG:
            print (toprint)

    def show(self):
        showpair.show(self.state)

    def ai(self):
        # Given the current state, and assuming it is the CPU's turn,
        # start the minimax algorithm
        seed = self.state_seed(self.state)
        seedplusplayer = seed
        if self.p1sturn:
            seedplusplayer = str(seed) + "/" + "1"
        else:
            seedplusplayer = str(seed) + "/" + "2"

        print ("seedplusplayer is " + seedplusplayer)
        print ("pastmoves: ")
        print (self.pastmoves)
        # Efficiency move: If we've already evaluated this tree, just go with the prior move.
        if seedplusplayer in self.pastmoves:
            print ("A game board we've seen before. Bypassing the tree.")
            print ("Last time we suggested move " + self.pastmoves[seedplusplayer] + "\n")
        
        if (seed == 1111):
            print ("Matches the initial state, so I'm not going to minimax it.")
            print ("Just go with qa!")
            self.pastmoves[seedplusplayer] = "qa"
            return (0, "qa")

        suggestion = self.minimax(self.state, self.p1sturn, [])
        self.pastmoves[seedplusplayer] = suggestion[1]

        return(suggestion)

    def score(self, state):
        if state[0] + state[1] == 0:
            return -10
        elif state[2] + state[3] == 0:
            return 10
        else:
            return 0

    def state_seed2 (self, state):
        # Returns a compact integer reflecting the current state of the board.
        # Algorithm: Use prime numbers to encode four slots
        multipliers = [2, 3, 5, 7]
        total = 1
        
        for x,y in zip(state, multipliers):
            # Must +1 to convert 0 to 1
            total = total * (x + 1) * y
            
        return total

    def state_seed (self, state):
        # Turns a list into a four digit number reflecting the current state of the board.
        return int(''.join([str(i) for i in state]))

    def minimax(self, state, p1sturn, seen):
        # Returns a tuple with (score, move)
        
        self.debugprint ("\ntop of minimax")
        self.debugprint (state)
        self.debugprint (p1sturn)
        self.debugprint (seen)
        score = self.score(state)
        if score != 0:
            self.debugprint ("* Score is " + str(score) + ". Branch terminating.\n")
            return (score, "")

        seed = self.state_seed(state)
        self.debugprint (seed)

        if seed in seen:
            # Loop, so return a 0
            self.debugprint ("* Loop! Branch terminating.\n")
            return (0, "")
        
        if len(seen) > self.maxdepth:
            self.debugprint("* maxdepth reached!! Branch Terminating.\n")
            return(0, '')
        
        newseen = copy(seen)
        newseen.append(seed)

        mapper = {
            'a' : 2,
            's' : 3,
            'q' : 0,
            'w' : 1
        }

        moves = []
        scores = []

        # p1 looks for max, and p2 looks for min, so make invalid_score the opposite
        invalid_score = 20

        # Generate list of possible moves for current player
        if (p1sturn):
            moves = ["qa", "qs", "wa", "ws"]
            for hand in [("q", "w"), ("w", "q")]:
                for i in range(0, state[mapper[hand[0]]]):
                    moves.append(hand[0] + hand[1] + str(i + 1))
            invalid_score *= -1
        else:
            # p2sturn
            moves = ["aq", "sq", "aw", "sw"]
            for hand in [("a", "s"), ("s", "a")]:
                for i in range(0, state[mapper[hand[0]]]):
                    moves.append(hand[0] + hand[1] + str(i + 1))
                    
        self.debugprint ("If this were AI, this would be the moves:")
        self.debugprint (moves)
        self.debugprint ("And this is the seen list")
        self.debugprint (newseen)

        # Starting to recurse
        for move in moves:
            self.debugprint("Trying move " + move + " with state ")
            self.debugprint(state)
            nextstate = self.testmove(state, move, p1sturn)
            if (nextstate[0] > -1):
                self.debugprint ("returned a valid board. recurse on it.")
                scores.append(self.minimax(nextstate, not p1sturn, newseen)[0])
            else:
                # Invalid move, so make score for this one just 0
                self.debugprint ("invalid move")
                self.debugprint (nextstate[1])
                self.debugprint ("* Branch terminating.\n")
                scores.append(invalid_score)
                
        print ("Scores are:")
        print (scores)
        print ("Moves are:")
        print (moves)
        print ("Best score is " + str(invalid_score * -1))

        # Figure out which to return. Return should be the move chosen.
        if (p1sturn):
            win_func = max
        else:
            win_func = min
            
        win_val = win_func(scores)
        win_index = scores.index(win_val)
        self.debugprint ("** Done with branch. Best move for current player is " + str(moves[win_index]) + " with value = " + str(win_val) + "\n\n")
        return (win_val, moves[win_index])

    def next(self):
        # Play the next turn
        
        # Just temporary:
        best_move = self.ai()
        print ("*** Best move seems to be " + best_move[1])

        self.debugprint ("seed is " + str(self.state_seed(self.state)))
        self.show()
        
        # If it is a human's turn, prompt them for their move, verify it is a valid move, and change the state
        if self.p1sturn:
            print ("P1", end="")
        else:
            print ("P2", end="")
        move = input ("> ")
        newstate = self.testmove(self.state, move, self.p1sturn)
        if (newstate[0] > -1):
            self.state = copy(newstate)
            self.show()
            self.p1sturn = not self.p1sturn
            self.testwin()
        else:
            print (newstate[1])

    def testwin(self):
        if self.state[0] + self.state[1] == 0:
            print ("Player Two Wins!!!! Sweg!")
        elif self.state[2] + self.state[3] == 0:
            print ("Player One Wins!!!! Sheer and utter reckation!")
        else:
            return

        print ("Thx for plzying!!!")
        exit()
            
    def testmove(self, state, move, p1sturn):
        # The internal representation of a move is a two letter combination
        # with an optional number
        # The letters refer to following square on the keyboard:
        # q = top left
        # w = top right
        # a = bottom left
        # s = bottom right

        # So:
        # aw = from bottom left to top right
        # qa = from top left to bottom left
        # as3 = from bottom left to bottom right (bump)
        # In the final example, the 3 is the number of fingers you are bumping

        # This function returns a newstate from state and move
        # It does error checking to ensure this is a valid move

        # Return value is either a newstate (presumed valid)
        # Or an error code

        # See if the move is a "tap" (against your opponent) or a "bump" (own hand)
        # This is complex given the representation for a move
        sort_move = move
        sort_move = ''.join(sorted(sort_move))
        if sort_move == "aq" or sort_move == "sw" or sort_move == "aw" or sort_move == "qs":
            move_type = "tap"
        else:
            move_type = "bump"

        from_hand = move[0]
        to_hand = move[1]
        bumped = 1
        
        if (len(move) > 2):
            bumped = int(move[2])

        mapper = {
            'a' : 2,
            's' : 3,
            'q' : 0,
            'w' : 1
        }

        # Test 0: Make sure the right player has played
        if p1sturn:
            if not (from_hand == 'q' or from_hand == 'w'):
                return [-3, "It's Player One's turn."]
        else:
           if not (from_hand == 'a' or from_hand == 's'):
                return [-3, "It's Player Two's turn."]

        # Other tests, depending on tap or bump
        if move_type == "tap":
            # Test 1, if "from" hand is zero, error
            if state[mapper[from_hand]] == 0:
                return [-1, "Invalid tap: 'from' hand is zero."]
            
            # Test 2, if "to" hand is zero, error
            if state[mapper[to_hand]] == 0:
                return [-1, "Invalid tap: 'to' hand is zero."]
            
        elif move_type == "bump":
            
            # Test 1: disallow the 1 -> 0 bump
            if (state[mapper[from_hand]] + state[mapper[to_hand]]) == 1:
                return [-2, "Invalid bump: bump with only one finger"]

            # Test 2: The from hand must be at least one
            if state[mapper[from_hand]] == 0:
                return [-2, "Invalid bump: bump 'from' is zero."]

            # Test 3: The from hand must have at least bumped fingers
            if state[mapper[from_hand]] < bumped:
                return [-2, "Invalid bump: Not enough fingers on 'from' hand."]

            # Test 4: The to hand plus bumped must not be greater than 4
            if state[mapper[to_hand]] + bumped > 4:
                return [-2, "Invalid bump: Overflow after bump."]

        # Got here, so no errors in move. Calculate and return the newstate
        newstate = copy(state)
        if move_type == "tap":
            newstate[mapper[to_hand]] += newstate[mapper[from_hand]]
        elif move_type == "bump":
            self.debugprint ("In bump.")
            newstate[mapper[to_hand]] += bumped
            newstate[mapper[from_hand]] -= bumped

        # Modulo
        newstate[mapper[to_hand]] = newstate[mapper[to_hand]] % 5

        return newstate
                          
