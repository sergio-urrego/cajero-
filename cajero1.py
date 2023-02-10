#hacer un cajero con las siguientes indicacion 
#1valor solicitado 
#2denominacion-10-20-50-100
#3inventario
#4cancelar transaccioon 


#denominacion que maneja el cajero y cantidad de cada una 
from os import system
billetes_100=1
billetes_50=1
billetes_20=1
billetes_10=1


#valor total de cuanta plata hay en el cajero 
inventario=(billetes_100*100)+(billetes_50*50)+(billetes_20*20)+(billetes_10*10)

#if inventario >=10:
#valida si hay plata en el cajero 
while inventario >=10:  
    system("cls")
    #valor a retirar
    print(inventario)
    valor_retirar=int(input("Digite el valor a retirar "))
    #while por si la cantidad del valor a retirar no es exacta
    opcion=int(input("desea continuar con la transacion? \n si=1 \n no=2 \n -:"))
    if opcion==1:
        while valor_retirar % 10 != 0:
            print("Digite el un valor exacto ejem: 10-50-100-70")
            valor_retirar=int(input(":"))

        #rectifica si alcanza la plata del cajero para pagar 
        if valor_retirar <=inventario:
            #hace un desglose del valor en billetes 
            #falta verificcar si no hay billetes de 100 pasar a el otro y asi sucesivamente 
            while  valor_retirar >=100 and billetes_100 > 0:
                queda=valor_retirar//100
                billetes_100=billetes_100-queda
                print(f"doy {queda} de 100")
                inventario=inventario-(queda*100)
                valor_retirar=valor_retirar % 100 
            while  valor_retirar>=50 and billetes_50 > 0:
                queda=valor_retirar//50
                billetes_50=billetes_50-queda
                print(f"doy {queda} de 50")
                inventario=inventario-(queda*50)
                valor_retirar=valor_retirar % 50 
            while  valor_retirar >=20 and billetes_20 > 0:
                queda=valor_retirar//20
                billetes_20=billetes_20-queda
                print(f"doy {queda} de 20")
                inventario=inventario-(queda*20)
                valor_retirar=valor_retirar % 20 
            while  valor_retirar >=10 and billetes_10 > 0:
                queda=valor_retirar//10
                billetes_10=billetes_10-queda
                print(f"doy {queda} de 10")
                inventario=inventario-(queda*10)
                valor_retirar=valor_retirar % 10    
        else:
            print("lo sentimos no contamos con la cantidad de dinero requerida:(° )")
    elif opcion==2:
        system("cls")
print("cajero esta fuera de servicio :( ")     