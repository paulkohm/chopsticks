# Plays the kids' game chopsticks.
# A little foray into AI.

def mirror (art):
    # Given a multi-line ascii art image
    # return the mirror image (meaning flipped right to left)

    # This isn't needed generically, but for these images, all / and \ characters need to be swapped.
    art = art.replace("\\", "XXX")
    art = art.replace("/", "\\")
    art = art.replace("XXX", "/")

    # Pythonic one-liner to flip multiline strings left-to-right
    return "\n".join([x[::-1] for x in art.split('\n')])

def flip (art):
    # Given a multi-line ascii art image
    # return the mirror image (meaning flipped right to left)

    # This isn't needed generically, but for these images, all / and \ characters need to be swapped.
    art = art.replace("\\", "XXX")
    art = art.replace("/", "\\")
    art = art.replace("XXX", "/")

    # A few more replacements to make it look right
    art = art.replace(".", "'")
    art = art.replace("`", ",")
    art = art.replace("_", "-")

    return "\n".join(x for x in art.split('\n')[::-1])

def compose (art1, art2):
    # Given two multi-line ascii art images
    # print them side-by-side
    # with a few spaces in between
    SPACES = "   "

    return "\n".join([i1 + SPACES + i2 for i1, i2 in zip(art1.split('\n'), art2.split('\n'))])
        

def showpair (left, right, p1 = False):
    IMAGES = [
        """
            
            
            
            
    _.-._   
   | | | |-.
  /|     ` |
 | |       |
 |         |
 \         /
  |       | 
  |       | 
""",
    """
            
   .-.      
   |U|      
   | |      
   | |-._   
   | | | |-.
  /|     ` |
 | |       |
 |         |
 \         /
  |       | 
  |       | 
""",
    """
     .-.    
   .-|U|    
   |U| |    
   | | |    
   | | |_   
   | | | |-.
  /|     ` |
 | |       |
 |         |
 \         /
  |       | 
  |       | 
""",
   """
     .-.    
   .-|U|-.  
   |U| |U|  
   | | | |  
   | | | |  
   | | | |-.
  /|     ` |
 | |       |
 |         |
 \         /
  |       | 
  |       | 
""",
   """
     .-.    
   .-|U|-.  
   |U| |U|  
   | | | |-.
   | | | |U|
   | | | | |
  /|     ` |
 | |       |
 |         |
 \         /
  |       | 
  |       | 
"""
    ]

    if p1:
        print (compose(mirror(flip(IMAGES[left])), flip(IMAGES[right])))
    else:
        print (compose(mirror(IMAGES[left]), IMAGES[right]))

def show(state):
    # Given the game state, display the current game board
    # Player 1
    showpair(state[0], state[1], True)
    # Player 2
    showpair(state[2], state[3])
