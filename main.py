from golay_code import generate_matrix_b
from vector import Vector
from comm_channel import *


def main():
    generate_matrix_b()
    vector = Vector([0, 1, 1, 1, 0])
    channel = CommChannel(0.1)
    print("Vector before being sent")
    print(vector)
    vector.elements = channel.send_binary_info(vector.elements)
    print("Vector after being sent")
    print(vector)


if __name__ == "__main__":
    main()
