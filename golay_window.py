# Biblioteka skirta grafinei vartotojo sasajai sukurti.
from tkinter import *
# Biblioteka naudojama perduoti metodams parametrus spaudziant mygtukus.
from functools import partial


class GolayWindow:
    """Programos grafines vartotojo sasajos klase.

    Klase apibrezia programos pagrindini langa ir jo elementus bei metodus, kurie dirba su lango elementais.
    """

    # Programos langas. Nebutinai pagrindinis
    window = None

    def create_probability_window(self):
        """Konstruktoriaus metodas, kuris sukuria kanalo tikimybes nurodymo langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.window.geometry("400x100")
        self.window.title("Channel Distortion")

        # Ivestis ir mygtukas kanalo iskraipymo tikimybei.
        probEntry = Entry(self.window)
        probEntry.grid(row=0, column=0, columnspan=4, padx=50, pady=50)
        probEntry.insert(0, "0.0")
        probButton = Button(self.window, padx=50)
        probButton.grid(row=0, column=4)
        self.window.mainloop()


    def create_main_window(self):
        """Metodas, kuris sukuria pagrindini programos langa ir pradeda lango cikla."""

        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.title("Golay Code")
        entry = Entry(self.window)
        entry.pack()
        entry.insert(0, "Enter your name:")
        myButton = Button(self.window, text="Enter your name", command=partial(self.my_click, entry))
        myButton.pack()
        self.window.mainloop()

    def my_click(self, entry):
        myLabel = Label(self.window, text="Hello " + entry.get())
        myLabel.pack()
