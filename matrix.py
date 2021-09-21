from typing import List
from vector import Vector


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

        rows = [[None] * len(matrixRows[0]) for i in range(len(matrixRows))]

        for index, row in enumerate(matrixRows):
            rows[index] = row

        self.rows = rows

    def __str__(self):
        """Metodas skirtas matricos atspausdinimui kvieciant funkcija print()."""

        text = ""
        for row in self.rows:
            text += "| "
            for element in row:
                text += str(element) + " "
            text += "|\n"

        return text
