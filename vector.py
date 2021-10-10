# Biblioteka naudojama objektu kopijoms kurti.
import copy
# Bibloteka naudojama tipu apibrezimams, kurie nurodomi metodu parametrams ir grazinamoms reiksmems.
from typing import List


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

    def get_elements_as_string(self) -> str:
        """Metodas, kuris grazina vektoriaus elementus sudetus i tesktine eilute.

        Metodas grazina str tipo teksto eilute, kurioje yra sudeti vektoriaus elementai.
        """

        vectorElements = ""

        for element in self.elements:
            vectorElements += str(element)

        return vectorElements

    def __str__(self):
        """Metodas skirtas vektoriaus atspausdinimui kvieciant funkcija print().

        Metodas grazina tekstine vektoriaus reprezentacija.
        """

        text = "( "
        for element in self.elements:
            text += str(element) + " "

        text += ")"

        return text
