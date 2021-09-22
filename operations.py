from vector import Vector


def vector_addition(firstVector: Vector, secondVector: Vector) -> Vector:
    """Metodas, kuris realizuoja dvieju vektoriu sudeties operacija.

    firstVector ir secondVector turi buti Vector klases tipo kintamieji, kuriu ilgiai sutampa.
    Metodas grazina nauja vektoriu newVector, kuris yra vektoriu sudeties rezultatas.
    """

    # Jeigu vektoriu ilgiai nesutampa, bus grazintas tuscias vektorius.
    newVector = Vector([], 0)

    if len(firstVector.elements) == len(secondVector.elements):
        for firstElement, secondElement in zip(firstVector.elements, secondVector.elements):
            newVector.elements.append(format_result_mod2(firstElement + secondElement))
        newVector.essentialElemLen = firstVector.essentialElemLen

    return newVector


def format_result_mod2(result: int):
    """Metodas, kuris grazina 0 arba 1 priklausomai nuo result liekanos su skaiciumi 2 (mod 2).

    result turi buti integer tipo sveikas skaicius.
    """

    return result % 2
