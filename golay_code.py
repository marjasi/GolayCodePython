from vector import Vector
from matrix import Matrix
from operations import vector_addition, remove_last_vector_element, merge_vectors, vector_matrix_multiplication
from operations import get_vector_weight, add_for_uneven_weight


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
        # Pirmasis masyvo elementas yra nulinis.
        if index + 1 == i:
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

    def check_matrix_b_rows(self, syndrome: Vector) -> tuple[Vector, bool]:
        """Metodas, kuris ivertina, ar yra tokia matricos B eilute i, su kuria
            sudauginus nurodyta sindromo vektoriu gautume vektoriu, kurio svoris
            mazesnis arba lygus 2.

        syndrome turi buti Vector klases tipo kintamasis.
        Metodas grazina reiksmiu rinkini, kurio pirmas elementas yra naujas klaidu vektorius,
         o antras elementas yra logine konstanta (True arba False), kuri pasako, ar buvo
         patenkintos vektoriaus svorio salygos, tai yra, ar radome klaidu vektoriu u.
        """

        for i in range(len(self.matrixB.rows)):
            matrixBRow = Vector(self.matrixB.rows[i], 0)
            sMatrixBRow = vector_addition(syndrome, matrixBRow)
            # Radome klaidu vektoriu.
            if get_vector_weight(sMatrixBRow) <= 2:
                return merge_vectors(sMatrixBRow, generate_ei_vector(i)), True

        # Neradome klaidu vektoriaus.
        return Vector([], 0), False

    def encode_vector(self, vector: Vector) -> Vector:
        """Metodas, kuris uzkoduoja vektoriu vector Golejaus kodu ir grazina uzkoduota vektoriu.

        vector turi buti Vector klases tipo kintamasis.
        Metodas grazina uzkoduota vektoriu.
        """

        return vector_matrix_multiplication(vector, self.matrixG)

    def decode_vector(self, vector: Vector) -> Vector:
        """Metodas, kuris dekoduoja vektoriu vector Golejaus kodu ir grazina dekoduota vektoriu.

        vector turi buti Vector klases tipo kintamasis.
        Metodas grazina dekoduota vektoriu receivedVector.
        """

        # Klaidu vektorius u.
        errorVector = Vector([], 0)
        errorVectorFound = False

        # Pridedame 0 ar 1, kad vektoriaus svoris butu nelyginis.
        receivedVector = Vector(add_for_uneven_weight(vector).elements, vector.essentialElemLen)

        print("Added 0 or 1 to vector:")
        print(receivedVector)

        # Apskaiciuojame sindroma s padaugine pailginta vektoriu receivedVector su matrica H.
        syndromeS = vector_matrix_multiplication(receivedVector, self.matrixH)

        print("Syndrome s:")
        print(syndromeS)

        # Jeigu vienetu skaicius mazesnis arba lygus trims, tai u = [s, 0].
        if get_vector_weight(syndromeS) <= 3:
            errorVector = merge_vectors(syndromeS, self.zeroVector)
            errorVectorFound = True
            print("Vektorius u = [s, 0]")
            print(errorVector)

        # Jeigu dar neradome klaidu vektoriaus u, ieskome i-osios matricos B eilutes, kur w(s+bi) <= 2.
        if not errorVectorFound:
            print("s svoris daugiau uz 3.")
            resultTuple = self.check_matrix_b_rows(syndromeS)
            errorVector = resultTuple[0]
            errorVectorFound = resultTuple[1]

        # Jeigu vis dar neradome klaidu vektoriaus u, skaiciuojame sindroma sB.
        if not errorVectorFound:
            syndromeSB = vector_matrix_multiplication(syndromeS, self.matrixB)
            # Jeigu vienetu skaicius mazesnis arba lygus trims, tai u = [0, sB].
            if get_vector_weight(syndromeSB) <= 3:
                errorVector = merge_vectors(self.zeroVector, syndromeSB)
                errorVectorFound = True
            # Jeigu dar neradome klaidu vektoriaus u, ieskome i-osios matricos B eilutes, kur w(sB+bi) <= 2.
            else:
                resultTuple = self.check_matrix_b_rows(syndromeSB)
                errorVector = resultTuple[0]
                errorVectorFound = resultTuple[1]

        # Sudedamas gautas vektorius w su klaidu vektoriumi u.
        receivedVector = vector_addition(receivedVector, errorVector)

        print("w + u")
        print(receivedVector)

        # Pasaliname paskutini vektoriaus receivedVector elementa.
        remove_last_vector_element(receivedVector)

        return receivedVector
