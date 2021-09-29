from typing import List


class Matrix:
    """Matricos klase.

    Matrica yra vienodo ilgio vektoriu rinkinys.
    Kiekvienas vektorius atitinka matricos eilute.
    """

    # Matricos eilutes.
    rows = None

    def __init__(self, matrixRows: List[List[int]]):
        """Konstruktoriaus metodas.

        Sukuriamas matrica su nurodytomis eilutemis masyve matrixRows.
        Masyvo matrixRows elementai yra nukopijuojami i nauja masyva sukurta matricos objektui.
        matrixRows elementai turi buti masyvai, kuriu elementai yra integer tipo sveikieji skaiciai.
        """

        self.rows = matrixRows.copy()

    def __str__(self):
        """Metodas skirtas matricos atspausdinimui kvieciant funkcija print().

        Metodas grazina tekstine matricos reprezentacija.
        """

        text = ""
        for row in self.rows:
            text += "| "
            for element in row:
                text += str(element) + " "
            text += "|"

        return text
