from os import system
from operaciones import *


def pausar():
    system("pause")

def limpiar_terminal():
    system("cls")
     
    
def menu_calculadora(valor_a, valor_b)-> str:
    limpiar_terminal()
    print("     Calculadora")
    print(f"a- Primer operando. (A={valor_a})")
    print(f"b- Segundo operando. (B={valor_b})")
    print("c- Elija su operación")
    print("d- Resultado")
    print("e- Salir")
    
    return input("Ingrese una opcion  ").lower()


def es_numero(entrada):
    flag_es_numero= False
    
    try:
        
        int(entrada) 
        flag_es_numero= True
    
    except ValueError:
        
        flag_es_numero= False
        
    return flag_es_numero



def obtener_numero(mensaje):
    
    
    
    while True:
        
        entrada = input(mensaje)
        if es_numero(entrada):
            
            return int(entrada)  
        else:
            print("Entrada inválida. Por favor, ingrese un número.")






def menu_operaciones(valor_a, valor_b)-> str:
    limpiar_terminal()
    print("     Operaciones")
    print(f"1- Suma. ({valor_a} + {valor_b}) ")
    print(f"2- Resta. ({valor_a} - {valor_b})")
    print(f"3- Multiplicacion. ({valor_a} * {valor_b})")
    print(f"4- Division. ({valor_a} / {valor_b})")
    print(f"5- Factorial. ({valor_a}!), ({valor_b}!)")
    
    return input("Ingrese una opcion  ")

def confirmar_salida(mensaje: str)-> bool:
    respuesta= input(mensaje).lower()
    
    return respuesta == "si"

resultado= None
flag_primer_operando= False
flag_segundo_operadno= False
flag_operacion= False
flag_factorial= False
primer_numero= "x"
segundo_numero= "x"
while True:
    
    
    match menu_calculadora(primer_numero, segundo_numero):
        case "a":
            
                primer_numero= obtener_numero("Ingrese el primer operando: ")
                
                flag_primer_operando= True
        case "b":
            if flag_primer_operando:
                segundo_numero= obtener_numero("Ingrese su segundo operando: ")
                
                flag_segundo_operadno= True
            else:
                print("Antes de ingresar el segundo operando, deberías empezar por el primero..")
        case "c":
            if flag_segundo_operadno:
                
                match menu_operaciones(primer_numero, segundo_numero):
                    case "1":
                        resultado= suma(primer_numero, segundo_numero)
                    case "2":
                        resultado= resta(primer_numero, segundo_numero)
                    case "3":
                        resultado= multiplicacion(primer_numero, segundo_numero)
                    case "4":
                        resultado= division(primer_numero, segundo_numero)
                    case "5":
                        if primer_numero != "x" and segundo_numero != "x":
                            resultado1= factorial(primer_numero)
                            resultado2= factorial(segundo_numero)
                            flag_factorial= True
                flag_operacion = True
                continue
            elif flag_segundo_operadno == False:
                print("Antes de elegir una operación, deberías ingresar ambos numeros...")
            
        case "d":
            if flag_factorial:
                print(f"El resultado de su operacion es: Factorial de A es {resultado1}, y el de B es {resultado2}")
                flag_primer_operando= False
                resultado= None
                flag_segundo_operadno= False
                flag_operacion= False
                flag_factorial= False
            elif flag_operacion:
                    print(f"El resultado de su operación es: {resultado}")
                    flag_primer_operando= False
                    resultado= None
                    flag_segundo_operadno= False
                    flag_operacion= False
                    
            elif flag_segundo_operadno == False:
                    print("Antes de pedir el resultado, deberías ingresar ambos numeros...")
            else:
                    print("Para tener el resultado, debes elegir la operación previamente...")
        case "e":
            if confirmar_salida("Desea salir?\n "):
                break
            else:
                continue
            
    pausar()       
            
print("Fin del programa")   



## <>\
