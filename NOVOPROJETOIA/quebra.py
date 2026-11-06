numero = int(input("Digite um numero: "))
print(10 / numero)
#ValueError - tipo de variavel
#ZeroDivisionError - inseri 0 
try: 
    numero = int(input("Digite um numero: "))
    print(10 / numero)
except ValueError: 
    print("Isso não é um numero válido")
except ZeroDivisionError:
    print("Não se divide por 0")