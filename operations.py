from vector import Vector
from matrix import Matrix


def check_vector_len(vector: Vector) -> bool:
    """Metodas, kuris grazina True, jeigu vektoriaus vector ilgis yra 12, ir False, kitu atveju.

    vector turi buti Vector klases tipo objektas.
    """

    return len(vector.elements) == 12


def fill_vector_zeros(vector: Vector):
    """Metodas, kuris pripildo vektoriu vector nuliais iki 12 ilgio.

    vector turi buti Vector klases tipo objektas.
    """

    # Pripildome vektoriu nuliais, kol vektoriaus ilgis nera 12
    while not check_vector_len(vector):
        vector.elements.append(0)


def format_result_mod2(result: int):
    """Metodas, kuris grazina 0 arba 1 priklausomai nuo result liekanos su skaiciumi 2 (mod 2).

    result turi buti integer tipo sveikas skaicius.
    """

    return result % 2


def vector_addition(firstVector: Vector, secondVector: Vector) -> Vector:
    """Metodas, kuris realizuoja dvieju vektoriu sudeties operacija.

    firstVector ir secondVector turi buti Vector klases tipo kintamieji, kuriu ilgiai sutampa.
    Metodas grazina nauja vektoriu resultVector, kuris yra vektoriu sudeties rezultatas.
    Rezultato vektoriui jau yra pritaikyta mod 2 operacija.
    """

    # Tuscias vektorius.
    resultVector = Vector([], 0)

    # Jeigu vektoriu ilgiai nesutampa, bus grazintas tuscias vektorius.
    if len(firstVector.elements) == len(secondVector.elements):
        for firstElement, secondElement in zip(firstVector.elements, secondVector.elements):
            resultVector.elements.append(format_result_mod2(firstElement + secondElement))

        # Imame pirmo metodui paduoto vektoriaus esminiu elementu skaiciu.
        resultVector.essentialElemLen = firstVector.essentialElemLen

    return resultVector


def vector_matrix_multiplication(vector: Vector, matrix: Matrix) -> Vector:
    """Metodas, kuris realizuoja vektoriaus vector ir matricos matrix daugyba.

    vector turi buti Vector klases tipo kintamasis, o matrix turi buti Matrix klases tipo kintamasis.
    Metodas grazina nauja vektoriu resultVector, kuris yra vektoriaus ir matricos daugybos rezultatas.
    Rezultato vektoriui jau yra pritaikyta mod 2 operacija.
    """

    # Tuscias vektorius.
    resultVector = Vector([], 0)

    # Turi sutapti vektoriaus stulpeliu skaicius ir matricos eiluciu skaicius.
    if len(vector.elements) == len(matrix.rows):
        # Rezultatas bus vektorius, kurio ilgis atitinka matricos stulpeliu skaiciu.
        for index in range(len(matrix.rows[0])):
            columnSum = 0
            # Sudauginame vektoriaus elementus su index-ojo matricos stulpelio elementais ir apskaiciuojame suma.
            for vectIndex in range(len(vector.elements)):
                columnSum += vector.elements[vectIndex] * matrix.rows[vectIndex][index]

            # Apskaiciuota suma yra index-asis rezultatu vektoriaus elementas.
            resultVector.elements.append(format_result_mod2(columnSum))

        resultVector.essentialElemLen = vector.essentialElemLen

    return resultVector
