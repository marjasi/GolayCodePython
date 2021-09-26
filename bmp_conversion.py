from text_conversion import text_to_bit_array, bit_array_to_text, g_text_encoding
from base64 import b64encode, b64decode
from typing import List


def bmp_to_bit_array(bmpFileLocation: str) -> List[int]:
    """Metodas, kuris konvertuoja bmp formata faila i dvejetaini formata.

    bmp tipo failo vieta bmpFileLocation turi buti str tipo kintamasis.
    Grazinamas integer tipo sveikuju skaiciu masyvas, kuris ir atitinka dvejetaini formata.
    """

    # Failas atidaromas su read binary rezimu.
    with open(bmpFileLocation, "rb") as bmpFile:
        encodedBmp = b64encode(bmpFile.read())

    return text_to_bit_array(encodedBmp.decode(g_text_encoding))


def bit_array_to_bmp(bitList: List[int], newBmpFileLocation: str):
    """Metodas, kuris konvertuoja dvejetainiu skaiciu seka i bmp tipo faila ir ta faila issaugo vietoje nurodytoje
        newBmpFileLocation.

    Dvejetainiu skaiciu masyvas bitList turi tureti integer tipo sveikuju skaiciu elementus.
    bmp tipo failo vieta newBmpFileLocation turi buti str tipo kintamasis.
    """

    encodedBmp = bit_array_to_text(bitList)

    # Failo vieta atidaroma su write binary rezimu.
    with open(newBmpFileLocation, "wb") as newBmpFile:
        newBmpFile.write(b64decode(encodedBmp.encode(g_text_encoding)))
