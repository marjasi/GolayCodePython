from typing import List


class Vector:
    """Vektoriaus klase.

    Vektorius yra elementu kolekcija - vienmatis masyvas.
    """

    # Vektoriaus elementu masyvas.
    elements = []

    def __init__(self, vectorElements: List[int]):
        """Konstruktoriaus metodas.

        Sukuriamas vektorius su nurodytais masyvo vectorElements elementais.
        Masyvo vectorElements elementai yra nukopijuojami i nauja masyva sukurta vektoriaus objektui.
        Elementai turi buti integer tipo sveikieji skaiciai.
        """

        self.elements = vectorElements.copy()


print("It works, my dude.")
input("Press Enter to continue...")
