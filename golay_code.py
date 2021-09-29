from vector import Vector
from matrix import Matrix
import operations as op


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

    def decode_vector(self, vector: Vector) -> Vector:
        """Metodas, kuris dekoduoja vektoriu vector Golejaus kodu ir grazina dekoduota vektoriu.

        vector turi buti Vector klases tipo kintamasis.
        Metodas grazina dekoduota vektoriu receivedVector.
        """

        # Klaidu vektorius u.
        errorVector = Vector([], 0)
        errorVectorFound = False

        # Pridedame 0 ar 1, kad vektoriaus svoris butu nelyginis.
        receivedVector = Vector(op.add_for_uneven_weight(vector).elements, vector.essentialElemLen)

        print("Added 0 or 1 to vector:")
        print(receivedVector)

        # Apskaiciuojame sindroma s padaugine pailginta vektoriu receivedVector su matrica H.
        syndromeS = op.vector_matrix_multiplication(receivedVector, self.matrixH)

        print("Syndrome s:")
        print(syndromeS)

        # Jeigu vienetu skaicius mazesnis arba lygus trims, tai u = [s, 0].
        if op.get_vector_weight(syndromeS) <= 3:
            errorVector = op.merge_vectors(syndromeS, self.zeroVector)
            errorVectorFound = True
            print("Vektorius u = [s, 0]")
            print(errorVector)

        # Jeigu dar neradome klaidu vektoriaus u, ieskome i-osios matricos B eilutes, kur w(s+bi) <= 2.
        if not errorVectorFound:
            print("Sindromo s svoris didesnis uz 3.")
            resultTuple = self.check_matrix_b_rows(syndromeS)
            # Jeigu vienetu skaicius mazesnis arba lygus dviems, tai u = [s + bi, ei].
            if resultTuple[1] != -1:
                errorVector = op.merge_vectors(resultTuple[0], generate_ei_vector(resultTuple[1]))
                errorVectorFound = True
                print("Vektorius u = [s + bi, ei]")
                print(errorVector)
                print("i = ")
                print(resultTuple[1] + 1)

        # Jeigu vis dar neradome klaidu vektoriaus u, skaiciuojame sindroma sB.
        if not errorVectorFound:
            syndromeSB = op.vector_matrix_multiplication(syndromeS, self.matrixB)
            print("Syndrome sB:")
            print(syndromeSB)
            # Jeigu vienetu skaicius mazesnis arba lygus trims, tai u = [0, sB].
            if op.get_vector_weight(syndromeSB) <= 3:
                errorVector = op.merge_vectors(self.zeroVector, syndromeSB)
                errorVectorFound = True
                print("Vektorius u = [0, sB]")
                print(errorVector)
            # Jeigu dar neradome klaidu vektoriaus u, ieskome i-osios matricos B eilutes, kur w(sB+bi) <= 2.
            else:
                print("Sindromo sB svoris didesnis uz 3.")
                resultTuple = self.check_matrix_b_rows(syndromeSB)
                # Jeigu vienetu skaicius mazesnis arba lygus dviems, tai u = [ei, sB + bi].
                if resultTuple[1] != -1:
                    errorVector = op.merge_vectors(generate_ei_vector(resultTuple[1]), resultTuple[0])
                    errorVectorFound = True
                    print("Vektorius u = [ei, sB + bi]")
                    print(errorVector)
                    print("i = ")
                    print(resultTuple[1] + 1)

        # Sudedamas gautas vektorius w su klaidu vektoriumi u.
        receivedVector = op.vector_addition(receivedVector, errorVector)

        print("w + u = ")
        print(receivedVector)

        # Pasaliname paskutini vektoriaus receivedVector elementa.
        op.remove_last_vector_element(receivedVector)

        return receivedVector
