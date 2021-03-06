# Biblioteka naudojama objektu kopijoms kurti.
import copy
# Biblietka naudojama darbui su failu direktorijomis.
import ntpath
# Bibloteka naudojama tipu apibrezimams, kurie nurodomi metodu parametrams ir grazinamoms reiksmems.
from typing import List
from vector import Vector
from matrix import Matrix


def divide_list_to_chunks(listToDivide: List[int], chunkSize: int) -> List[int]:
    """Metodas, kuris masyva listToDivide isskaido i gabalus, kurie yra chunkSize dydzio.

    Skaidomas masyvas listToDivide turi tureti elementus, kurie yra integer tipo sveikieji skaiciai.
    Gabalu dydis chunkSize turi buti integer tipo sveikasis skaicius.
    Metodas grazina isskaidyta gabala kaip masyva, kurio elementai yra integer tipo sveikieji skaiciai.
    """

    # Zodis yield leidzia metodui grazinti nurodyta reiksme ir toliau vykdyti cikla, kol jis baigsis.
    # Isimenama metodo busena pries gabalo grazinima ir tada programos vykdymui
    #  grizus i metoda atitinkamai tesiamas ciklo vykdymas.
    for index in range(0, len(listToDivide), chunkSize):
        yield listToDivide[index:index + chunkSize]


def increase_list_values(listToIncrease: List[int], increaseAmount: int) -> List[int]:
    """Metodas, kuris kiekviena masyvo listToIncrease elementa padidina reiksme increaseAmount.

    Metodas grazina masyva listToIncrease, kuriame elementai buvo padidinti increaseAmount
     reiksme.
    """

    for index in range(len(listToIncrease)):
        listToIncrease[index] += increaseAmount

    return listToIncrease


def get_directory_and_file_name(fullDirectoryPath: str) -> tuple[str, str]:
    """Metodas, kuris pilname direktorijos aprase suranda direktorijos aplanko ir failo pavadinimo reiksmes.

    fullDirectoryPath turi buti str tipo kintamasis.
    fullDirectoryPath yra pilna direktorijos kelias.
    Metodas grazina rezultatu rinkini, kurio pirmas elementas yra direktorijos aplanko kelias,
     o antras elementas - failo pavadinimas.
    """

    return ntpath.dirname(fullDirectoryPath), ntpath.basename(fullDirectoryPath)


def check_vector_len(vector: Vector) -> bool:
    """Metodas, kuris grazina True, jeigu vektoriaus vector ilgis yra 12, ir False, kitu atveju.

    vector turi buti Vector klases tipo kintamasis.
    """

    return len(vector.elements) == 12


def separate_list_into_two_chunks(listToSeparate: List, firstChunkLength: int) -> List:
    """Metodas, kuris issakdio masyva list i du gabalus.
    Pirmo gabalo ilgis yra firstChunkLength.
    Antras gabalas apima visa likusia masyvo dali.

    listToSeparate turi buti List tipo kintamasis.
    firstChunkLength turi buti int tipo sveikasis skaicius.
    Metodas grazina nauja masyva, kurio pirmas elementas yra masyvo listToSeparate pirmas gabalas, o antras elementas
     yra masyvo listToSeparate antras gabalas.
    """

    separatedList = [copy.deepcopy(listToSeparate[0:firstChunkLength]),
                     copy.deepcopy(listToSeparate[firstChunkLength:])]

    return separatedList


def merge_sublists(listWithSublists: List) -> List:
    """Metodas, kuris sujungia masyvo gabalus i vientisa masyva.

    listWithSublists turi buti List klases tipo kintamasis.
    listWithSublists yra masyvas, kurio elementai yra masyvai, tai yra, masyvas, kuris padalintas i gabalus.
    Metodas grazina sujungta masyva.
    """

    # for element atrenka listWithSublists gabalus kaip sublist ir tada parenkamas kiekvienas sublist elementas
    #  element, kuris dedamas i galutini masyva mergedList.
    # Kitaip sakant: praiteruojam listWithSublists gabalus ir kiekvieno gabalo kiekviena elementa.
    mergedList = [sublist for element in listWithSublists for sublist in element]

    return mergedList


def remove_last_vector_element(vector: Vector):
    """Metodas, kuris pasalina paskutini vektoriaus vector elementa.

    vector turi buti Vector klases tipo kintamasis.
    """

    if len(vector.elements) > 0:
        del vector.elements[-1]


