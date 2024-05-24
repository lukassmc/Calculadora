def suma(a, b)-> int:
      """lo que hace la funcion es sumar numero A, y numero B

      Args:
         a (_type_): primer numero
          b (_type_): segundo numero

      """
      resultado= a + b
      return resultado
  
def resta(a, b)-> int:
    """Lo que hace esta funcion es restar A y

    Args:
        a (int): primer numero
        b (int): Segundo numero
        
    """
    resultado= a - b
    
    return resultado

def multiplicacion(a, b)-> int:
    """Lo que hace esta funcion es multiplicar A y B

    Args:
        a (int): Primer numero
        b (int): Segundo numero

 
    """
    resultado= a * b
    return resultado

def division(a, b)-> float:
    """Divide numero A entre numero B

    Args:
        a (int): Primer numero
        b (int): Segundo numero

  
    """
    resultado= a / b

    return resultado


def factorial (a: int)-> int:
    """Da como resultado al factorial de el numero ingresado

    Args:
        a (int): numero del que se pide factorial

    """
    numero= a
    resultado= 1
    
    while numero > 0:
       resultado *= numero
       numero -= 1
        
    return resultado

