from boxes import *
import math

class DiceTower(Boxes):
    """Simple dice tower with built in tray"""

    ui_group = "Unstable"

    def __init__(self):
        Boxes.__init__(self)

        self.buildArgParser("x", "y", "h")
        self.argparser.set_defaults(x=100.0, y=80.0, h=180.0)
        self.argparser.add_argument("--tray_length", action="store", type=float, default=100, help="The tray has the same width (x) has the tower, but it's own length")
        self.argparser.add_argument("--tray_depth", action="store", type=float, default=50, help="The depth of the tray")

    def side(self, y, h, tl, th, callback=None, move=None):
        self.edges["F"](y+tl, False)
        self.corner(90)
        self.edges["F"](h, False)
        self.corner(90)
        self.edges["e"](y, False)
        self.corner(90)
        self.edges["F"](h-th, False)
        self.corner(-90)
        self.edges["e"](tl, False)
        self.corner(90)
        self.edges["F"](th, False)
        self.corner(90)

        #add the holes for the shelves

        #bottom shelf
        #calculate degree using
        deg = math.degrees(math.atan(th/y))
        self.fingerHolesAt(tl, 0, 0.8*math.sqrt(th*th + y*y), deg)

    def side2(self, y, h, tl, th, callback=None, move=None):
        self.edges["F"](y+tl, False)
        self.corner(90)
        self.edges["F"](th, False)
        self.corner(90)
        self.edges["e"](tl, False)
        self.corner(-90)
        self.edges["F"](h-th, False)
        self.corner(90)
        self.edges["e"](y, False)
        self.corner(90)
        self.edges["F"](h, False)
        self.corner(90)



    def render(self):
        x, y, h, tl, th = self.x, self.y, self.h, self.tray_length, self.tray_depth
        

        # The base 
        self.rectangularWall(x, y+tl, edges="ffff", move="right")

        # The back wall
        self.rectangularWall(x, h, edges="Ffef", move="right")

        #The front wall
        self.rectangularWall(x, h-th, edges="efef", move="right")

        # The side walls
        self.side(y, h, tl, th, move="right")
        #self.side2(y, h, tl, th, move="right")

       