from typing import List


class Vector:
    """Vektoriaus klase.

    Vektorius yra elementu kolekcija - vienmatis masyvas.
    """

    # Vektoriaus elementu masyvas.
    elements = None

    def __init__(self, vectorElements: List[int]):
        """Konstruktoriaus metodas.

        Sukuriamas vektorius su nurodytais masyvo vectorElements elementais.
        Masyvo vectorElements elementai yra nukopijuojami i nauja masyva sukurta vektoriaus objektui.
        Elementai turi buti integer tipo sveikieji skaiciai.
        """

        self.elements = vectorElements.copy()

    def __str__(self):
        """
        Metodas skirtas vektoriaus atspausdinimui kvieciant funkcija print().

        Metodas grazina tekstine vektoriaus reprezentacija.
        """

        text = "( "
        for element in self.elements:
            text += str(element) + " "

        text += ")\n"

        return text
