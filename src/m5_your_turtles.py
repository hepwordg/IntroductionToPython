"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Graham Hepworth.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
# Import RoseGraphics for ease of use
window = rg.TurtleWindow()
# Set the window to be simple and easy.
m = rg.SimpleTurtle('turtle')
n = rg.SimpleTurtle()
# Define the turtles
m.pen = rg.Pen('blue',3)
n.pen = rg.Pen('green',3)
# Color the turtles... trails?
m.speed = 5
n.speed = 10
# Set that speed
size = 40
for a in range(17):
    # Set size of circle
    m.draw_circle(size)
    #Force Circle to Conform and Repeat
    m.pen_up()
    m.forward(20)
    m.left(20)
    m.right(20) 

    m.pen_down()
    #I like this size because it goes negative
    size=size-5

for b in range(50):
    #Makes a zigzag
    n.forward(20)
    n.right(20)
    n.backward(20)
    n.left(20)

#You know why this is here
window.close_on_mouse_click()
