from os import system

def pausar():
    system("pause")

def limpiar_terminal():
    system("cls")
    
def menu()-> str:
    limpiar_terminal()
    print("     Menu de opciones")
    print("1- Saludar")
    print("2- Brindar")
    print("3- Despedir")
    print("4- Salir")
    
    return input("Ingrese una opcion")
    
    
    
def saludar():
    print("Hola")

def brindar():
    print("Chin chin")

def despedir():
    print("Adios")
    
bandera_saludo= False
bandera_brindis= False 
bandera_adios= False

while True:
    
    match menu():
         case "1":
             saludar()
             bandera_saludo= True
         case "2":
             if bandera_saludo:
                 brindar()
                 bandera_brindis= True
             else:
                 print("Antes, deberiamos saludarnos")
         case "3":
             if bandera_brindis:
                 despedir()
                 bandera_adios= True
                 bandera_saludo= False
                 bandera_brindis= False  
             elif bandera_saludo == False:
                 print("Antes de despedirnos deberiamos saludarnos..")
                
             else:
                 print("Antes de despedirnos deberiamos brindar..")
                
                 
        
            
         case "4":
             if bandera_adios:
                 break
             else:
                 print("Antes de irte, deberíamos saludarnos.")
     # if opcion == 4:
     #     break
     #input("Enter para continuar")
    pausar()
    
print("fin del programa")