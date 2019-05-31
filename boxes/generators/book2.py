from boxes import *
import math

class Book2(Boxes):
    "Book box with flex spine, and a simple gear mechanic for the opening/closure"

    ui_group = "Unstable"

    def __init__(self):
        Boxes.__init__(self)
        self.addSettingsArgs
        (edges.FingerJointSettings)
        self.buildArgParser("x", "y", "h")
        self.argparser.set_defaults(x=110.0,y=160.0,h=30.0)

    # The Cover of the book
    def cover(self, x, y, h, move=None):
        r = 0.5
        c2 = math.pi * h * 0.5
        self.moveTo(r + self.thickness, self.thickness)
        self.edge(x - r)
        self.edges["X"](c2, y)
        self.edge(x - r)
        self.corner(90, r)
        self.edge(y - 2 * r)
        self.corner(90, r)
        self.edge(2 * x - 2 * r + c2)
        self.corner(90, r)
        self.edge(y - 2 * r)
        self.corner(90,r)

    # One side of the book (with a curved end)
    def sidepiece(self, x, h, callback=None, move=None):
        t = self.thickness
        self.moveTo(2*t + h, .25*t)
        self.edges["f"](x-5, False)
        self.corner(90)
        self.edges["F"](h, False)
        self.corner(90)
        self.edges["e"](x-5, False)
        self.corner(180, h/2)

    # The mirror of the piece above
    def opposite(self, x, h, callback=None, move=None):
        t = self.thickness
        self.moveTo(-h/2, h + 2*t)
        self.edges["f"](x-5, False)
        self.corner(180, h/2)
        self.edges["e"](x-5, False)
        self.corner(90)
        self.edges["F"](h, False)

    # The connector that holds the walls together for the front mechanism
    def connector(self, h, callback=None, move=None):
        t = self.thickness
        self.rectangularWall(3*t, h*0.3, edges="eeee", move="right")

    # Circles holding gear
    def circles(self, h, callback=None, move=None):
        t = self.thickness
        self.moveTo(t, t)
        self.corner(360, (1/3)*h)
        # make cross in the center of the circle

    # Gear responsible for the magic
    def sun(self, h, callback=None, move=None):
        self.rectangularWall(2, 2, edges="eeee")
        
    # The walls holding the locking mechanism in
    def smallwalls(self, h, y, callback=None, move=None):
        self.rectangularWall(y*.6, h, edges="eeee")


    # Put it all together
    def render(self):
        x, y, h = self.x, self.y, self.h
        t = self.thickness

        self.cover(self.x, self.y, self.h, move="right")
        self.rectangularWall(self.y-10-(2*t), self.h, edges="ffef", move="right")
        self.sidepiece(x, h, callback=None, move="right")
        self.opposite(x, h, callback=None, move="right")