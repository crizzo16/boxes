from boxes import *
import math

class Book3(Boxes):
    "Book box with flex spine, no indentation for the pages"

    ui_group = "Unstable"

    def __init__(self):
        Boxes.__init__(self)
        self.addSettingsArgs
        (edges.FingerJointSettings)
        self.buildArgParser("x", "y", "h")
        self.argparser.set_defaults(x=110.0,y=160.0,h=30.0)
        self.argparser.add_argument(
            "--hole", action="store", type=str, default="default (none)", choices=("default (none", "top lid", "bottom lid", "top base", "bottom base"), help="hole to add string closure"
        )

    def cover(self, x, y, h, hole, move=None):
        r = 0.5
        t = self.thickness
        c2 = math.pi * h * 0.5
        self.moveTo(3.175, 2*t)
        #self.edge(x)
        #self.edges["X"](c2, y)
        #self.edges["F"](x, False)
        #self.corner(90)
        #self.edges["F"](y, False)
        #self.corner(90)
        #self.edges["F"](x, False)
        #self.edge(x + c2) 
        #self.corner(90)
        #self.edge(y)
        #self.corner(90)

        self.edges["F"](x, False)
        self.edges["X"](c2, y)
        self.edge(x)
        self.corner(90)
        self.edge(y)
        self.corner(90)
        self.edge(x + c2)
        self.edges["F"](x, False)
        self.corner(90)
        self.edges["F"](y, False)
        self.corner(90)
        
        #if (self.hole == "top lid")
        if hole == "bottom base":
            self.moveTo(0.5*x, 3+t)
            self.corner(360, 2)
            self.moveTo(-0.5*x, -3-t)
        elif hole == "top base":
            self.moveTo(0.5*x, y-t-6)
            self.corner(360, 2)
            self.moveTo(-0.5*x, 6+t-y)
        elif hole == "top lid":
            self.moveTo(1.5*x + c2, y-t-6)
            self.corner(360, 2)
            self.moveTo(-1.5*x - c2, 6+t-y)
        elif hole == "bottom lid":
            self.moveTo(1.5*x + c2, 3+t)
            self.corner(360, 2)
            self.moveTo(-1.5*x- c2, -3-t)
        
        self.moveTo(-(x*.5), 0)

    def sidepiece(self, x, h, callback=None, move=None):
        t = self.thickness
        cw = math.pi*0.5*h + 2*x
        self.moveTo(3.175*2 + 2*h + cw, 0)
        
        self.edges["F"](h, False)
        self.corner(90)
        self.edges["e"](x, False)
        self.corner(180, h/2)
        self.edges["f"](x, False)
        self.corner(90)

    def opposite(self, x, h, callback=None, move=None):
        t = self.thickness
        self.moveTo(h + 3.175,0)
        self.edges["F"](h, False)
        self.corner(90)
        self.edges["f"](x, False)
        self.corner(180, h/2)
        self.edges["e"](x, False)
        self.corner(90)
        
        


    def render(self):
        x, y, h, t, hole = self.x, self.y, self.h, self.thickness, self.hole

        
        #self.rectangularWall(self.y, self.h, edges="ffef", move="right")
        self.rectangularWall(h, y, edges="feff", move="right")
        self.cover(x, y, h, hole, move="right")
        self.sidepiece(x, h, callback=None, move="right")
        self.opposite(x, h, callback=None, move="right")