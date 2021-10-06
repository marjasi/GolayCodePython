from comm_channel import CommChannel
from golay_code import GolayCode
from vector import Vector
from typing import List
import operations as op
import text_conversion as txt_conv
import bmp_conversion as bmp_conv


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
        # Jeigu negalime dekoduoti gauti is kanalo teksto i tekstini unicode formata, graziname specifini pranesima.
        except UnicodeDecodeError:
            errorMessage = "**ERROR**UNABLE**TO**DECODE**TEXT**CORRUPTION**AT*CRITICAL**LEVELS**"
            return errorMessage, errorMessage

    def send_raw_text(self, text: str) -> str:
        """Metodas, kuris persiuncia nekoduota teksta komunikacijos kanalu.

        text turi buti str tipo kintamasis.
        Metodas grazina is kanalo gauta nekoduota teksta str tipo kintamuoju.
        """

        # Gauto teksto masyvas.
        receivedTextBitArray = []

        # Tekstas konvertuojamas i dvejetaini formata.
        textBitArray = txt_conv.text_to_bit_array(text)

        # Gauta dvejetainiu skaiciu masyva padalijame i ilgio 12 gabalus.
        textBitArray = list(op.divide_list_to_chunks(textBitArray, 12))

        for chunk in textBitArray:
            # Is kiekvieno gabalo sukuriame vektoriu ir ji apdorojame atskirai.
            # Isimename, kiek esminio turinio elementu yra kiekviename gabale - paskutiniame gali buti maziau nei 12.
            vector = Vector(chunk, len(chunk))

            # Vektoriu pripildome nuliais, jeigu jo ilgis mazesnis nei 12.
            op.fill_vector_zeros(vector)

            # Is kanalo gautas iskraipytas vektorius.
            receivedVector = self.send_vector(vector)

            # Pasiimame esmini turini is vektoriaus ir ji pridedame prie gauto teksto masyvo.
            receivedVector.elements = receivedVector.elements[0:receivedVector.essentialElemLen]

            for element in receivedVector.elements:
                receivedTextBitArray.append(element)

        return txt_conv.bit_array_to_text(receivedTextBitArray)

    def send_encoded_text(self, text: str) -> str:
        """Metodas, kuris persiuncia uzkoduota teksta komunikacijos kanalu.

        text turi buti str tipo kintamasis.
        Metodas grazina is kanalo gauta uzkoduota teksta str tipo kintamuoju.
        """

        # Gauto teksto masyvas.
        receivedTextBitArray = []

        # Tekstas konvertuojamas i dvejetaini formata.
        textBitArray = txt_conv.text_to_bit_array(text)

        # Gauta dvejetainiu skaiciu masyva padalijame i ilgio 12 gabalus.
        textBitArray = list(op.divide_list_to_chunks(textBitArray, 12))

        for chunk in textBitArray:
            # Is kiekvieno gabalo sukuriame vektoriu ir ji apdorojame atskirai.
            # Isimename, kiek esminio turinio elementu yra kiekviename gabale - paskutiniame gali buti maziau nei 12.
            vector = Vector(chunk, len(chunk))

            # Vektoriu pripildome nuliais, jeigu jo ilgis mazesnis nei 12.
            op.fill_vector_zeros(vector)

            # Uzkoduojamas vektorius.
            encodedVector = self.encode_vector(vector)

            # Is kanalo gautas iskraipytas vektorius.
            receivedVector = self.send_vector(encodedVector)

            # Dekoduojamas is kanalo gautas vektorius.
            resultTuple = self.decode_vector(receivedVector)
            decodedVector = resultTuple[0]

            # Pridedame esmini turini prie gauto teksto masyvo.
            for element in decodedVector.elements:
                receivedTextBitArray.append(element)

        return txt_conv.bit_array_to_text(receivedTextBitArray)

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
