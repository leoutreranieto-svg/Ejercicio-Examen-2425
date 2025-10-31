from typing import NamedTuple
from datetime import datetime
import csv

Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)])

CarreraFP=NamedTuple("CarreraFP",[
        ("fecha_hora",datetime), 
        ("circuito",str),                    
        ("pais",str), 
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado
        ("tiempo",float), 
        ("podio", list[Piloto])])


def lee_carreras(filename: str) -> list[CarreraFP]:
    with open (filename, "r", encoding="utf-8") as f:
        lista = []
        lector = csv.reader(f)
        next(lector)
        for fecha_hora,circuito,pais,seco,tiempo,piloto_1,escuderia_1,piloto_2,escuderia_2,piloto_3,escuderia_3 in lector:
            fecha_hora2 = datetime(fecha_hora,"%Y-%m-%d H:M")
            circuito = str(circuito)
            pais = str(pais)
            seco = seco == "1"
            tiempo = float(tiempo)
            podio = [(piloto_1,escuderia_1),(piloto_2,escuderia_2)(piloto_3,escuderia_3)]
            carreraFP=CarreraFP(fecha_hora2,circuito,pais,seco,tiempo,podio)
            lista.append(carreraFP)
        return lista