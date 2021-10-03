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
        Parametras probOfError turi buti float tipo realusis skaicius.
        Viena karta inicializuojamas atsitiktiniu skaiciu generatorius.
        """

        self.set_prob_of_error(probOfError)
        random.seed()

    def set_prob_of_error(self, probOfError: float):
        """Metodas skirtas naujos iskraipymo tikimybes nustatymui.

        Parametras probOfError turi buti float tipo realusis skaicius.
        Iskraipymo tikimybe visada bus reiksme priklausanti intervale [0.0, 1.0].
        Tai yra, paduotos reiksmes nesancios is sio intervalo bus interpretuojamos kaip 1.0 ar 0.0.
        """

        # Jeigu iskraipymo tikimybe didesne uz 1.0, tai ji ir bus lygi 1.0.
        if probOfError > 1.0:
            probOfError = 1.0
        # Jeigu iskraipymo tikimybe mazesne uz 0.0, tai ji ir bus lygi 0.0.
        elif probOfError < 0.0:
            probOfError = 0.0

        self.probOfError = probOfError

    def get_prob_of_error(self) -> float:
        """Metodas, kuris grazina dabartine komunikacijos kanalo iskraipymo tikimybe.

        Grazinama iskraipymo tikimybe yra float tipo realus skaicius.
        """

        return self.probOfError

    def send_binary_info(self, vectorElements: List[int]) -> List[int]:
        """Metodas skirtas binariniu duomenu persiuntimui kanalu.

        Sugeneruojamas realus skaicius intervale [0, 1] ir pagal iskraipymo tikimybe
         nusprendziama ar informacija bus iskraipyta.
        Po siuntimo metodas grazina persiusta binarines informacijos sarasa.
        vectorElements turi buti masyvas, kurio elementai yra integer tipo sveikieji skaiciai.
        Metodas grazina masyva binaryInfo, kuriame yra iskraipyti vektoriaus elementai.
        """

        binaryInfo = vectorElements.copy()

        for index, element in enumerate(binaryInfo):
            if random.random() < self.probOfError:
                binaryInfo[index] = distort_binary_info(element)

        return binaryInfo
