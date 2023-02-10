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

def operacion (denominacion,cant_bille,valor_re,valor_inv):
    while valor_re >=denominacion and cant_bille > 0:
        cant=valor_re//denominacion
        cant_bille=cant_bille-cant
        print(f"doy {cant} de {denominacion}")
        valor_inv=valor_inv-(cant*denominacion)
        valor_re=valor_re % denominacion
    return(valor_re,cant_bille,valor_inv)
#valor total de cuanta plata hay en el cajero 
inventario=(billetes_100*100)+(billetes_50*50)+(billetes_20*20)+(billetes_10*10)
 
while inventario >=10:  
    system("cls")
    print(inventario)
    valor_retirar=int(input("Digite el valor a retirar "))
    opcion=int(input("desea continuar con la transacion? \n si=1 \n no=2\n"))
    if opcion==1:
        while valor_retirar % 10 != 0:
            valor_retirar=int(input("Digite el un valor exacto ejem: 10-50-100-70\n:"))
        if valor_retirar <=inventario:
            #hace un desglose del valor en billetes 
            #falta verificcar si no hay billetes de 100 pasar a el otro y asi sucesivamente  
            (valor_retirar,billetes_100,inventario)=operacion(100,billetes_100,valor_retirar,inventario)
            (valor_retirar,billetes_50,inventario)=operacion(50,billetes_50,valor_retirar,inventario)
            (valor_retirar,billetes_20,inventario)=operacion(20,billetes_20,valor_retirar,inventario)
            (valor_retirar,billetes_10,inventario)=operacion(10,billetes_10,valor_retirar,inventario) 
            print("transacion terminada ")
            input("digite enter para continuar") 
        else:
            print("lo sentimos no contamos con la cantidad de dinero requerida:(° )")
    elif opcion==2:
        system("cls")
print("cajero esta fuera de servicio :( ")     