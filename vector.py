from typing import List

class Vector:
    """Vektoriaus klase.

    Vektorius yra elementu kolekcija - vienmatis masyvas.
    """

    # Vektoriaus elementu masyvas.
    elements = []

    def __init__(self, vectorElements: List[int]):
        """Konstruktoriaus metodas.

        Sukuriamas vektorius su nurodytais elementais vectorElements.
        Elementai turi buti int tipo sveikieji skaiciai.
        """

        self.elements = vectorElements
