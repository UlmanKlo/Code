from tkinter import *
import re


class Graph():
    def __init__(self, w, h, predpis=str) -> None:
        self.c = Canvas(width=w, height=h)
        self.width = w
        self.height = h
        self.predpis = predpis

    def build(self):
        self.c.pack()
        self.ox = self.width/2
        self.oy = self.height/2

        self.c.create_line((0, self.oy), (self.width, self.oy))
        self.c.create_line((self.ox, 0), (self.ox, self.height))
        
        def spracuj_predpis(predpis):
            right_side = predpis[2:]
            return right_side
        
        p = spracuj_predpis(self.predpis)
        for i in range(100):
            x = i
            y = re.sub("x", str(i), p)
            if re.search("**", y) != None:
                y = re.sub("**", "^", p)
            print(y)
        
        self.c.mainloop()


g = Graph(w=1000, h=800, predpis="y=x**2")
g.build()
