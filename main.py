from golay_code import *
from vector import Vector
from comm_channel import *
from operations import vector_addition


def main():
    matrixB = generate_matrix_h()
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


if __name__ == "__main__":
    main()
