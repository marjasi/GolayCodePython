from golay_code import *
from vector import Vector
from comm_channel import *
from operations import vector_addition, vector_matrix_multiplication, check_vector_len, fill_vector_zeros, get_vector_errors


def main():
    golayCode = GolayCode()
    channel = CommChannel(0.1)
    print("Vector to be encoded:")
    vector = Vector([0, 0, 0, 1, 0, 0], 12)
    fill_vector_zeros(vector)
    print(vector)
    print("Vector after encoding")
    encodedVector = golayCode.encode_vector(vector)
    print(encodedVector)
    receivedVector = Vector(channel.send_binary_info(encodedVector.elements), encodedVector.essentialElemLen)
    print("Received from channel vector")
    print(receivedVector)
    print("Kanalo iskraipymu skaicius:")
    print(get_vector_errors(encodedVector, receivedVector))
    print("Dekoduotas vektorius:")
    print(golayCode.decode_vector(receivedVector))
    """matrixB = generate_matrix_b()
    print("Rows:")
    print(len(matrixB.rows))
    print(matrixB)
    vector = Vector([0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0], 12)
    channel = CommChannel(0.2)
    print("Vector before being sent")
    print(vector)
    vector.elements = channel.send_binary_info(vector.elements)
    print("Vector after being sent")
    print(vector)
    firstVector = Vector([0, 0, 1, 0], 4)
    secondVector = Vector([1, 0, 1, 1], 4)
    print("First vector:")
    print(firstVector)
    print("Second vector:")
    print(secondVector)
    print("Added vector:")
    print(vector_addition(firstVector, secondVector))
    multVector = Vector([0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0], 12)
    print("Mult vector result:")
    print(vector_matrix_multiplication(multVector, generate_matrix_g()))
    input("Press any key to continue...")"""


if __name__ == "__main__":
    main()
