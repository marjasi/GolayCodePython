from typing import List
import copy


class Vector:
    """Vektoriaus klase.

    Vektorius yra elementu kolekcija - vienmatis masyvas.
    """

    # Vektoriaus elementu masyvas.
    elements = None

    # Kiek vektoriaus reiksmiu yra esmines.
    essentialElemLen = None

    def __init__(self, vectorElements: List[int], essentialElemLen: int):
        """Konstruktoriaus metodas.

        Sukuriamas vektorius su nurodytais masyvo vectorElements elementais.
        Isimenama, kiek elementu vektoriuje yra esminiai, tai yra, isimenama essentialElemLen reiksme.
        Masyvo vectorElements elementai yra nukopijuojami i nauja masyva sukurta vektoriaus objektui.
        Elementai turi buti integer tipo sveikieji skaiciai.
        Esminiu elementu skaicius turi buti integer tipo sveikas skaicius.
        """

        self.elements = copy.deepcopy(vectorElements)
        self.essentialElemLen = essentialElemLen

    def __str__(self):
        """Metodas skirtas vektoriaus atspausdinimui kvieciant funkcija print().

        Metodas grazina tekstine vektoriaus reprezentacija.
        """

        text = "( "
        for element in self.elements:
            text += str(element) + " "

        text += ")"

        return text
