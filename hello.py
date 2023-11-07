import numpy as np
from turtle import Screen, Turtle


ITERATIONS = 10                       # total number of iterations
ROOT_COLOUR = np.array([129, 59, 9]) # root branch colour
LEAF_COLOUR = np.array([0, 255, 127])# leaf colour
TRUNK_LEN = 150                      # initial length of the trunk
TRUNK_RAD = 10.0                     # initial radius of the trunk
THETA = np.pi / 2                    # initial angle of the branch
ANGLE = np.pi / 4.5                  # angle between branches in the same level
PERTURB = 6.0                        # perturb the angle a little to make the tree look random
RATIO = 0.85                         # contraction factor between successive trunks
WIDTH = 700                          # image width
HEIGHT = 700                         # image height
ROOT = (0, -410)  

def get_colour(level):  # interpolates the two colours `ROOT_COLOUR` and `LEAF_COLOUR`.
    a = level / ITERATIONS
    colour = a * ROOT_COLOUR + (1 - a) * LEAF_COLOUR
    colour = np.rint(colour).astype(int)
    return( colour )

def get_line_width(level):
    return max(1, TRUNK_RAD * level / ITERATIONS)

def fractal_tree(turtle,      # turtle object
                 level,       # current level in the iterations
                 start,       # (x, y) coordinates of the start of this trunk
                 t,           # current trunk length
                 r,           # factor to contract the trunk in each iteration
                 theta,       # orientation of current trunk
                 angle,       # angle between branches in the same level
                 perturb):    # perturb the angle
    if level == 0:
        return

    x0, y0 = start
    if level == ITERATIONS:   # randomise except don't randomise the trunk length
        randt = 1.0 * t
    else:
        randt = np.random.uniform(0.05,1.0) * t
    x, y = x0 + randt * np.cos(theta), y0 + randt * np.sin(theta)

    colour = get_colour(level)
    turtle.up()
    turtle.goto(x0, y0)
    turtle.down()
    turtle.width(get_line_width(level))
    turtle.pencolor(colour)
    turtle.goto(x, y)

    theta1 = theta + np.random.random() * (perturb / level) * angle
    theta2 = theta - np.random.random() * (perturb / level) * angle
    # recursively draw the next branches
    fractal_tree(turtle, level - 1, (x, y), t * r, r, theta1, angle, perturb)
    fractal_tree(turtle, level - 1, (x, y), t * r, r, theta2, angle, perturb)


turt = Turtle()
turt.speed(0)
screen = Screen()
screen.setup(WIDTH, HEIGHT)
if ITERATIONS > 9:
    screen.tracer(False)       # don't show the turtle moving, we lack the patience
screen.colormode(255)
fractal_tree(turt, ITERATIONS, ROOT, TRUNK_LEN, RATIO, THETA, ANGLE, PERTURB)
screen.update()                # display what we have done now
screen.tracer(True)            # turn back on screen updates
turt.ht()                      # hide the turtle
