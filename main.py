from golay_code import *
from vector import Vector
from comm_channel import *
from operations import vector_addition, vector_matrix_multiplication, check_vector_len


def main():

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
    print(vector_matrix_multiplication(multVector, generate_matrix_g()))"""


if __name__ == "__main__":
    main()
