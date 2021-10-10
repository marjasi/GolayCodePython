# Biblioteka naudojama patikrinti ivesciu tinkamuma naudojant regex.
import re
import operations as op
# Biblioteka skirta grafinei vartotojo sasajai sukurti.
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
# Biblioteka naudojama perduoti metodams parametrus spaudziant mygtukus.
from functools import partial
from golay_execution import GolayExecution
# Biblioteka naudojama darbui su paveiksleliais.
from PIL import Image, ImageTk


def set_entry_text(entry: Entry, entryText: str):
    """Metodas, kuris pakeicia ivesties lauke entry esanti teksta i entryText.

    entry turi buti Entry klases tipo kintamasis.
    entryText turi buti str tipo kintamasis.
    """

    # Istriname visa entry esanti teksta.
    entry.delete(0, END)

    # Idedame nauja teksta entryText.
    entry.insert(0, entryText)


def set_scrolled_text_area_text(scrolledTextArea: ScrolledText, areaText: str):
    """Metodas, kuris pakeicia ivesties srityje scrolledTextArea esanti teksta i areaText.

    scrolledTextArea turi buti ScrolledText klases tipo kintamasis.
    areaText turi buti str tipo kintamasis.
    """

    # Istriname visa scrolledTextArea esanti teksta.
    scrolledTextArea.delete(1.0, END)

    # Idedame nauja teksta areaText.
    scrolledTextArea.insert(1.0, areaText)


def get_scrolled_text_area_text(scrolledTextArea: ScrolledText) -> str:
    """Metodas, kuris grazina ivesties srityje scrolledTextArea esanti teksta.

    scrolledTextArea turi buti ScrolledText klases tipo kintamasis.
    Metodas grazina ivesties srityje esanti teksta str tipo kintamuoju.
    """

    # Gauname visa teksta esanti ivesties srityje.
    # Atmetame viena simboli nuo galo, kad nepaimtume papildomo '\n' simbolio.
    return scrolledTextArea.get(1.0, "end-1c")


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


