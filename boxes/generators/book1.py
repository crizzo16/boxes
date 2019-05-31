from boxes import *
import math

class Book1(Boxes):
    "Book box with flex spine, meant to be used with elastic to keep shut"

    ui_group = "Unstable"

    def __init__(self):
        Boxes.__init__(self)
        self.addSettingsArgs
        (edges.FingerJointSettings)
        self.buildArgParser("x", "y", "h")
        self.argparser.set_defaults(x=110.0,y=160.0,h=30.0)
        self.argparser.add_argument("--e_width", action="store", type=float, default=8, help="the width of the elastic you're using")
        self.argparser.add_argument("--closure", action="store", type=str, default="default (none)", choices=("default (none)", "elastic band", "wrap string"), help="Various closure option for box. Some require outside materials, such as elastic or string.")
    
    #def sidepieces(self, x, h, r, callback=None, move=None):
     #   self.moveTo(10, 15)
      #  self.edge(x - r)

    def cover(self, x, y, h, move=None):
        r = 0.5
        c2 = math.pi * h * 0.5
        t = self.thickness
        self.moveTo(r + t, t)
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
        self.fingerHolesAt(5, 5 + 0.5*t, x-5, 0)
        self.fingerHolesAt(5 + 0.5*t, 5+t, y-10-2*t, 90)
        self.fingerHolesAt(5, y - 5 - 0.5*t, x-5, 0)

    def sidepiece(self, x, h, callback=None, move=None):
        c2 = math.pi * h * 0.5
        t = self.thickness
        # 3.175 mm = 0.125 in (1/8")
        self.moveTo(2*x + c2 + 0.5*h + 3.175, 0)
        self.edges["f"](x-5, False)
        self.corner(90)
        self.edges["F"](h, False)
        self.corner(90)
        self.edges["e"](x-5, False)
        self.corner(180, h/2)

    def opposite(self, x, h, callback=None, move=None):
        t = self.thickness
        self.moveTo(-h/2, h + 2*t)
        self.edges["f"](x-5, False)
        self.corner(180, h/2)
        self.edges["e"](x-5, False)
        self.corner(90)
        self.edges["F"](h, False)
    
    def closurechoice(self, x, y, t, close, callback=None, move=None):
        if close=="elastic band":
            # draw holes in correct spot
            self.rectangularHole(15+t, t + 8, 8, 1)
            self.rectangularHole(t+15, y-t-8, 8, 1)
        elif close=="wrap string":
            # move to correct spot
            # make thing
            # self.circle(xpos, ypos, rad)
            self.circle(0.5*x, 10+t, 2)
            # move back to origin point

    def elasticHole(self, x, y, callback=None, move=None):
        t = self.thickness
        self.rectangularHole(15+t, t + 8, 8, 1)
        self.rectangularHole(t+15, y-t-8, 8, 1)
        #(x, y, dx, dy)


    def render(self):
        x, y, h, t, close = self.x, self.y, self.h, self.thickness, self.closure

        self.rectangularWall(self.h, self.y-10-(2*t), edges="feff", move="right")
        self.cover(self.x, self.y, self.h, move="right")
        self.closurechoice(x, y, t, close, callback=None, move="right")
        self.sidepiece(x, h, callback=None, move="right")
        self.opposite(x, h, callback=None, move="right")
        
        #self.rectangularHole(5, 5, 3, 5)
        