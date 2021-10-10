import operations as op
from vector import Vector
from matrix import Matrix


def generate_zero_vector() -> Vector:
    """Metodas, skirtas nulinio vektoriaus, kurio ilgis 12 sukurimui.

    Metodas grazina sukurta nulini vektoriu zeroVector.
    """

    zeroVector = Vector([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)

    return zeroVector


def generate_ei_vector(i: int) -> Vector:
    """Metodas, kuris sugeneruoja 12 ilgio vektoriu ei pagal paduota reiksme i.

    i turi buti integer tipo sveikasis skaicius.
    Metodas grazina sukurta ei vektoriu eiVector.
    """

    eiVector = generate_zero_vector()
    for index in range(len(eiVector.elements)):
        # i-ojoje pozicijoje bus vienetas. Pirma pozicija yra, kai i = 0.
        if index == i:
            eiVector.elements[index] = 1

    return eiVector


def generate_matrix_b() -> Matrix:
    """Metodas skirtas matricos B sukurimui.

    Metodas grazina sukurta matrica B.
    """

    matrixRows = [[1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
                  [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                  [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                  [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
                  [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                  [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                  [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                  [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                  [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                  [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

    return Matrix(matrixRows)


def generate_matrix_g() -> Matrix:
    """Metodas skirtas matricos G sukurimui.

    Metodas grazina sukurta matrica G.
    """

    matrixRows = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    return Matrix(matrixRows)


def generate_matrix_h() -> Matrix:
    """Metodas skirtas matricos H sukurimui.

    Metodas grazina sukurta matrica H.
    """

    matrixRows = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
                  [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                  [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                  [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
                  [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                  [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                  [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                  [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                  [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                  [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

    return Matrix(matrixRows)


class GolayCode:
    """Golejaus kodo operaciju klase.

    Atskira klase sukuriama, kad algoritmo kodas butu atskirtas nuo vartotojo sasajos.
    """

    # Matricos B, G ir H.
    matrixB = None
    matrixG = None
    matrixH = None

    def __init__(self):
        """Konstruktoriaus metodas.

        Sugeneruojamos reikalingos matricos ir nulinis vektorius.
        """

        self.matrixB = generate_matrix_b()
        self.matrixG = generate_matrix_g()
        self.matrixH = generate_matrix_h()
        self.zeroVector = generate_zero_vector()

    def check_matrix_b_rows(self, syndrome: Vector) -> tuple[Vector, int]:
        """Metodas, kuris ivertina, ar yra tokia matricos B eilute i, su kuria
            sudauginus nurodyta sindromo vektoriu gautume vektoriu, kurio svoris
            mazesnis arba lygus 2.

        syndrome turi buti Vector klases tipo kintamasis.
        Metodas grazina reiksmiu rinkini, kurio pirmas elementas yra vektorius sindromas + bi,
         o antras elementas yra matricos B eilutes, su kuria buvo rastas klaidu vektorius u, numeris.
        """

        for i in range(len(self.matrixB.rows)):
            matrixBRow = Vector(self.matrixB.rows[i], 0)
            sMatrixBRow = op.vector_addition(syndrome, matrixBRow)
            # Radome tinkama matricos B eilute i.
            if op.get_vector_weight(sMatrixBRow) <= 2:
                return sMatrixBRow, i

        # Neradome tinkamos matricos B eilutes i.
        return Vector([], 0), -1

    def encode_vector(self, vector: Vector) -> Vector:
        """Metodas, kuris uzkoduoja vektoriu vector Golejaus kodu ir grazina uzkoduota vektoriu.

        vector turi buti Vector klases tipo kintamasis.
        Metodas grazina uzkoduota vektoriu.
        """

        return op.vector_matrix_multiplication(vector, self.matrixG)

    def decode_vector(self, vector: Vector) -> tuple[Vector, str]:
        """Metodas, kuris dekoduoja vektoriu vector Golejaus kodu ir grazina dekoduota vektoriu.

        vector turi buti Vector klases tipo kintamasis.
        Metodas grazina rezultatu rinkini, kurio pirmas elementas yra dekoduotas vektorius,
         o antras elementas yra algoritmo vykdymo informacijos tekstas.
        """

        # Klaidu vektorius u.
        errorVector = Vector([], 0)
        errorVectorFound = False

        # Algoritmo vykdymo informacijos tekstas.
        algorithmLog = ""

        # Pridedame 0 ar 1, kad vektoriaus svoris butu nelyginis.
        receivedVector = Vector(op.add_for_uneven_weight(vector).elements, vector.essentialElemLen)

        algorithmLog += "Added 0 or 1 to distorted vector:"
        algorithmLog += "\n"
        algorithmLog += str(receivedVector)
        algorithmLog += "\n"

        # Apskaiciuojame sindroma s padaugine pailginta vektoriu receivedVector su matrica H.
        syndromeS = op.vector_matrix_multiplication(receivedVector, self.matrixH)

        algorithmLog += "Calculated syndrome s:"
        algorithmLog += "\n"
        algorithmLog += str(syndromeS)
        algorithmLog += "\n"

        # Jeigu vienetu skaicius mazesnis arba lygus trims, tai u = [s, 0].
        if op.get_vector_weight(syndromeS) <= 3:
            errorVector = op.merge_vectors(syndromeS, self.zeroVector)
            errorVectorFound = True
            algorithmLog += "Error vector u = [s, 0]:"
            algorithmLog += "\n"
            algorithmLog += str(errorVector)
            algorithmLog += "\n"

        # Jeigu dar neradome klaidu vektoriaus u, ieskome i-osios matricos B eilutes, kur w(s+bi) <= 2.
        if not errorVectorFound:
            algorithmLog += "Syndrome s weight is bigger than 3."
            algorithmLog += "\n"
            resultTuple = self.check_matrix_b_rows(syndromeS)
            # Jeigu vienetu skaicius mazesnis arba lygus dviems, tai u = [s + bi, ei].
            if resultTuple[1] != -1:
                errorVector = op.merge_vectors(resultTuple[0], generate_ei_vector(resultTuple[1]))
                errorVectorFound = True
                algorithmLog += "Error vector u = [s + bi, ei]:"
                algorithmLog += "\n"
                algorithmLog += str(errorVector)
                algorithmLog += "\n"
                algorithmLog += "i = "
                algorithmLog += str(resultTuple[1] + 1)
                algorithmLog += "\n"

        # Jeigu vis dar neradome klaidu vektoriaus u, skaiciuojame sindroma sB.
        if not errorVectorFound:
            syndromeSB = op.vector_matrix_multiplication(syndromeS, self.matrixB)
            algorithmLog += "Calculated syndrome sB:"
            algorithmLog += str(syndromeSB)
            algorithmLog += "\n"
            # Jeigu vienetu skaicius mazesnis arba lygus trims, tai u = [0, sB].
            if op.get_vector_weight(syndromeSB) <= 3:
                errorVector = op.merge_vectors(self.zeroVector, syndromeSB)
                errorVectorFound = True
                algorithmLog += "Error vector u = [0, sB]:"
                algorithmLog += "\n"
                algorithmLog += str(errorVector)
                algorithmLog += "\n"
            # Jeigu dar neradome klaidu vektoriaus u, ieskome i-osios matricos B eilutes, kur w(sB+bi) <= 2.
            else:
                algorithmLog += "Syndrome sB weight is bigger than 3."
                resultTuple = self.check_matrix_b_rows(syndromeSB)
                # Jeigu vienetu skaicius mazesnis arba lygus dviems, tai u = [ei, sB + bi].
                if resultTuple[1] != -1:
                    errorVector = op.merge_vectors(generate_ei_vector(resultTuple[1]), resultTuple[0])
                    errorVectorFound = True
                    algorithmLog += "Error vector u = [ei, sB + bi]:"
                    algorithmLog += "\n"
                    algorithmLog += str(errorVector)
                    algorithmLog += "\n"
                    algorithmLog += "i = "
                    algorithmLog += str(resultTuple[1] + 1)
                    algorithmLog += "\n"

        # Sudedamas gautas vektorius w su klaidu vektoriumi u.
        receivedVector = op.vector_addition(receivedVector, errorVector)

        algorithmLog += "Calculated encoded vector w and error vector u sum."
        algorithmLog += "\n"
        algorithmLog += "w + u:"
        algorithmLog += "\n"
        algorithmLog += str(receivedVector)
        algorithmLog += "\n"

        # Pasaliname paskutini vektoriaus receivedVector elementa.
        algorithmLog += "Received vector with last element removed:"
        algorithmLog += "\n"
        op.remove_last_vector_element(receivedVector)
        algorithmLog += str(receivedVector)
        algorithmLog += "\n"

        return receivedVector, algorithmLog
