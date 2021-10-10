from golay_execution import GolayExecution
from golay_window import GolayWindow
from golay_code import GolayCode
from comm_channel import CommChannel

# Iskraipymo tikimybe yra 0.0 programos pradzioje.
g_channel = CommChannel(0.0)
# Golejaus kodo klases incializavimas.
g_golayCode = GolayCode()


def main():
    # Inicijuojama Golejaus kodo vykdymo klase.
    golayExecutor = GolayExecution(g_channel, g_golayCode)

    # Golejaus kodo lango klasei perduodama Golejaus kodo vykdymo klase.
    window = GolayWindow(golayExecutor)

    # Inicijuojamas pradinio lango sukurimas.
    window.create_probability_window()


if __name__ == "__main__":
    main()
