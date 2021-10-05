# Biblioteka skirta grafinei vartotojo sasajai sukurti.
from tkinter import *
from tkinter.scrolledtext import ScrolledText
# Biblioteka naudojama perduoti metodams parametrus spaudziant mygtukus.
from functools import partial
from golay_execution import GolayExecution
import operations as op
# Biblioteka naudojama patikrinti ivesciu tinkamuma naudojant regex.
import re


def set_entry_text(entry: Entry, entryText: str):
    """Metodas, kuris pakeicia ivesties lauke entry esanti teksta i entryText.

    entry turi buti Entry klases tipo kintamasis.
    entryText turi buti str tipo kintamasis.
    """

    # Istriname visa entry esanti teksta.
    entry.delete(0, END)

    # Idedame nauja teksta entryText.
    entry.insert(0, entryText)


def check_vector_regex(vectorString: str) -> bool:
    """Metodas, kuris patikrina vektoriaus ilgi ir turini pagal nurodyta regex formata.

    vectorString turi buti str tipo kintamasis.
    Metodas grazina bool tipo kintamaji.
    Grazinama True, jeigu vectorString tenkina regex formata.
    Grazinama False, jeigu vectorString netenkina regex formato.
    regex formatas apibrezia ilgio 12 vektoriu, kuri sudaro elementai 0 ar 1.
    """

    if re.fullmatch("[01]{12}", vectorString) is not None:
        return True
    else:
        return False


