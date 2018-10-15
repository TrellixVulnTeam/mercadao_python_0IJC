import tkinter


class Interface:

    def __init__(self, width, height):
        self.root = tkinter.Tk()
        self.root.geometry("" + str(width) + "x" + str(height) + "+500+100")

    def button(self, _x, _y, _text, **options):
        btn = tkinter.Button(self.root, text=_text, **options)
        btn.place(x=_x, y=_y)

    def label(self, _x, _y, _text, **options):
        lbl = tkinter.Label(self.root, text=_text, **options)
        lbl.place(x=_x, y=_y)

    def entry(self, _x, _y, _width, **options):
        ent = tkinter.Entry(self.root, width=_width, **options)
        ent.place(x=_x, y=_y)
        return ent

    def radio_group(self, _x, _y, names,**options):
        var = tkinter.IntVar()
        var.set(1)
        count = 1
        for name in names:
            rb = tkinter.Radiobutton(self.root, text=name, variable=var, value=count, **options)
            rb.place(x=_x, y=_y + 20 * count)
            count += 1

        return var

    def start(self):
        self.root.mainloop()
