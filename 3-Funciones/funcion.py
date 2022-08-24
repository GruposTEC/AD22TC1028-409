def menor(num1, num2, num3):
    """_Metodo que calula el menor de tres numeros

    Args:
        num1 (int): EL primer numero
        num2 (int): El segundo numero
        num3 (int): _El tercer numero

    Returns:
        int: el menor de los tres
    """
    if(num1 <= num2):
        menorn = num1
    else:
        menorn = num2
    if(num3 < menorn):
        menorn = num3
    return menorn


numero = menor(3, -1, 8)
print(numero)
print(menor(3, -1, 8))
menorn = 10
help(menor)
