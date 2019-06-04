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

        ################
        # bottom shelf #
        ################
        #box showing space
        
        #calculate degree using
        bsb = th*0.8
        deg = math.degrees(math.atan(bsb/(y-t)))
        extra = t*math.sin(math.pi/4)
        # calculate the bottom part of the triangle
        bsl = y-2*extra-2*t
        # calculate the side part of the triangle
        bst = th-2*extra
        # Calculate the hypotenuese of the the triangle (length of the piece)
        bsh = math.sqrt(bsl*bsl + bst*bst)
        self.fingerHolesAt(tl+t, t+extra*2, bsh, deg)
        
        ###########
        # Shelves #
        ###########
        sh = 30 # shelf height (each shelf's alloted height space)
        so = 0.55 # shelf overhang (percent of y)

        hr = h-th
        lvls = hr//sh
        left = (hr/sh)-lvls
        # These shelves extend 55% over depth of dice tower
        shadow = math.sqrt(so*so*y*y-sh*sh)
        ang = math.degrees(math.atan(sh/shadow))
        #shadow = 0.5*(80-2*t)
        #shadow = so*y

        for i in range(int(lvls)):
            # use i to determine which way it going
            # goes from 0 to lvls-1
            # use modulo % to calc if even or odd
            # even downhill \, odd uphill /
            # self.fingerHolesAt(xpos, ypos, length, deg)
            #ang=0
            # Downhill \, -ang
            if (i%2)==0:
                self.fingerHolesAt(tl+t, th+sh*(i+1)+t, so*y, -ang)
                #  self.moveTo(tl+t, th+sh*i)
                # self.edges["e"](shadow, False)
                #self.moveTo(-t-tl-shadow, -th-sh*i)
                self.moveTo(tl+t, th+i*sh)
                self.rectangularWall(shadow, sh, edges="eeee")
                self.moveTo(0, sh)
                self.corner(-ang)
                self.rectangularWall(so*y, t, edges="eeee")
                self.corner(ang)
                self.moveTo(-tl-t, -th-i*sh-sh)
            # Uphill /, ang
            else:
                self.fingerHolesAt(tl+(y-shadow-t-1), th+t+sh*i, so*y, ang)
                #   self.moveTo(tl+(y-shadow)-t, th+sh*i)
                # self.edges["e"](shadow, False)
                #self.moveTo(-tl-shadow-(y-shadow)+t, -th-sh*i)
                self.moveTo(tl+t+(y-shadow-2*t-1), th+i*sh)
                self.rectangularWall(shadow, sh, edges="eeee")
                self.corner(ang)
                self.rectangularWall(so*y, t, edges="eeee")
                self.corner(-ang)
                self.moveTo(-tl-t-y+shadow+2*t+1, -th-i*sh)
        #self.moveTo(tl+t, th+sh*lvls)
        #self.edges["e"](shadow, False)
        #self.moveTo(-t-tl-shadow, -th-sh*lvls)
                

    def shelves(self, y, x, h, th, t, tl, callback=None, move=None):
        self.moveTo(y+tl)
        # Bottom Shelf
        bsb = th*0.8
        deg = math.degrees(math.atan(bsb/(y-t)))
        extra = t*math.sin(math.pi/4)
        # calculate the bottom part of the triangle
        bsl = y-2*extra-2*t
        # calculate the side part of the triangle
        bst = th-2*extra
        bsh = math.sqrt(bsl*bsl + bst*bst)
        self.rectangularWall(x, bsh, edges="efef", move="right")

        ## Other Shelves
        amt = (h-th)//30
        hgt = 0
        for i in range(int(amt)):
            self.rectangularWall(x, 0.55*y, edges="efef", move="up")
                
        

            
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
        self.shelves(y, x, h, th, t, tl, move="right")
        #self.side2(y, h, tl, th, t, move="right")

       