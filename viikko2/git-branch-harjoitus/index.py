# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
<<<<<<< HEAD
print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")
=======
print(f"{summa(x, y)}") # kommentit poikkeen
print(f"{erotus(x, y)}")
>>>>>>> main

logger("lopetetaan")
print("goodbye!")