class GolayWindow:
    """Programos grafines vartotojo sasajos klase.

    Klase apibrezia programos pagrindini langa ir jo elementus bei metodus, kurie dirba su lango elementais.
    """

    # Programos langas. Nebutinai pagrindinis.
    window = None
    # Golejaus kodo vykdymo klase.
    golayExecutor = None

    # Mygtuko spalva, kai nebuvo klaidu.
    buttonOkColor = "#9CFD8C"

    # Mygtuko spalva, kai ivyko klaidos.
    buttonErrorColor = "#FF8E8E"

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
        entryLabel = Label(self.window, text="Distortion Probability:")
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
        vectorButton.grid(columnspan=1, row=0, column=0)
        textButton = Button(self.window, text="Send Some Text", command=self.close_window_open_text)
        textButton.grid(columnspan=1, row=1, column=0)
        imageButton = Button(self.window, text="Send an Image", command=self.close_window_open_image)
        imageButton.grid(columnspan=1, row=2, column=0)
        self.window.mainloop()

    def create_vector_window(self):
        """Metodas, kuris sukuria pirmo scenarijaus langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(1200, 500, "Send a Vector", 11, 14)

        # Mygtukas grizti atgal i meniu.
        menuButton = Button(self.window, text="Back To Menu", command=self.close_window_open_main)
        menuButton.grid(columnspan=1, row=0, column=0)

        # Iskraipymo tikimybes ivestis.
        probLabel = Label(self.window, text="Distortion Probability:")
        probLabel.grid(columnspan=2, row=2, column=0)
        probEntry = Entry(self.window)
        probEntry.grid(columnspan=2, row=2, column=2)
        probEntry.insert(0, self.golayExecutor.get_distortion_probability())
        probButton = Button(self.window, width=12, text="Set Probability")
        probButton.configure(command=partial(self.button_color_update_probability, probButton, probEntry))
        probButton.grid(columnspan=1, row=4, column=4)

        # Uzkoduotas vektorius.
        encodedVectorLabel = Label(self.window, text="Encoded Vector:")
        encodedVectorLabel.grid(columnspan=2, row=8, column=0)
        encodedVectorEntry = Entry(self.window, state="readonly", width=25)
        encodedVectorEntry.grid(columnspan=2, row=8, column=2)

        # Kanale ivykusios klaidos.
        distVectorErrorLabel = Label(self.window, text="Mistakes: ")
        distVectorErrorLabel.grid(columnspan=2, row=10, column=0)
        distVectorErrorEntry = Entry(self.window, state="disabled", width=4, justify="center")
        distVectorErrorEntry.grid(columnspan=2, row=10, column=2)

        # Gauto is kanalo vektoriaus ivestis.
        distVectorEntry = Entry(self.window, width=25)
        distVectorEntry.grid(columnspan=2, row=9, column=2)

        # Vektoriaus ivestis.
        vectorInputLabel = Label(self.window, text="Vector To Send:")
        vectorInputLabel.grid(columnspan=2, row=6, column=0)
        vectorInputEntry = Entry(self.window)
        vectorInputEntry.grid(columnspan=2, row=6, column=2)
        vectorInputButton = Button(self.window, width=13, text="Encode and Send")
        vectorInputButton.configure(command=partial(self.encode_send_vector, vectorInputButton, vectorInputEntry,
                                                    encodedVectorEntry, distVectorEntry, distVectorErrorEntry))
        vectorInputButton.grid(columnspan=1, row=7, column=4)

        # Gauto is kanalo vektoriaus keitimas.
        distVectorLabel = Label(self.window, text="Received Vector:")
        distVectorLabel.grid(columnspan=2, row=9, column=0)
        distVectorButton = Button(self.window, width=12, text="Decode")
        distVectorButton.grid(columnspan=1, row=10, column=4)

        # Dekoduotas vektorius.
        decodedVectorLabel = Label(self.window, text="Decoded Vector:")
        decodedVectorLabel.grid(columnspan=2, row=11, column=0)
        decodedVectorEntry = Entry(self.window, state="readonly", width=25)
        decodedVectorEntry.grid(columnspan=2, row=11, column=2)

        # Algoritmo veikimo israsas.
        algorithmLogLabel = Label(self.window, text="Algorithm Log:")
        algorithmLogLabel.grid(columnspan=2, row=1, column=6)
        algorithmLogText = ScrolledText(self.window, width=60)
        algorithmLogText.grid(columnspan=4, rowspan=9, row=2, column=6)

        # Inicializuojamas lango veikimo ciklas.
        self.window.mainloop()

    def create_text_window(self):
        """Metodas, kuris sukuria antro scenarijaus langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(400, 200, "Send Some Text", 9, 7)

        # Mygtukas grizti atgal i meniu.
        menuButton = Button(self.window, text="Back To Menu", command=self.close_window_open_main)
        menuButton.grid(columnspan=1, row=0, column=0)

        # Iskraipymo tikimybes ivestis.
        probLabel = Label(self.window, text="Distortion Probability:")
        probLabel.grid(columnspan=2, row=1, column=0)
        probEntry = Entry(self.window)
        probEntry.grid(columnspan=2, row=1, column=2)
        probEntry.insert(0, self.golayExecutor.get_distortion_probability())
        probButton = Button(self.window, width=12, text="Set Probability")
        probButton.configure(command=partial(self.button_color_update_probability, probButton, probEntry))
        probButton.grid(columnspan=1, row=2, column=4)

        # Inicializuojamas lango veikimo ciklas.
        self.window.mainloop()

    def create_image_window(self):
        """Metodas, kuris sukuria trecio scenarijaus langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(400, 200, "Send an Image", 13, 9)

        # Mygtukas grizti atgal i meniu.
        menuButton = Button(self.window, text="Back To Menu", command=self.close_window_open_main)
        menuButton.grid(columnspan=1, row=0, column=0)

        # Iskraipymo tikimybes ivestis.
        probLabel = Label(self.window, text="Distortion Probability:")
        probLabel.grid(columnspan=2, row=1, column=0)
        probEntry = Entry(self.window)
        probEntry.grid(columnspan=2, row=1, column=2)
        probEntry.insert(0, self.golayExecutor.get_distortion_probability())
        probButton = Button(self.window, width=12, text="Set Probability")
        probButton.configure(command=partial(self.button_color_update_probability, probButton, probEntry))
        probButton.grid(columnspan=1, row=2, column=4)

        # Inicializuojamas lango veikimo ciklas.
        self.window.mainloop()

    def close_window(self):
        """Metodas, kuris uzdaro rodoma langa."""

        self.window.destroy()

    def update_probability(self, probEntry: Entry) -> bool:
        """Metodas, kuris atnaujina kanalo iskraipymo tikimybe.

        probEntry turi buti Entry klases tipo kintamasis.
        probEntry yra ivesties laukas, i kuri buvo ivesta nauja iskraipymo tikimybes reiksme.
        Metodas grazina bool tipo reiksme, kuri nurodo, ar buvo sekmingai pakeista iskraipymo tikimybe
        """

        # Gauname ivesties lauko tekstine reiksme ir joje kablelius pakeiciame taskais.
        probability = probEntry.get().replace(",", ".")

        # Jeigu ivyko klaida ir reiksme negalejo buti konvertuota i realu skaiciu, graziname False.
        # Kitu atveju graziname True.
        try:
            self.golayExecutor.set_distortion_probability(float(probability))
        except ValueError:
            return False
        return True

    def encode_send_vector(self, button: Button, vectorEntry: Entry, encodedVectorEntry: Entry,
                           distortedVectorEntry: Entry, mistakeEntry: Entry):
        """Metodas, kuris uzkoduoja ivesta vektoriu ir siuncia ji per komunikacijos kanalo.

        Pries vektoriu uzkoduojant, patikrinama, ar vartotojas ivede tinkamo ilgio ir turinio vektoriu.
        button turi buti Button klases tipo kintamasis.
        button yra mygtukas, kuris inicijuoja si metoda.
        vectorEntry turi buti Entry klases tipo kintamasis.
        vectorEntry yra vektoriaus, kuri norime uzkoduoti ir siusti kanalu, elementu ivestis.
        encodedVectorEntry turi buti Entry klases tipo kintamasis.
        encodedVectorEntry yra uzkoduoto vektoriaus parodymo ivestis.
        distortedVectorEntry turi buti Entry klases tipo kintamasis.
        distortedVectorEntry yra iskraipyto vektoriaus parodymo ivestis.
        mistakeEntry yra Entry klases tipo kintamasis.
        mistakeEntry yra kanale padarytu klaidu skaiciaus parodymo ivestis.
        """

        # Jeigu buvo ivestas netinkamas vektorius, mygtukas nudazomas raudonai.
        if not check_vector_regex(vectorEntry.get()):
            button.configure(bg=self.buttonErrorColor)
        # Kitu atveju, mygtukas nudazomas zaliai ir toliau vykdomas metodas.
        else:
            button.configure(bg=self.buttonOkColor)

            # Uzkoduojamas vektorius.
            inputVector = op.create_vector_from_string(vectorEntry.get())
            encodedVector = self.golayExecutor.encode_vector(inputVector)

            # Parodoma uzkoduoto vektoriaus reiksme.
            encodedVectorEntry.configure(state="normal")
            set_entry_text(encodedVectorEntry, encodedVector.get_elements_as_string())
            encodedVectorEntry.configure(state="readonly")

            # Uzkoduotas vektorius siunciamas kanalu.
            receivedVector = self.golayExecutor.send_vector(encodedVector)
            set_entry_text(distortedVectorEntry, receivedVector.get_elements_as_string())

            # Suskaiciuojamos padarytos klaidos ir parodomas klaidu skaicius.
            resultTuple = self.golayExecutor.get_error_num_positions(encodedVector, receivedVector)
            mistakeEntry.configure(state="normal")
            set_entry_text(mistakeEntry, str(resultTuple[0]))
            mistakeEntry.configure(state="disabled")

    def button_color_update_probability(self, button: Button, probEntry: Entry):
        """Metodas, kuris atnaujina kanalo iskraipymo tikimybe ir pakeicia mygtuko spalva.

        button turi buti Button klases tipo kintamasis.
        button yra mygtukas, kuris bus nudazytas zaliai arba raudonai.
        probEntry turi buti Entry klases tipo kintamasis.
        probEntry yra ivesties laukas, i kuri buvo ivesta nauja iskraipymo tikimybes reiksme.
        """

        if self.update_probability(probEntry):
            # Iskraipymo tikimybe pakeista.
            set_entry_text(probEntry, str(self.golayExecutor.get_distortion_probability()))
            button.configure(bg=self.buttonOkColor)
        else:
            # Nepavyko pakeisti iskraipymo tikimybes.
            button.configure(bg=self.buttonErrorColor)

    def update_probability_close_window_open_main(self, probEntry: Entry):
        """Metodas, kuris atnaujina kanalo iskraipymo tikimybe, uzdaro rodoma langa ir atidaro pagrindini langa.

        probEntry turi buti Entry klases tipo kintamasis.
        probEntry yra ivesties laukas, i kuri buvo ivesta nauja iskraipymo tikimybes reiksme.
        """

        if self.update_probability(probEntry):
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
