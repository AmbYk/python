# Register / login

print("Informace: Program je urcen pro registraci a nasledne prihlaseni")
print("           k fungovani vyuziva zapisu do .txt souboru.")
print("")
print("Planovana funkce: Po prihlaseni moznost vytvareni .txt souboru s")
print("                  obsahem, ktery muze cist pouze prihlaseny uzivatel.")
print("")
print("")
print("              Verze 1.0 - created by Andrej Ambroz.")
print("")
print("")

typ = input("[INFO] Vyberte typ: Registrace (R) / Login (L): ")

if typ == "R" or typ == "Registrace" or typ == "r" or typ == "registrace":
    rjmeno = input("Vase nove jmeno: ")
    rheslo1 = input("Vase nove heslo: ")
    rheslo2 = input("Zopakujte heslo: ")
    
    if rheslo1 == rheslo2:
        print("")
        print("[INFO] Registrace byla uspesna.")
        print("")
        f= open(rjmeno + ".txt","w+")
        f.write(rheslo1)
        f.close()
        
        typ2 = input("Chcete se nyni prihlasit? (A/N): ")
        if typ2 == "N" or typ2 == "n":
            input("")
        
    if rheslo1 != rheslo2:
        print("")
        print("[CHYBA] Hesla se neshoduji, registrace neuspesna.")
        print("")
        
        typ3 = input("Chcete zopakovat registraci? (A/N): ")
        if typ3 == "A" or typ3 == "a":
            print("")
            print("[INFO] Zavrete program a spuste ho znovu.")
            print("")
            input("")
            
        if typ3 == "N" or typ3 == "n":
            input("")
        
# Login now
if typ == "L" or typ == "Login" or typ == "l" or typ == "login" or typ2 == "A" or typ2 == "a":
    ljmeno = input("Vase jmeno: ")
    lheslo = input("Vase heslo: ")
    
    f= open(ljmeno + ".txt","r")
    if f.mode == "r":
        contents = f.read()
        if contents == lheslo:
            print("")
            print("[INFO] Prihlaseni bylo uspesne.")
            print("Nyni jste prihlasen jako " + ljmeno)
            input("")
        
        if contents != lheslo:
            print("")
            print("[CHYBA] Heslo se neshoduje, prihlaseni neuspesne.")
            print("")
            
            typ4 = input("Chcete zopakovat prihlaseni? (A/N): ")
            if typ4 == "A" or typ4 == "a":
                print("")
                print("[INFO] Zavrete program a spuste ho znovu.")
                print("")
                input("")
                
            if typ4 == "N" or typ4 == "n":
                input("")            