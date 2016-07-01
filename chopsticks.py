import showpair
from copy import copy

class Chopsticks(object):

    def __init__(self):
        self.state = [1, 1, 1, 1]
        self.p1sturn = True

    def show(self):
        showpair.show(self.state)

    def next(self):
        # Play the next turn
        # If it is a human's turn, prompt them for their move, verify it is a valid move, and change the state
        if self.p1sturn:
            print ("P1", end="")
        else:
            print ("P2", end="")
        move = input ("> ")
        if (self.testmove(move) > 0):
            self.show()
            self.p1sturn = not self.p1sturn
        self.testwin()

    def testwin(self):
        if self.state[0] + self.state[1] == 0:
            print ("Player Two Wins!!!! Sweg!")
        elif self.state[2] + self.state[3] == 0:
            print ("Player One Wins!!!! Sheer and utter reckation!")
        else:
            return

        print ("Thx for plzying!!!")
        exit()
            

    def testmove(self, move):
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

        # This function returns a newstate from self.state and move
        # It does error checking to ensure this is a valid move

        # Return value is either a newstate (presumed valid)
        # Or an error code

        # See if the move is a "tap" (against your opponent) or a "bump" (own hand)
        # This is complex given the representation for a move
        sort_move = move
        sort_move = ''.join(sorted(sort_move))
        print("sort_move is " + sort_move)
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
        if self.p1sturn:
            if not (from_hand == 'q' or from_hand == 'w'):
                print ("It's Player One's turn.")
                return -3
        else:
           if not (from_hand == 'a' or from_hand == 's'):
                print ("It's Player Two's turn.")
                return -3

        # Other tests, depending on tap or bump
        if move_type == "tap":
            # Test 1, if "from" hand is zero, error
            if self.state[mapper[from_hand]] == 0:
                print ("Invalid tap: 'from' hand is zero.")
                return -1
            
            # Test 2, if "to" hand is zero, error
            if self.state[mapper[to_hand]] == 0:
                print ("Invalid tap: 'to' hand is zero.")
                return -1
            
        elif move_type == "bump":
            
            # Test 1: disallow the 1 -> 0 bump
            if (self.state[mapper[from_hand]] + self.state[mapper[to_hand]]) == 1:
                print ("Invalid bump: bump with only one finger")
                return -2

            # Test 2: The from hand must be at least one
            if self.state[mapper[from_hand]] == 0:
                print ("Invalid bump: bump 'from' is zero.")
                return -2

            # Test 3: The from hand must have at least bumped fingers
            if self.state[mapper[from_hand]] < bumped:
                print ("Invalid bump: Not enough fingers on 'from' hand.")
                return -2

            # Test 4: The to hand plus bumped must not be greater than 4
            if self.state[mapper[to_hand]] + bumped  > 4:
                print ("Invalid bump: Overflow after bump.")
                return -2

        # Got here, so no errors in move. Calculate and return the newstate
        if move_type == "tap":
            self.state[mapper[to_hand]] += self.state[mapper[from_hand]]
        elif move_type == "bump":
            self.state[mapper[to_hand]] += bumped
            self.state[mapper[from_hand]] -= bumped

        # Modulo
        self.state[mapper[to_hand]] = self.state[mapper[to_hand]] % 5

        return 1
                          
game = Chopsticks()
game.show()
while True:
    game.next()
# game.next()
# print ("aq")
# game.testmove("aq")
# game.show()
# print("wa")
# game.testmove("wa")
# game.show()
# print ("qw")
# game.testmove("qw")
# game.show()
# print("as")
# game.testmove("as")
# game.show()
