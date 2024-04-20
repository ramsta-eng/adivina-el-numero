import random as r
import os
clear = lambda: os.system('cls')
clear()

print("Bienvenido al Adivino, Juego donde deberas adivinar un numero del 1-10 con un maximo de 5 intentos!")
eleccion= "s"

def loop_juego():
    while True:
        ranNum= r.randrange(1, 10, 1)

        # print(ranNum)
        
        numIntento = 1
        puntaje= 100    
        
        print("Empezamos!")
        
        while True:
            intento=int(input(": "))
                        
            if intento == ranNum and numIntento != 6:
    
                if puntaje <= 30:
                    clear()
                    print(f"\nWin, ganaste en {numIntento} Intentos, que son {puntaje} pts!. La proxima sera mejor!")
                    break
                
                elif puntaje > 30 and puntaje <= 60:
                    clear()
                    print(f"\nWin, ganaste en {numIntento} Intentos, que son {puntaje} pts!. Buen puntaje!")
                    break
                
                elif puntaje > 60 and puntaje <=90:
                    clear()
                    print(f"\nWin, ganaste en {numIntento} Intentos, que son {puntaje} pts!. Wow lo hiciste increible!")
                    break
                
                else:
                    clear()
                    print(f"\nWin, ganaste en {numIntento} Intentos, que son {puntaje} pts!. Puntaje perfecto!")
                    break

            elif numIntento == 5:
                clear()
                print("\nno quedan intentos, perdiste.")
                break 
            
            else:
                clear()
                print("\nIncorrecto, te quedan " + str(5-numIntento) + " Intentos.")
                puntaje= 100    
                puntaje = puntaje - numIntento*22
                numIntento = numIntento + 1
                continue

        eleccion =str(input("\nDesea volver a jugar?(s/n): "))
        
        if eleccion == "s":
            continue
        
        elif eleccion == "n":
            print("Gracia por jugar!")
            break
        
        else:
            print("seleccion no valida, cerrando automaticamente")
            break

loop_juego()