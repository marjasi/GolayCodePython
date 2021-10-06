# Treciuju saliu biblioteka naudojama teskto vertimui i dvejetaini formata ir atvirksciai.
from bitarray import bitarray
from typing import List

# Teksto uzkodavimo formatas.
g_text_encoding = "utf-16"


def text_to_bit_array(text: str) -> List[int]:
    """Metodas, kuris konvertuoja teksta i dvejetaini formata.

    Tekstas text turi buti str tipo kintamasis.
    Grazinamas integer tipo sveikuju skaiciu masyvas, kuris ir atitinka dvejetaini formata.
    """

    bitArray = bitarray()
    bitArray.frombytes(text.encode(g_text_encoding))

    return bitArray.tolist()


def bit_array_to_text(bitList: List[int]) -> str:
    """Metodas, kuris konvertuoja dvejetainiu skaiciu seka i teksta.

    Dvejetainiu skaiciu masyvas bitList turi tureti integer tipo sveikuju skaiciu elementus.
    Grazinamas tekstas yra str tipo kintamasis.
    """

    return bitarray(bitList).tobytes().decode(g_text_encoding)
