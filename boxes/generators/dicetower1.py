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

    def side(self, y, h, tl, th, t, callback=None, move=None):
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
        #z = t*math.cos(math.radians(theta))
        #where theta is the angle of the shelf
        #that's the extra length added to one side when tilted
        #w = t*math.sin(math.radians(theta))
        #that's the extra length added to the bottom
        #worst added when at 45 deg


        #bottom shelf
        #calculate degree using
        deg = math.degrees(math.atan(th/y))
        bsl = y - t*math.sin(math.pi/4)
        bst = th - t*math.sin(math.pi/4)
        bsh = math.sqrt(bsl*bsl + bst*bst)
        self.fingerHolesAt(tl, t, bsh, deg)
        self.moveTo(tl + y + 3.175, 0)

    def shelves(self, y, x, h, th, t, callback=None, move=None):
        bsl = y - t*math.sin(math.pi/4)
        bst = th - t*math.sin(math.pi/4)
        bsh = math.sqrt(bsl*bsl + bst*bst)
        self.rectangularWall(x, bsh, edges="efef", move="right")

    def side2(self, y, h, tl, th, t, callback=None, move=None):
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
        x, y, h, tl, th, t = self.x, self.y, self.h, self.tray_length, self.tray_depth, self.thickness
        

        # The base 
        self.rectangularWall(x, y+tl, edges="ffff", move="right")

        # The back wall
        self.rectangularWall(x, h, edges="Ffef", move="right")

        #The front wall
        self.rectangularWall(x, h-th, edges="efef", move="right")

        # The side walls
        self.side(y, h, tl, th, t, move="right")
        self.shelves(y, x, h, th, t, move="right")
        #self.side2(y, h, tl, th, t, move="right")

       