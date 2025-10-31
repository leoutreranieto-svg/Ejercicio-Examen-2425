from motosFP import *


def test_lee_carreras(filename: str):
    print(f"Número de carreras leídas:{len(filename)}")
    print("Las dos primeras carreras son:")
    print(lee_carreras[:2])
    print("Las dos últimas carreras son:")
    print(lee_carreras[-2:])

if __name__ == "__main__":
    datos = lee_carreras("data\mundial_motofp.csv")
    print(test_lee_carreras(datos))