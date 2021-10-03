# Biblioteka skirta grafinei vartotojo sasajai sukurti.
from tkinter import *
# Biblioteka naudojama perduoti metodams parametrus spaudziant mygtukus.
from functools import partial
from golay_execution import GolayExecution


class GolayWindow:
    """Programos grafines vartotojo sasajos klase.

    Klase apibrezia programos pagrindini langa ir jo elementus bei metodus, kurie dirba su lango elementais.
    """

    # Programos langas. Nebutinai pagrindinis.
    window = None
    # Golejaus kodo vykdymo klase.
    golayExecutor = None

    def __init__(self, golayExecutor: GolayExecution):
        """Konstruktoriaus metodas.

        GolayWindow klasei perduodama Golejaus kodo vykdymo klase GolayExecution.
        golayExecutor turi buti GolayExecution klases tipo kintamasis.
        """

        self.golayExecutor = golayExecutor

    def set_window_properties(self, width: int, height: int, title: str, center=True):
        """Metodas, kuris leidzia nurodyti lango ypatybes.

        width yra int tipo sveikasis skaicius, kuris nusako lango ploti pikseliais.
        height yra int tipo sveikasis skaicius, kuris nusako lango auksti pikseliais.
        title yra str tipo kintamasis, kuris nusako lango pavadinima.
        center yra bool tipo kintamasis. center pagal nutylejima yra True.
        Jeigu center yra True, tai lango pozicija pakeiciame i ekrano viduri.
        Jeigu center yra False, tai lango pozicija nekeiciama ir langas bus parodomas neapibreztoje
         vietoje atsitiktinai.
        """

        self.window.title(title)

        if center:
            # Gaunamas ekrano plotas ir aukstis.
            screenWidth = self.window.winfo_screenwidth()
            screenHeight = self.window.winfo_screenheight()

            # Suskaiciuojamos lango pozicijos koordinates.
            x = (screenWidth / 2) - (width / 2)
            y = (screenHeight / 2) - (height / 2)

            self.window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        else:
            self.window.geometry("%dx%d" % (width, height))

    def create_probability_window(self):
        """Konstruktoriaus metodas, kuris sukuria kanalo tikimybes nurodymo langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(400, 100, "Channel Distortion")

        # Ivestis ir mygtukas kanalo iskraipymo tikimybei.
        probEntry = Entry(self.window)
        probEntry.grid(row=0, column=0, columnspan=4, padx=50, pady=50)
        probEntry.insert(0, self.golayExecutor.get_distortion_probability())
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
