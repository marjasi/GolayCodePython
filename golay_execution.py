# Biblioteka naudojama objektu kopijoms kurti.
import copy
import operations as op
import text_conversion as txt_conv
import bmp_conversion as bmp_conv
# Treciuju saliu biblioteka naudojama darbui su paveiksleliais.
from PIL import Image
from comm_channel import CommChannel
from golay_code import GolayCode
from vector import Vector
# Bibloteka naudojama tipu apibrezimams, kurie nurodomi metodu parametrams ir grazinamoms reiksmems.
from typing import List


class GolayExecution:
    """Klase, kuri naudoja kitas projekto klases ir metodus uzduoties scenariju realizavimui."""

    # Komunikacijos kanalas bei Golejaus kodo algoritmo klase.
    commChannel = None
    golayCode = None

    def __init__(self, commChannel: CommChannel, golayCode: GolayCode):
        """Konstruktoriaus metodas.

        GolayExecution klasei perduodamos CommChannel ir GolayCode klases.
        commChannel turi buti CommChannel klases tipo kintamasis.
        commChannel turi buti GolayCode klases tipo kintamasis.
        """

        self.commChannel = commChannel
        self.golayCode = golayCode

    def get_distortion_probability(self) -> float:
        """Metodas, kuris grazine dabartine komunikacijos kanalo iskraipymo tikimybe.

        Grazinama iskraipymo tikimybe yra float tipo realus skaicius.
        """

        return self.commChannel.get_prob_of_error()

    def set_distortion_probability(self, distortionProbability: float):
        """Metodas nustato nauja kanalo iskraipymo tikimybe.

        Parametras probOfError turi buti float tipo realusis skaicius.
        """

        return self.commChannel.set_prob_of_error(distortionProbability)

    def encode_vector(self, vector: Vector) -> Vector:
        """Metodas, kuris uzkoduoja paduota vektoriu vector.

        vector turi buti Vector klases tipo kintamasis.
        Metodas grazina nauja Vector klases vektoriu, kuris yra uzkoduotas.
        """

        encodedVector = self.golayCode.encode_vector(vector)
        return encodedVector

    def decode_vector(self, encodedVector: Vector) -> tuple[Vector, str]:
        """Metodas, kuris dekoduoja uzkoduota vektoriu encodedVector.

        Metodas grazina rezultatu rinkini, kurio pirmas elementas yra dekoduotas vektorius,
         o antras elementas yra algoritmo vykdymo informacijos tekstas.
        """

        decodedVector, algorithmLog = self.golayCode.decode_vector(encodedVector)

        # Paliekame tik tuos elementus, kurie yra esminiai.
        decodedVector.elements = decodedVector.elements[0:decodedVector.essentialElemLen]
        return decodedVector, algorithmLog

    def send_vector(self, vector: Vector) -> Vector:
        """Metodas, kuris komunikacijos kanalu nusiuncia vektoriu vector ir grazina is kanalo gauta vektoriu.

        vector turi buti Vector klases tipo kintamasis.
        Metodas grazina is kanalo gauta Vector klases vektoriu.
        """

        receivedVector = Vector(self.commChannel.send_binary_info(vector.elements), vector.essentialElemLen)
        return receivedVector

    def send_text(self, text: str) -> tuple[str, str]:
        """Metodas, kuris persiuncia nekoduota ir uzkoduota teksta komunikacijos kanalu.

        text turi buti str tipo kintamasis.
        Metodas grazina rezultatu rinkini, kurio pirmas elementas yra is kanalo gautas nekoduotas tekstas,
         o antras elementas yra is kanalo gautas uzkoduotas tekstas.
        """

        try:
            return self.send_raw_text(text), self.send_encoded_text(text)
        # Jeigu negalime dekoduoti gauto is kanalo teksto i tekstini unicode formata, graziname specifini pranesima.
        except UnicodeDecodeError:
            errorMessage = "**ERROR**UNABLE**TO**DECODE**TEXT**CORRUPTION**AT*CRITICAL**LEVELS**"
            return errorMessage, errorMessage

    def send_image_bit_data(self, imageDirectory: str, saveFiles=True) -> tuple[Image, Image]:
        """Metodas, kuris kanalu nusiuncia paveiksleli esanti imageDirectory dviem budais: uzkodavus ir nekodavus.
        Metodas grazina gautus is kanalo paveikslelius.
        Gauti is kanalo paveiksleliai taip pat yra issaugomi toje pacioje direktorijoje
         kaip ir pasirinktas paveikslelis, jeigu saveFiles yra True.
        Failu pavadinimai sudaromi pridejus prefiksus raw ir enc prie originalaus paveikslelio pavadinimo.

        imageDirectory turi buti str tipo kintamasis.
        imageDirectory yra paveikslelio buvimo vieta.
        saveFiles turi buti bool tipo kintamasis.
        saveFiles pagal nutylejima yra True.
        Metodas grazina rezultatu rinkini, kurio pirmas elementas yra gautas is kanalo neuzkoduotas paveikslelis,
         o antras elementas - gautas is kanalo uzkoduotas paveikslelis.
        """

        rawImg = bmp_conv.bmp_to_bit_array(imageDirectory)

        # Su giliaja kopija sukuriame du identisko turinio masyvus, kurie yra skirtingi objektai.
        encodedImg = copy.deepcopy(rawImg)

        # Atskiriame .bmp failu antrasciu informacija nuo failo turinio informacijos.
        # .bmp failo antrastes dydis priklauso nuo .bmp failo formato.
        # Pavyzdziui, .bmp failu saugojimui daznai naudojama yra Windows V3 BMP antraste, kurios dydis yra 40 baitu.
        # Prie to dar pridedame failo informacijos antraste, kurios dydis yra 14 baitu.
        # Turime 54 baitu antraste. Tai yra 54 * 8 = 432 bitai, tad ju ir neiskraipysime.
        rawImg = op.separate_list_into_two_chunks(rawImg, 432)
        encodedImg = op.separate_list_into_two_chunks(encodedImg, 432)

        # Kanalu siunciame tik paveiksleliu turinio informacija.
        rawImg[1] = self.send_bit_array(rawImg[1], False)
        encodedImg[1] = self.send_bit_array(encodedImg[1], True)

        # Sujungiame paveiksleliu turinio informacija su antrastes informacija.
        rawImg = op.merge_sublists(rawImg)
        encodedImg = op.merge_sublists(encodedImg)

        # Randame paveikslelio direktorijos kelia ir paveikslelio pavadinima.
        imgDirectory, imgFileName = op.get_directory_and_file_name(imageDirectory)

        # Sudarome is kanalo gautu paveiksleliu direktorijos kelius.
        rawImgLocation = copy.deepcopy(imgDirectory)
        rawImgLocation += "\\raw"
        rawImgLocation += copy.deepcopy(imgFileName)
        encodedImgLocation = copy.deepcopy(imgDirectory)
        encodedImgLocation += "\\enc"
        encodedImgLocation += copy.deepcopy(imgFileName)

        if saveFiles:
            # Issaugome is kanalo gautus paveikslelius direktorijoje.
            rawImg = bmp_conv.bit_array_to_bmp(rawImg, rawImgLocation)
            encodedImg = bmp_conv.bit_array_to_bmp(encodedImg, encodedImgLocation)

        return rawImg, encodedImg

    def send_image(self, imageDirectory: str) -> tuple[Image, Image]:
        """Metodas, kuris kanalu nusiuncia paveiksleli esanti imageDirectory dviem budais: uzkodavus ir nekodavus.
        Metodas grazina gautus is kanalo paveikslelius.
        Gauti is kanalo paveiksleliai taip pat yra issaugomi toje pacioje direktorijoje
         kaip ir pasirinktas paveikslelis.
        Failu pavadinimai sudaromi pridejus prefiksus raw ir enc prie originalaus paveikslelio pavadinimo.

        imageDirectory turi buti str tipo kintamasis.
        imageDirectory yra paveikslelio buvimo vieta.
        Metodas grazina rezultatu rinkini, kurio pirmas elementas yra gautas is kanalo neuzkoduotas paveikslelis,
         o antras elementas - gautas is kanalo uzkoduotas paveikslelis.
        """

        rawImg = bmp_conv.bmp_to_bit_array(imageDirectory)

        # Su giliaja kopija sukuriame du identisko turinio masyvus, kurie yra skirtingi objektai.
        encodedImg = copy.deepcopy(rawImg)

        # Atskiriame .bmp failu antrasciu informacija nuo failo turinio informacijos.
        # Kadangi konvertuojame dvejetaini formata i base64 formata ir tada interpretuojame base64 kaip
        #  teksta UTF-16 formatu, kuri konvertuojame i dvejetaini formata, antrastes informacija
        #  sudarys pirmi 608 bitai.
        # .bmp failo antraste dvejetainiame formate yra 14 baitu dydzio. Tai bus 112 bitu.
        # Tada base64 vienas simbolis apibudina 6 bitus. Tad musu 112 bitu yra apie 19 base64 simboliu.
        # UTF-16 formate vienam simboliui gali buti skiriama iki 4 baitu. Tad base64 19 simboliu bus skiriami 76 baitai.
        # Vadinasi, antrastes informacija bus 608 bitu ilgio.
        rawImg = op.separate_list_into_two_chunks(rawImg, 608)
        encodedImg = op.separate_list_into_two_chunks(encodedImg, 608)

        # Kanalu siunciame tik paveiksleliu turinio informacija.
        rawImg[1] = self.send_bit_array(rawImg[1], False)
        encodedImg[1] = self.send_bit_array(encodedImg[1], True)

        # Sujungiame paveiksleliu turinio informacija su antrastes informacija.
        rawImg = op.merge_sublists(rawImg)
        encodedImg = op.merge_sublists(encodedImg)

        # Randame paveikslelio direktorijos kelia ir paveikslelio pavadinima.
        imgDirectory, imgFileName = op.get_directory_and_file_name(imageDirectory)

        # Sudarome is kanalo gautu paveiksleliu direktorijos kelius.
        rawImgLocation = copy.deepcopy(imgDirectory)
        rawImgLocation += "raw"
        rawImgLocation += copy.deepcopy(imgFileName)
        encodedImgLocation = copy.deepcopy(imgDirectory)
        encodedImgLocation += "enc"
        encodedImgLocation += copy.deepcopy(imgFileName)

        # Issaugome is kanalo gautus paveikslelius direktorijoje.
        bmp_conv.bit_array_to_bmp(rawImg, rawImgLocation)
        bmp_conv.bit_array_to_bmp(encodedImg, encodedImgLocation)

        return rawImg, encodedImg

    def send_bit_array(self, bitArray: List[int], encode: bool) -> List[int]:
        """Metodas, kuris nusiuncia dvejetainio formato informacijos masyva kanalu.

        bitArray turi buti masyvas, kurio elementai yra int tipo sveikieji skaiciai.
        encode turi buti bool tipo kintamasis.
        Jeigu encode yra True, tai dvejetaine informacija bus uzkoduota pries siuntima kanalu.
        Jeigu encode yra False, tai dvejetaine informacija nebus uzkoduota pries siuntima kanalu.
        Metodas grazina is kanalo gauna dvejetaines informacijos masyva.
        Grazinti masyvo elementai yra int tipo sveikieji skaiciai.
        """

        # Gautos dvejetaines informacijos masyvas.
        receivedBitArray = []

        # Gauta dvejetainiu skaiciu masyva padalijame i ilgio 12 gabalus.
        dividedBitArray = list(op.divide_list_to_chunks(bitArray, 12))

        for chunk in dividedBitArray:
            # Is kiekvieno gabalo sukuriame vektoriu ir ji apdorojame atskirai.
            # Isimename, kiek esminio turinio elementu yra kiekviename gabale - paskutiniame gali buti maziau nei 12.
            vector = Vector(chunk, len(chunk))

            # Vektoriu pripildome nuliais, jeigu jo ilgis mazesnis nei 12.
            op.fill_vector_zeros(vector)

            if encode:
                # Uzkoduojamas vektorius.
                vector = self.encode_vector(vector)

            # Is kanalo gautas iskraipytas vektorius.
            receivedVector = self.send_vector(vector)

            if encode:
                # Dekoduojamas is kanalo gautas vektorius.
                resultTuple = self.decode_vector(receivedVector)
                receivedVector = resultTuple[0]

            if not encode:
                # Pasiimame esmini turini is vektoriaus ir ji pridedame prie gauto teksto masyvo.
                receivedVector.elements = receivedVector.elements[0:receivedVector.essentialElemLen]

            for element in receivedVector.elements:
                receivedBitArray.append(element)

        return receivedBitArray

    def send_raw_text(self, text: str) -> str:
        """Metodas, kuris persiuncia nekoduota teksta komunikacijos kanalu.

        text turi buti str tipo kintamasis.
        Metodas grazina is kanalo gauta nekoduota teksta str tipo kintamuoju.
        """

        # Tekstas konvertuojamas i dvejetaini formata.
        textBitArray = txt_conv.text_to_bit_array(text)

        return txt_conv.bit_array_to_text(self.send_bit_array(textBitArray, False))

    def send_encoded_text(self, text: str) -> str:
        """Metodas, kuris persiuncia uzkoduota teksta komunikacijos kanalu.

        text turi buti str tipo kintamasis.
        Metodas grazina is kanalo gauta uzkoduota teksta str tipo kintamuoju.
        """

        # Tekstas konvertuojamas i dvejetaini formata.
        textBitArray = txt_conv.text_to_bit_array(text)

        return txt_conv.bit_array_to_text(self.send_bit_array(textBitArray, True))

    def conduct_experiment(self, repeatNumber: int):
        """Metodas, kuris ivykdo nurodyta kieki eksperimentu ir ju rezultatus
            issaugo Excel faile experimentResults.xlsx.

        repeatNumber turi buti int tipo sveikasis skaicius.
        repeatNumber yra vykdomu eksperimentu kiekis.
        """

        return None

    def get_error_num_positions(self, encodedVector: Vector, receivedVector: Vector, increasePositionValues=False)\
            -> tuple[int, List[int]]:
        """Metodas, kuris suskaiciuoja, kiek yra skirtumu tarp dvieju vektoriu ir pateikia,
            kuriose vietose yra tie skirtumai.

        encodedVector turi buti Vector klases tipo kintamasis.
        encodedVector yra uzkoduotas vektorius, kuris dar nebuvo siustas kanalu.
        receivedVector turi buti Vector klases tipo kintamasis.
        receivedVector yra jau kanalu siustas ir is kanalo gautas vektorius.
        increasePositionValues turi buti bool tipo kintamasis.
        Pagal nutylejima increasePositionValues yra False.
        Jeigu increasePositionValues yra True, tai poziciju skaiciai bus padidinti vienetu ir tiks atveju, jeigu
         pirmoji pozicija yra nuo vieneto.
        Jeigu increasePositionValues yra False, tai poziciju skaiciui nebus padidinti vienetu, pirma pozicija bus
         nuo nulio.
        Metodas grazina rezultatu rinkini, kurio pirmas elementas yra klaidu skaicius, o antras elementas yra pozicijos,
         kuriose ivyko klaidos.
        """

        vectorErrorNum = op.get_vector_errors(encodedVector, receivedVector)
        vectorErrorPos = op.get_vector_error_positions(encodedVector, receivedVector)

        if increasePositionValues:
            op.increase_list_values(vectorErrorPos, 1)

        return vectorErrorNum, vectorErrorPos
