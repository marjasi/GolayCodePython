from typing import List
import random


def distort_binary_info(binaryNumber: int) -> int:
    """Metodas skirtas binariniu duomenu iskraipymui.

    Metodas 0 pavercia 1, o 1 pavercia 0.
    Atitinkamai grazinamas 0 arba 1.
    """

    return 0 if binaryNumber == 1 else 1


class CommChannel:
    """Kanalo klase.

    Kiekvienas siunciamas simbolis kanalu yra iskraipomas su nurodyta tikimybe.
    """

    # Kanalo iskraipymo tikimybe.
    probOfError = None

    def __init__(self, probOfError: float):
        """Konstruktoriaus metodas.

        Sukuriamas komunikacijos kanalas su iskraipymo tikimybe probOfError.
        Viena karta inicializuojamas atsitiktiniu skaiciu generatorius.
        """

        self.probOfError = probOfError
        random.seed()

    def send_binary_info(self, binaryInfo: List[int]) -> List[int]:
        """Metodas skirtas binariniu duomenu persiuntimui kanalu.

        Sugeneruojamas realus skaicius intervale [0, 1] ir pagal iskraipymo tikimybe
         nusprendziama ar informacija bus iskraipyta.
        Po siuntimo metodas grazina persiusta binarines informacijos sarasa.
        """

        for index, element in enumerate(binaryInfo):
            if random.random() < self.probOfError:
                binaryInfo[index] = distort_binary_info(element)

        return binaryInfo
