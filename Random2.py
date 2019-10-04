# Vytvoril Andrej Ambroz z V1C
while True:
    print("INFO: Zadejte prvni cislo a odeslete ho entrem,")
    print("      pak napiste druhe cislo a odeslete ho taky entrem,")
    print("      pote vyberte operaci odeslanim cisla, ktere je u dane")
    print("      operace, program nasledne vypise vysledek.")
    print("")

    cisloOne = int(input("Zadejte prvni cislo: "))
    cisloTwo = int(input("Zadejte druhe cislo: "))
    typVypoctu = str(input("Zadejte zpusob vypoctu Nasobeni(N), Deleni(D), Scitani(S), Odecitani(O): "))
    print("")
    
    if typVypoctu == "N" or typVypoctu == "n" or typVypoctu == "Nasobeni" or typVypoctu == "nasobeni": 
        print("Vysledek po vynasobeni cisel:", cisloOne*cisloTwo)
    if typVypoctu == "D" or typVypoctu == "d" or typVypoctu == "Deleni" or typVypoctu == "deleni": 
        print("Vysledek po vydeleni cisel:", cisloOne/cisloTwo)
    if typVypoctu == "S" or typVypoctu == "s" or typVypoctu == "Scitani" or typVypoctu == "scitani": 
        print("Vysledek po secteni cisel:", cisloOne+cisloTwo)
    if typVypoctu == "O" or typVypoctu == "o" or typVypoctu == "Odcitani" or typVypoctu == "odcitani":
        print("Vysledek po odecteni cisel:", cisloOne*cisloTwo)

    print("")
    print("")
    
    res = input("Prejete si opakovat program A/N: ")
    if res == "N" or res == "n": break    
    
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")