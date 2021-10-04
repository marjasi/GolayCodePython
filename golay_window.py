# Biblioteka skirta grafinei vartotojo sasajai sukurti.
from tkinter import *
# Biblioteka naudojama perduoti metodams parametrus spaudziant mygtukus.
from functools import partial
from golay_execution import GolayExecution
# Biblioteka naudojama patikrinti ivesciu tinkamuma naudojant regex.
import re


# if re.fullmatch("[01][01][01][01][01][01][01][01][01][01][01][01]", probEntry.get()) is not None:

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

    def set_window_properties(self, width: int, height: int, title: str, columnspan: int, rowspan: int, center=True):
        """Metodas, kuris leidzia nurodyti lango ypatybes.

        width yra int tipo sveikasis skaicius, kuris nusako lango ploti pikseliais.
        height yra int tipo sveikasis skaicius, kuris nusako lango auksti pikseliais.
        title yra str tipo kintamasis, kuris nusako lango pavadinima.
        columnspan yra int tipo sveikasis skaicius, kuris nusako lango lenteles (grid) stulpeliu skaiciu.
        rowspan yra int tipo sveikasis skaicius, kuris nusako lango lenteles (grid) eiluciu skaiciu.
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

        # Lange esancios nematomos lenteles konfiguracija.
        Canvas(self.window, width=width, height=height).grid(columnspan=columnspan, rowspan=rowspan)

    def create_probability_window(self):
        """Konstruktoriaus metodas, kuris sukuria kanalo tikimybes nurodymo langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(400, 100, "Channel Distortion", 3, 2)

        # Ivesties anotacija, ivestis ir mygtukas kanalo iskraipymo tikimybei.
        entryLabel = Label(self.window, text="Distortion probability:")
        entryLabel.grid(columnspan=1, row=0, column=0)
        probEntry = Entry(self.window)
        probEntry.grid(columnspan=1, row=0, column=1)
        probEntry.insert(0, self.golayExecutor.get_distortion_probability())
        probButton = Button(self.window, width=12, text="Set Probability",
                            command=partial(self.update_probability_close_window_open_main, probEntry))
        probButton.grid(columnspan=1, row=1, column=2)
        self.window.mainloop()

    def create_main_window(self):
        """Metodas, kuris sukuria pagrindini programos langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(400, 200, "Main Menu", 1, 3)

        vectorButton = Button(self.window, text="Send a Vector", command=self.close_window_open_vector)
        vectorButton.grid(row=0, column=0)
        textButton = Button(self.window, text="Send Some Text", command=self.close_window_open_text)
        textButton.grid(row=1, column=0)
        imageButton = Button(self.window, text="Send an Image", command=self.close_window_open_image)
        imageButton.grid(row=2, column=0)
        self.window.mainloop()

    def create_vector_window(self):
        """Metodas, kuris sukuria pirmo scenarijaus langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(400, 200, "Send a Vector", 4, 3)

        menuButton = Button(self.window, text="Back To Menu", command=self.close_window_open_main)
        menuButton.grid(row=0, column=0)
        self.window.mainloop()

    def create_text_window(self):
        """Metodas, kuris sukuria antro scenarijaus langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(400, 200, "Send Some Text", 4, 3)

        menuButton = Button(self.window, text="Back To Menu", command=self.close_window_open_main)
        menuButton.grid(row=0, column=0)
        self.window.mainloop()

    def create_image_window(self):
        """Metodas, kuris sukuria trecio scenarijaus langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(400, 200, "Send an Image", 4, 3)

        menuButton = Button(self.window, text="Back To Menu", command=self.close_window_open_main)
        menuButton.grid(row=0, column=0)
        self.window.mainloop()

    def close_window(self):
        """Metodas, kuris uzdaro rodoma langa."""

        self.window.destroy()

    def update_probability(self, probEntry: Entry):
        """Metodas, kuris atnaujina kanalo iskraipymo tikimybe.

        probEntry turi buti Entry klases tipo kintamasis.
        probEntry yra ivesties laukas, i kuri buvo ivesta nauja iskraipymo tikimybes reiksme.
        """

        # Gauname ivesties lauko tekstine reiksme ir joje kablelius pakeiciame taskais.
        probability = probEntry.get().replace(",", ".")
        self.golayExecutor.set_distortion_probability(float(probability))

    def update_probability_close_window_open_main(self, probEntry: Entry):
        """Metodas, kuris atnaujina kanalo iskraipymo tikimybe, uzdaro rodoma langa ir atidaro pagrindini langa.

        probEntry turi buti Entry klases tipo kintamasis.
        probEntry yra ivesties laukas, i kuri buvo ivesta nauja iskraipymo tikimybes reiksme.
        """

        self.update_probability(probEntry)
        self.close_window()
        self.create_main_window()

    def close_window_open_main(self):
        """Metodas, kuris uzdaro rodoma langa ir atidaro pagrindini langa."""

        self.close_window()
        self.create_main_window()

    def close_window_open_vector(self):
        """Metodas, kuris uzdaro rodoma langa ir atidaro pirmo scenarijaus langa."""

        self.close_window()
        self.create_vector_window()

    def close_window_open_text(self):
        """Metodas, kuris uzdaro rodoma langa ir atidaro antro scenarijaus langa."""

        self.close_window()
        self.create_text_window()

    def close_window_open_image(self):
        """Metodas, kuris uzdaro rodoma langa ir atidaro trecio scenarijaus langa."""

        self.close_window()
        self.create_image_window()
