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
