from tkinter import *

root = Tk()
root.attributes('-fullscreen', True)  # make main window full-screen

c = Canvas(root, bg='#454545', highlightthickness=0)
# configure canvas to occupy the whole main window
c.pack(fill=BOTH, expand=True)

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()


class Draw():
    global box_list
    box_list = []

    def box(self, x, y, a):
        c.create_rectangle((x - a/2, y - a/2), (x + a/2, y + a/2),
                               fill="#555555", outline="#777777", width=3)
        box_list.append((x, y))

    def board(self):
        X = WIDTH/2
        Y = HEIGHT/2
        a = (0.8*HEIGHT) / 3
        x = X - a
        y = Y - a
        for i in range(3):
            for j in range(3):
                self.box(x, y, a)
                x += a
            y += a
            x = X - a

    def circle(self, x, y, r, color):
        c.create_oval((x - r, y - r), (x + r, y + r),
                      fill=color, outline="black", width=1)
        a = (5*r)/6
        c.create_oval((x - a, y - a), (x + a, y + a),
                      fill="#555555", outline="black", width=1)

    def cross(self, x, y, r, color):
        c.create_line((x - r, y - r), (x + r, y + r), fill=color, width=4)
        c.create_line((x - r, y + r), (x + r, y - r), fill=color, width=4)


class Player():
    is_circle = True
    a = (0.8*HEIGHT) / 3
    r = a/4
    box_restricted = []

    def plant_tvar(self, pos):
        box_pos = None
        for i in box_list:
            if i[0] - self.a/2 + 1 < pos.x < i[0] + self.a/2 - 1:
                if i[1] - self.a/2 + 1 < pos.y < i[1] + self.a/2 - 1:
                    if i not in self.box_restricted:
                        box_pos = i
                        self.box_restricted.append(i)

        if box_pos != None:
            if self.is_circle:
                Draw().circle(box_pos[0], box_pos[1], self.r, "red")
                self.is_circle = not self.is_circle
            else:
                Draw().cross(box_pos[0], box_pos[1], self.r, "blue")
                self.is_circle = not self.is_circle


Draw().board()

# Binds
c.bind("<Button-1>", Player().plant_tvar)

root.mainloop()