def create_vector_from_string(bitString: str) -> Vector:
    """Metodas, kuris sukuria nauja Vector klases objetkaa pagal reiksmes esancias bitString tekste.

    bitString turi buti str tipo kintamasis.
    Metodas grazina Vector klases tipo objekta.
    """

    # Vektoriaus elementai.
    vectorElements = []

    for char in bitString:
        if char == "1":
            vectorElements.append(1)
        elif char == "0":
            vectorElements.append(0)

    # Jeigu vektorius yra ilgesnis uz 12, jo esminio turinio ilgis visada bus 12.
    if len(vectorElements) > 12:
        return Vector(vectorElements, 12)
    else:
        return Vector(vectorElements, len(vectorElements))


def fill_vector_zeros(vector: Vector):
    """Metodas, kuris pripildo vektoriu vector nuliais iki 12 ilgio.

    vector turi buti Vector klases tipo kintmasis.
    """

    # Pripildome vektoriu nuliais, kol vektoriaus ilgis nera 12
    while not check_vector_len(vector):
        vector.elements.append(0)


def merge_vectors(firstVector: Vector, secondVector: Vector) -> Vector:
    """Metodas, kuris sujungia vektoriu firstVector su vektoriumi secondVector.

    firstVector ir secondVector turi buti Vector klases tipo kintamieji.
    Metodas grazina sujungta vektoriu mergedVector.
    """

    mergedVectorElements = []
    mergedVectorElements.extend(firstVector.elements)
    mergedVectorElements.extend(secondVector.elements)

    mergedVector = Vector(mergedVectorElements, firstVector.essentialElemLen)

    return mergedVector


def get_vector_weight(vector: Vector) -> int:
    """Metodas, kuris grazina vektoriaus vector svori - vienetu skaiciu vektoriuje vector.

    vector turi buti vector klases tipo kintamasis.
    Vektoriuje grazinamas vienetu skaicius weight yra integer tipo sveikasis skaicius.
    """

    weight = 0

    for element in vector.elements:
        if element == 1:
            weight += 1

    return weight


def add_for_uneven_weight(vector: Vector) -> Vector:
    """Metodas, kuris prideda 0 ar 1 prie vektoriaus vector galo, kad vienetu skaicius butu nelygynis.

    vector turi buti Vector klases tipo kintamasis.
    Metodas grazina vektoriu addedVector su prirasytu 0 ar 1 .
    """

    addedVector = Vector(copy.deepcopy(vector.elements), vector.essentialElemLen)

    if get_vector_weight(addedVector) % 2 == 0:
        addedVector.elements.append(1)
    else:
        addedVector.elements.append(0)

    return addedVector


def get_vector_errors(sentVector: Vector, receivedVector: Vector) -> int:
    """Metodas palygina siunciama vektoriu sentVector su gautu is kanalo vektoriumi receivedVector ir grazina
        vektoriaus iskraipymu kanale skaiciu.
        
    sentVector ir receivedVector turi buti Vector klases tipo kintamieji,
    Grazinamas iskraipymu skaicius errorCount yra integer tipo sveikas skaicius.
    """

    errorCount = 0

    for index in range(len(sentVector.elements)):
        if sentVector.elements[index] != receivedVector.elements[index]:
            errorCount += 1

    return errorCount


def get_vector_error_positions(sentVector: Vector, receivedVector: Vector) -> List[int]:
    """Metodas palygina siunciama vektoriu sentVector su gautu is kanalo vektoriumi receivedVector ir grazina
        pozicijas, kuriose buvo padaryti iskraipymai.

    sentVector ir receivedVector turi buti Vector klases tipo kintamieji,
    Grazinamas iskraipymu vietu masyvas errorPositions, kurio elementai yra integer tipo sveikieji skaiciai.
    """

    errorPositions = []

    for index in range(len(sentVector.elements)):
        if sentVector.elements[index] != receivedVector.elements[index]:
            errorPositions.append(index)

    return errorPositions


def format_result_mod2(result: int):
    """Metodas, kuris grazina 0 arba 1 priklausomai nuo result liekanos su skaiciumi 2 (mod 2).

    result turi buti integer tipo sveikas skaicius.
    """

    return result % 2


def vector_addition(firstVector: Vector, secondVector: Vector) -> Vector:
    """Metodas, kuris realizuoja dvieju vektoriu sudeties operacija.

    firstVector ir secondVector turi buti Vector klases tipo kintamieji, kuriu ilgiai sutampa.
    Metodas grazina nauja vektoriu resultVector, kuris yra vektoriu sudeties rezultatas.
    Rezultato vektoriui resultVector jau yra pritaikyta mod 2 operacija.
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
    Rezultato vektoriui resultVector jau yra pritaikyta mod 2 operacija.
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