def check_encoded_vector_regex(vectorString: str) -> bool:
    """Metodas, kuris patikrina uzkoduoto vektoriaus ilgi ir turini pagal nurodyta regex formata.

    vectorString turi buti str tipo kintamasis.
    Metodas grazina bool tipo kintamaji.
    Grazinama True, jeigu vectorString tenkina regex formata.
    Grazinama False, jeigu vectorString netenkina regex formato.
    regex formatas apibrezia ilgio 12 vektoriu, kuri sudaro elementai 0 ar 1.
    """

    if re.fullmatch("[01]{23}", vectorString) is not None:
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

    # Siuo metu pasirinktas paveikslelis.
    selectedImage = None

    # Pasirinkto paveikslelio direktorija.
    selectedImageDirectory = None

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
        self.set_window_properties(400, 200, "Main Menu", 1, 4)

        vectorButton = Button(self.window, text="Send a Vector", command=self.close_window_open_vector)
        vectorButton.grid(columnspan=1, row=0, column=0)
        textButton = Button(self.window, text="Send Some Text", command=self.close_window_open_text)
        textButton.grid(columnspan=1, row=1, column=0)
        imageButton = Button(self.window, text="Send an Image", command=self.close_window_open_image)
        imageButton.grid(columnspan=1, row=2, column=0)
        imageButton = Button(self.window, text="Experiment", command=self.close_window_open_experiment)
        imageButton.grid(columnspan=1, row=3, column=0)
        self.window.mainloop()

    def create_vector_window(self):
        """Metodas, kuris sukuria pirmo scenarijaus langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(1200, 500, "Send a Vector", 12, 14)

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

        # Dekoduoto vektoriaus parodymo ivestis.
        decodedVectorEntry = Entry(self.window, state="readonly", width=25)
        decodedVectorEntry.grid(columnspan=2, row=11, column=2)

        # Algoritmo veikimo israsas.
        algorithmLogLabel = Label(self.window, text="Algorithm Log:")
        algorithmLogLabel.grid(columnspan=2, row=1, column=6)
        algorithmLogText = ScrolledText(self.window, width=65)
        algorithmLogText.grid(columnspan=5, rowspan=9, row=2, column=6)

        # Gauto is kanalo vektoriaus keitimas.
        distVectorLabel = Label(self.window, text="Received Vector:")
        distVectorLabel.grid(columnspan=2, row=9, column=0)
        distVectorButton = Button(self.window, width=12, text="Decode")
        distVectorButton.configure(comman=partial(self.decode_vector, distVectorEntry, decodedVectorEntry,
                                                  distVectorButton, algorithmLogText))
        distVectorButton.grid(columnspan=1, row=9, column=4)

        # Klaidu perskaiciavimas.
        renewErrorButton = Button(self. window, width=16, text="Recalculate Mistakes")
        renewErrorButton.configure(command=partial(self.renew_error_number, encodedVectorEntry,
                                                   distVectorEntry, distVectorErrorEntry, renewErrorButton))
        renewErrorButton.grid(columnspan=1, row=10, column=4)

        # Dekoduotas vektorius.
        decodedVectorLabel = Label(self.window, text="Decoded Vector:")
        decodedVectorLabel.grid(columnspan=2, row=11, column=0)

        # Inicializuojamas lango veikimo ciklas.
        self.window.mainloop()

    def create_text_window(self):
        """Metodas, kuris sukuria antro scenarijaus langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(1600, 1000, "Send Some Text", 12, 9)

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

        # Teksto siuntimui ivestis.
        textInputLabel = Label(self.window, text="Text To Send:")
        textInputLabel.grid(columnspan=2, row=3, column=0)
        textInputTextArea = ScrolledText(self.window)
        textInputTextArea.grid(columnspan=5, rowspan=2, row=4, column=1)

        # Gautas nekoduotas tekstas.
        rawTextOutputLabel = Label(self.window, text="Received Raw Text:")
        rawTextOutputLabel.grid(columnspan=2, row=0, column=7)
        rawTextOutputTextArea = ScrolledText(self.window, state="disabled")
        rawTextOutputTextArea.grid(columnspan=5, rowspan=3, row=1, column=7, padx=50)

        # Gautas koduotas tekstas.
        encodedTextOutputLabel = Label(self.window, text="Received Encoded Text:")
        encodedTextOutputLabel.grid(columnspan=2, row=4, column=7)
        encodedTextOutputTextArea = ScrolledText(self.window, state="disabled")
        encodedTextOutputTextArea.grid(columnspan=5, rowspan=3, row=5, column=7, padx=50)

        # Tesksto siuntimo mygtukas.
        textInputSendButton = Button(self.window, width=12, text="Send Text")
        textInputSendButton.configure(command=partial(self.send_text, textInputSendButton, textInputTextArea,
                                                      rawTextOutputTextArea, encodedTextOutputTextArea))
        textInputSendButton.grid(columnspan=1, row=7, column=4)

        # Inicializuojamas lango veikimo ciklas.
        self.window.mainloop()

    def create_image_window(self):
        """Metodas, kuris sukuria trecio scenarijaus langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(1600, 800, "Send an Image", 20, 11)

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

        # Gauti is kanalo paveiksleliai.
        rawImgAnnotationLabel = Label(self.window, text="Received Raw Image:")
        rawImgAnnotationLabel.grid(columnspan=2, row=0, column=10)
        showReceivedRawImgLabel = Label(self.window)
        showReceivedRawImgLabel.grid(columnspan=4, rowspan=7, row=1, column=10)
        encodedImgAnnotationLabel = Label(self.window, text="Received Encoded Image:")
        encodedImgAnnotationLabel.grid(columnspan=2, row=0, column=15)
        showReceivedEncodedImgLabel = Label(self.window)
        showReceivedEncodedImgLabel.grid(columnspan=4, rowspan=7, row=1, column=15)

        # Paveikslelio pasirinkimas ir siuntimas.
        showSelectedImgLabel = Label(self.window)
        showSelectedImgLabel.grid(columnspan=4, rowspan=7, row=1, column=5)
        selectImgButton = Button(self.window, text="Select Image...")
        selectImgButton.configure(command=partial(self.show_bmp_image_after_selection, showSelectedImgLabel))
        selectImgButton.grid(columnspan=1, row=3, column=4)
        shownImgAnnotationLabel = Label(self.window, text="Selected Image:")
        shownImgAnnotationLabel.grid(columnspan=2, row=0, column=5)
        sendImgButton = Button(self.window, text="Send Image")
        sendImgButton.configure(command=partial(self.send_selected_bmp_image, sendImgButton, showReceivedRawImgLabel,
                                                showReceivedEncodedImgLabel))
        sendImgButton.grid(columnspan=1, row=4, column=4)

        # Is naujo iejus i scenarijaus langa parodomas pries tai pasirinktas paveikslelis.
        if self.selectedImage is not None:
            self.show_bmp_image(showSelectedImgLabel, self.selectedImage, True)

        # Inicializuojamas lango veikimo ciklas.
        self.window.mainloop()

    def create_experiment_window(self):
        """Metodas, kuris sukuria eksperimentu langa."""

        # Lango sukurimas ir ypatybes.
        self.window = Tk()
        self.set_window_properties(1200, 500, "Experiment", 5, 6)

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

        # Bandymu skaiciaus ivestis
        repeatLabel = Label(self.window, text="Number Of Repeats:")
        repeatLabel.grid(columnspan=2, row=3, column=0)
        repeatEntry = Entry(self.window)
        repeatEntry.grid(columnspan=2, row=3, column=2)
        conductButton = Button(self.window, width=16, text="Conduct Experiment")
        conductButton.grid(columnspan=1, row=4, column=4)

        # Inicializuojamas lango veikimo ciklas.
        self.window.mainloop()

    def show_bmp_image(self, imgLabel: Label, image: Image, setAsSelected=False):
        """Metodas, kuris nurodytoje erdveje imgLabel parodo paveiksleli image.

        imgLabel turi buti Label klases tipo kintamasis.
        imgLabel yra paveikslelio rodymo sritis.
        image turi buti Image klases tipo kintamasis.
        image yra paveikslelis.
        setAsSelected turi buti bool tipo kintamasis.
        Jeigu setAsSelected yra True, tai parodomas paveikslelis bus issaugotas kaip klases laukas self.selectedImage.
        Jeigu setAsSelected yra False, tai parodomas paveikslelis nebus issaugotas
         kaip klases laukas self.selectedImage.
        Pagal nutylejima, setAsSelected yra False.
        """

        if setAsSelected:
            # Nuoroda i paveiksleli ir paveikslelio direktorija issaugoma klases kintamuosiuose..
            self.selectedImage = image

        # Paveikslelis parodomas nurodytoje erdveje.
        tkImage = ImageTk.PhotoImage(image)
        imgLabel.configure(image=tkImage)
        imgLabel.image = tkImage

    def show_bmp_image_after_selection(self, imgLabel: Label):
        """Metodas, kuris parodo pasirinktoje vietoje esanti paveiksleli erdveje imgLabel.

        imgLabel turi buti Label klases tipo kintamasis.
        """

        # Nurodome failo vietos pasirinkimo veiksma ir palaikomus failu tipus.
        imgPath = filedialog.askopenfilename(filetypes=[("Image File", ".bmp")])

        # Jeigu buvo pasirinktas failas.
        if imgPath:
            # Issaugome pasirinkto paveikslelio direktorija.
            self.selectedImageDirectory = imgPath
            # Paveikslelis atidaromas.
            image = Image.open(imgPath)
            self.show_bmp_image(imgLabel, image, True)

    def send_selected_bmp_image(self, sendButton: Button, rawImgLabel: Label, encImgLabel: Label):
        """Metodas, kuris nusiuncia pasirinkta paveiksleli kanalu dviem budais: uzkodavus ir neuzkodavus.
        Gauti paveiksleliai parodomi atitinkamose rodymo srityse rawImgLabel ir encImgLabel.
        Gauti paveiksleliai taip pat yra issaugomi toje pacioje direktorijoje kaip ir pasirinktas paveikslelis.
        Failu pavadinimai sudaromi pridejus prefiksus raw ir enc prie originalaus paveikslelio pavadinimo.

        sendButton turi buti Button klases tipo kintamasis.
        sendButton yra paveikslelio siuntimo mygtukas.
        rawImgLabel turi buti Label klases tipo kintamasis.
        rawImgLabel yra neuzkoduoto gauto is kanalo paveikslelio rodymo sritis.
        encImgLabel turi buti Label klases tipo kintamasis.
        encImgLabel yra uzkoduoto gauto is kanalo paveikslelio rodymo sritis.
        """

        # Is kanalo gautas nekoduotas paveikslelis.
        receivedRawImg = None

        # Is kanalo gautas uzkoduotas paveikslelis.
        receivedEncodedImg = None

        # Fiksuojame, ar ivyko klaida.
        noError = True

        # Jeigu buvo pasirinktas paveikslelis, tik tada siunciame paveiksleli kanalu.
        if self.selectedImageDirectory:
            # Nuimame raudona spalva nuo mygtuko.
            sendButton.configure(bg="SystemButtonFace")

            # Bandome paveikslelius siusti kanalu, ivykus klaidoms parodome paveikslelius, kurie informuoja
            #  apie nepalaikoma bmp failo antrasciu formata.
            try:
                receivedRawImg, receivedEncodedImg = self.golayExecutor.send_image_bit_data(self.selectedImageDirectory)
            except OSError:
                receivedRawImg = receivedEncodedImg = Image.open(r"bmpImages\errorImg.bmp")
                noError = False
            finally:
                # Gauti is kanalo paveiksleliai parodomi atitinkamose rodymo srityse ir issaugomi, jeigu neivyko klaida.
                self.show_bmp_image(rawImgLabel, receivedRawImg, noError)
                self.show_bmp_image(encImgLabel, receivedEncodedImg, noError)
        # Jeigu paveikslelis nebuvo pasirinktas, nudazome mygtuka raudonai.
        else:
            sendButton.configure(bg=self.buttonErrorColor)

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

    def decode_vector(self, encodedVectorEntry: Entry, distortedVectorEntry: Entry, decodedVectorButton: Button,
                      scrolledTextArea: ScrolledText):
        """Metodas, kuris dekoduoja vektoriu esanti ivestyje encodedVectorEntry ir parodo dekoduota vektoriu
            ivestyje decodedVectorEntry.

        distortedVectorEntry turi buti Entry klases tipo kintamasis.
        distortedVectorEntry yra iskraipyto vektoriaus parodymo ivestis.
        decodedVectorEntry turi buti Entry klases tipo kintamasis.
        decodedVectorEntry yra dekoduoto vektoriaus parodymo ivestis.
        decodedVectorButton turi buti Button klases tipo kintamasis.
        decodedVectorButton yra vektoriaus dekodavimo mygtukas.
        scrolledTextArea turi buti ScrolledText klases tipo kintamasis.
        scrolledTextArea yra teksto laukas, kuriame bus rodomas algoritmo vykdymo tekstas.
        """

        # Patikriname, ar uzkoduotas vektoriaus atitinka reikiama formata
        if check_encoded_vector_regex(encodedVectorEntry.get()):
            encodedVector = op.create_vector_from_string(encodedVectorEntry.get())

            # Dekoduojame uzkoduota vektoriu.
            decodedVector, algorithmLog = self.golayExecutor.decode_vector(encodedVector)

            # Parodome vartotojui dekoduota vektoriu.
            distortedVectorEntry.configure(state="normal")
            set_entry_text(distortedVectorEntry, decodedVector.get_elements_as_string())
            distortedVectorEntry.configure(state="disabled")

            # Parodome algoritmo vykdymo teksta.
            set_scrolled_text_area_text(scrolledTextArea, algorithmLog)

            # Nudazome dekodavimo mygtuka zaliai.
            decodedVectorButton.configure(bg=self.buttonOkColor)
        # Uzkoduotas vektoriaus formato neatitinka.
        else:
            # Nudazome dekodavimo mygtuka raudonai.
            decodedVectorButton.configure(bg=self.buttonErrorColor)

    def renew_error_number(self, encodedVectorEntry: Entry, distortedVectorEntry: Entry, mistakeEntry: Entry,
                           mistakeButton: Button):
        """Metodas, kuris perskaicijuoja klaidu skaiciu is kanalo gautame iskreiptame vektoriuje.

        encodedVectorEntry turi buti Entry klases tipo kintamasis.
        encodedVectorEntry yra uzkoduoto vektoriaus parodymo ivestis.
        distortedVectorEntry turi buti Entry klases tipo kintamasis.
        distortedVectorEntry yra iskraipyto vektoriaus parodymo ivestis.
        mistakeEntry turi buti Entry klases tipo kintamasis.
        mistakeEntry yra kanale padarytu klaidu skaiciaus parodymo ivestis.
        mistakeButton turi buti Button klases tipo kintamasis.
        mistakeButton yra klaidu perskaiciavimo mygtukas.
        """

        encodedVector = op.create_vector_from_string(encodedVectorEntry.get())
        receivedVector = op.create_vector_from_string(distortedVectorEntry.get())

        # Patikriname, ar abu vektoriai turi elementus (yra netusti) ir ar vektoriai atitinka reikiama formata.
        if encodedVector.elements and receivedVector.elements\
                and check_encoded_vector_regex(encodedVectorEntry.get())\
                and check_encoded_vector_regex(distortedVectorEntry.get()):
            # Suskaiciuojamos padarytos klaidos ir atnaujinamas klaidu skaicius.
            resultTuple = self.golayExecutor.get_error_num_positions(encodedVector, receivedVector)
            mistakeEntry.configure(state="normal")
            set_entry_text(mistakeEntry, str(resultTuple[0]))
            mistakeEntry.configure(state="disabled")

            # Nudazome klaidos perskaiciavimo mygtuka zaliai.
            mistakeButton.configure(bg=self.buttonOkColor)
        else:
            # Nudazome klaidos perskaiciavimo mygtuka raudonai.
            mistakeButton.configure(bg=self.buttonErrorColor)

    def send_text(self, textSendButton: Button, textInputTextArea: ScrolledText,
                  rawTextOutputTextArea: ScrolledText, encodedTextOutputTextArea: ScrolledText):
        """Metodas, kuris persiuncia ir parodo nekoduota ir uzkoduota teksta.

        textSendButton turi buti Button tipo klases kintamasis.
        textSendButton yra teksto siuntimo mygtukas.
        textInputTextArea turi buti ScrolledText tipo kintamasis.
        textInputTextArea yra teksto ivesties parodymo sritis.
        rawTextOutputTextArea turi buti ScrolledText tipo kintamasis.
        rawTextOutputTextArea yra nekoduoto kanalu persiusto teksto parodymo sritis.
        encodedTextOutputTextArea turi buti ScrolledText tipo kintamasis.
        encodedTextOutputTextArea yra uzkoduoto kanalu persiusto teksto parodymo sritis.
        """

        textInput = get_scrolled_text_area_text(textInputTextArea)

        # Patikriname, ar teksto ivesties parodymo sritis yra tuscia.
        if textInput:
            receivedRawText, receivedEncodedText = self.golayExecutor.send_text(textInput)

            # Is kanalo gauta teksta parodomose atitinkamose teksto srityse.
            rawTextOutputTextArea.configure(state="normal")
            set_scrolled_text_area_text(rawTextOutputTextArea, receivedRawText)
            rawTextOutputTextArea.configure(state="disabled")

            encodedTextOutputTextArea.configure(state="normal")
            set_scrolled_text_area_text(encodedTextOutputTextArea, receivedEncodedText)
            encodedTextOutputTextArea.configure(state="disabled")

            # Siuntimo mygtukas nudazomas zaliai.
            textSendButton.configure(bg=self.buttonOkColor)
        # Jeigu teksto ivesties parodymo sritis yra tuscia, nudazome siuntimo mygtuka raudonai.
        else:
            textSendButton.configure(bg=self.buttonErrorColor)

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

    def close_window_open_experiment(self):
        """Metodas, kuris uzdaro rodoma langa ir atidaro eksperimentu langa."""

        self.close_window()
        self.create_experiment_window()
