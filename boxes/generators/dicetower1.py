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
        # calculate bottom shelf length
        bsl = y - t*math.sin(math.pi/4)
        bst = th - t*math.sin(math.pi/4)
        # Calculate 
        bsh = math.sqrt(bsl*bsl + bst*bst)
        self.fingerHolesAt(tl, t, bsh, deg)
        self.moveTo(0, 0)

        sh = 30 # shelf height (each shelf's alloted height space)
        so = 0.55 # shelf overhang (percent of y)

        hr = h-th
        lvls = hr//sh
        left = (hr/sh)-lvls
        # These shelves extend 55% over depth of dice tower
        ang = math.degrees(math.atan(sh/(so*y)))
        shadow = math.sqrt(so*so*y*y-sh*sh)
        #shadow = 0.5*(80-2*t)

        for i in range(int(lvls)):
            # use i to determine which way it going
            # goes from 0 to lvls-1
            # use modulo % to calc if even or odd
            # even downhill \, odd uphill /
            # self.fingerHolesAt(xpos, ypos, length, deg)
            #ang=0
            # Downhill \, -ang
            if (i%2)==0:
                self.fingerHolesAt(tl+t, th+t+sh*(i+1), so*y, -ang)
                self.moveTo(tl+t, th+sh*i)
                self.edges["e"](shadow, False)
                self.moveTo(-t-tl-shadow, -th-sh*i)
            # Uphill /, ang
            else:
                self.fingerHolesAt(tl+(1-so)*y-t, th+t+sh*i, so*y, ang)
                self.moveTo(tl+(y-shadow)-t, th+sh*i)
                self.edges["e"](shadow, False)
                self.moveTo(-tl-shadow-(y-shadow)+t, -th-sh*i)
        self.moveTo(tl+t, th+sh*lvls)
        self.edges["e"](shadow, False)
        self.moveTo(-t-tl-shadow, -th-sh*lvls)
                

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
        #self.shelves(y, x, h, th, t, move="right")
        #self.side2(y, h, tl, th, t, move="right")

       