import os 
from colorama import Fore, Style

def limpiar_Pantalla()-> None:
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_Titulo(titulo : str) -> None:
    """Imprime un título en la consola con formato."""
    print(f"{Fore.CYAN}{Style.BRIGHT}==={titulo.upper()}=== {Style.RESET_ALL}")

def imprimir_Error(mensaje : str) -> None:
    """Imprime un mensaje de error en la consola con formato."""
    print(f"{Fore.RED}{Style.BRIGHT}ERROR: {mensaje}{Style.RESET_ALL}")

def imprimir_Exito(mensaje: str)-> None:
    """Imprime un mensaje de éxito en la consola con formato."""
    print(f"{Fore.GREEN}{Style.BRIGHT}ÉXITO: {mensaje}{Style.RESET_ALL}")

def validar_Input_float(mensaje : float) -> float:   
    """Valida que la entrada del usuario sea un número flotante."""
    while True:
        entrada = input(f"{Fore.YELLOW}{mensaje}: {Style.RESET_ALL}").strip()
        try:
            valor = float(entrada)
            if valor >= 0:
                return valor
            imprimir_Error("Por favor, ingrese un número mayor o igual a cero.")
        except ValueError:
            imprimir_Error("Por favor, ingrese un número válido.")

def validar_Input_str(mensaje : str) -> str:
    """Valida que la entrada del usuario sea una cadena de texto."""
    while True:
        entrada = input(f"{Fore.YELLOW}{mensaje}: {Style.RESET_ALL}").strip()
        if entrada:
            return entrada
        else:
            imprimir_Error("Por favor, ingrese una cadena de texto válida.")

def validar_Input_int(mensaje : str) -> int:

    """Valida que la entrada del usuario sea un número entero."""
    while True:
        entrada = input(f"{Fore.YELLOW}{mensaje}: {Style.RESET_ALL}").strip()
        try:
            valor = int(entrada)
            if valor >= 0:
                return valor
            imprimir_Error("Por favor, ingrese un número entero mayor o igual a cero.")
        except ValueError:
            imprimir_Error("Por favor, ingrese un número entero válido.")

