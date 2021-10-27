def es_primo(numero: int) -> bool:
    contador = 0
    for i in range (1, numero+1):
        if i == 1 or i == numero:
            continue 
        if numero % i == 0:
            contador += 1
            break
    if contador == 0:
        return True 
    else:
        return False

def run():
    numero = int(input("Ingrese un número: "))
    if es_primo(numero):
        print("El número es Primo")
    else:
        print("El número No es primo")

if __name__ == '__main__':
    run()