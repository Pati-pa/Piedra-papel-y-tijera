import random
print("-------------------------------------------")
print("----------- Piedra, Papel y tijera ----------------")
print("-------------------------------------------")

aleatorio = random.randrange(0,3)
elijePc = ""
print ("1. piedra")
print("2. papel")
print("3. tijera")
opcion = int(input("Elige tu opcion "))
    
if opcion == 1 :
        elijepersona = "Piedra"
elif opcion == 2:
        elijepersona = "Papel"
elif opcion == 3 :
        elijepersona = "Tijera"
print("Elejiste:", elijepersona)
    
if aleatorio == 0 :
        elijePc = "Piedra"
elif aleatorio == 1:
        elijePc = "Papel"
elif aleatorio == 2 :
        elijePc = "Tijera"
print("La maquina elijio:", elijePc)
print("......")
   
if elijePc == "Piedra" and elijepersona == "Papel" :
        print("Ganaste,papel envuelve a piedra ")
elif elijePc == "Papel" and elijepersona== "Tijera" :
        print("Ganaste, Tijera corta a papel ")
elif elijePc == "Tijera" and elijepersona== "Piedra" :
        print("Ganaste, Piedra machaca a Tijera ")
if elijePc == "Papel" and elijepersona== "Piedra" :
        print("Perdiste,papel envuelve a piedra ")
elif elijePc == "Tijera" and elijepersona== "Papel" :
        print("Perdiste, Tijera corta a papel ")
elif elijePc == "Piedra" and elijepersona== "Tijera" :
        print("Perdiste, Piedra machaca a Tijera ")
elif elijePc==elijepersona :
        print("empate")


