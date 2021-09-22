from golay_code import *
from vector import Vector
from comm_channel import *


def main():
    matrixB = generate_matrix_h()
    print(matrixB)
    vector = Vector([0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0])
    channel = CommChannel(0.2)
    print("Vector before being sent")
    print(vector)
    vector.elements = channel.send_binary_info(vector.elements)
    print("Vector after being sent")
    print(vector)


if __name__ == "__main__":
    main()
