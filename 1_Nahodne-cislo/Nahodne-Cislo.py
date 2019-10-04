# Vytvoril Andrej Ambroz z V1C

import random
spodniHranice = int(input("Vyberte spodni hranici nahodneho cisla: "))
horniHranice = int(input("Vyberte horni hranici nahodneho cisla: "))

print("")
print("Nahodne cislo od", spodniHranice, "do", horniHranice, "=", random.randrange(spodniHranice, horniHranice))
