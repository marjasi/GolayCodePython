import io
import text_conversion as txt_conv
from base64 import b64encode, b64decode
from typing import List
from PIL import Image, ImageFile

""" Failas atidaromas su read binary rezimu.
with open(r"D:\\img.bmp", "rb") as bmpFile:
    bmp = bmpFile.read()
print(bmp)
bmpBits = [access_bit(bmp, i) for i in range(len(bmp) * 8)]
print("BITS:")
print(bmpBits)
bytesS = [sum([byte[b] << b for b in range(0, 8)])
          for byte in zip(*(iter(bmpBits),) * 8)
          ]
bytesS = bytearray(bytesS)
bmpFile = Image.open(io.BytesIO(bytesS))
bmpFile.save(r"D:\\four.bmp")
print(bmpFile)"""


def get_bit(byteData: bytes, index: int):
    """Metodas, kuris grazina baite esancio duomens pozicijoje index dvejetainio formato reiksme.

    byteData turi buti bytes tipo kintamasis.
    index turi buti int tipo sveikasis skaicius.
    """

    base = int(index // 8)
    shift = int(index % 8)
    return (byteData[base] >> shift) & 0x1


def bmp_to_bit_array(bmpFileLocation: str) -> List[int]:
    """Metodas, kuris atidaro paveiksleli esanti direktorijoje bmpFileLocation ir ji nuskaito kaip dvejetainio
        formato masyva.

    bmpFileLocation turi buti str tipo kintamasis.
    Grazinamas integer tipo sveikuju skaiciu masyvas, kuris ir atitinka paveikslelio dvejetaini formata.
    """

    # Failas atidaromas su read binary rezimu.
    with open(bmpFileLocation, "rb") as bmpFile:
        bmpByteArray = bmpFile.read()

    # Konvertuojame baitu masyva i bitu masyva.
    bmpBitArray = [get_bit(bmpByteArray, index) for index in range(len(bmpByteArray) * 8)]
    return bmpBitArray


def bit_array_to_bmp(bitList: List[int], newBmpFileLocation: str) -> Image:
    """Metodas, kuris konvertuoja dvejetainiu skaiciu seka i bmp tipo faila ir ta faila issaugo vietoje nurodytoje
        newBmpFileLocation.

    Dvejetainiu skaiciu masyvas bitList turi tureti integer tipo sveikuju skaiciu elementus.
    bmp tipo failo vieta newBmpFileLocation turi buti str tipo kintamasis.
    Metodas grazina konvertuota bmp paveiksleli Image tipo kintamuoju.
    """

    # Konvertuojame bitu masyva i baitu masyva.
    bmpByteArray = [sum([byte[b] << b for b in range(0, 8)]) for byte in zip(*(iter(bitList),) * 8)]
    bmpByteArray = bytearray(bmpByteArray)

    # Konvertuojame baitu masyva i bmp failo paveiksleli.
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    bmpImgFile = Image.open(io.BytesIO(bmpByteArray))

    # bmp failas issaugojamas nurodytoje direktorijoje.
    bmpImgFile.save(newBmpFileLocation)

    return bmpImgFile


def bmp_to_bit_array_string_method(bmpFileLocation: str) -> List[int]:
    """Metodas, kuris konvertuoja bmp formata faila i dvejetaini formata.

    bmp tipo failo vieta bmpFileLocation turi buti str tipo kintamasis.
    Grazinamas integer tipo sveikuju skaiciu masyvas, kuris ir atitinka dvejetaini formata.
    """

    # Failas atidaromas su read binary rezimu.
    with open(bmpFileLocation, "rb") as bmpFile:
        encodedBmp = b64encode(bmpFile.read())

    return txt_conv.text_to_bit_array(encodedBmp.decode(txt_conv.g_text_encoding))


def bit_array_to_bmp_string_method(bitList: List[int], newBmpFileLocation: str):
    """Metodas, kuris konvertuoja dvejetainiu skaiciu seka i bmp tipo faila ir ta faila issaugo vietoje nurodytoje
        newBmpFileLocation.

    Dvejetainiu skaiciu masyvas bitList turi tureti integer tipo sveikuju skaiciu elementus.
    bmp tipo failo vieta newBmpFileLocation turi buti str tipo kintamasis.
    """

    encodedBmp = txt_conv.bit_array_to_text(bitList)

    # Failo vieta atidaroma su write binary rezimu.
    with open(newBmpFileLocation, "wb") as newBmpFile:
        newBmpFile.write(b64decode(encodedBmp.encode(txt_conv.g_text_encoding)))
