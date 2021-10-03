from comm_channel import CommChannel
from golay_code import GolayCode
from vector import Vector
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
