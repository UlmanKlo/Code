from tkinter import *
import sympy


class Graph():
    def __init__(self, w, h, predpis) -> None:
        self.c = Canvas(width=w, height=h)
        self.width = w
        self.height = h
        self.predpis = predpis

    def definition_to_function(self, s):
        lhs, rhs = s.split("=", 1)
        rhs = rhs.rstrip('; ')
        args = sympy.sympify(lhs).args
        f = sympy.sympify(rhs)
        def f_func(*passed_args):
            argdict = dict(zip(args, passed_args))
            result = f.subs(argdict)
            return float(result)
        return f_func

    def build(self):
        self.c.pack()
        self.ox = self.width/2
        self.oy = self.height/2

        self.c.create_line((0, self.oy), (self.width, self.oy))
        self.c.create_line((self.ox, 0), (self.ox, self.height))
        
        f = self.definition_to_function(self.predpis)
        count = 1
        l = []
        for i in range(int(self.width/2 +1)):
            x = i*.1 + self.ox
            y = -f(i)*.1 + self.oy
            x += count*3
            y -= count*3
            if len(l) < 2:
                l.append((x, y))
            else:
                self.c.create_line((l[0][0], l[0][1]),( l[1][0], l[1][1]), fill="blue")
                l.reverse()
                l.pop()

            count += 1
        count = 1
        l = []
        for i in range(int(self.width/2 +1)):
            x = (-i)*.1 + self.ox
            y = -f(-i)*.1 + self.oy
            x -= count*3
            y += count*3
            if len(l) < 2:
                l.append((x, y))
            else:
                self.c.create_line((l[0][0], l[0][1]),( l[1][0], l[1][1]), fill="blue")
                l.reverse()
                l.pop()
            count += 1
    

        self.c.mainloop()


g = Graph(w=1000, h=800, predpis="f(x)=x**3")
g.build()

'''
for i in range(int(-self.width/2), int(self.width/2 + 1)):
            x = i*.25 + self.ox
            y = -f(i)*.25 + self.oy
            print(x, y)
            if x < self.width/2:
                x -= count*3
            else:
                x += count*3

            self.c.create_oval((x - 1, y - 1), (x + 1, y + 1))
            count += 1
'''