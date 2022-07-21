# Programa que pida un numero al usuario, y que imprima dos numeros, 'root' y 
# 'pwr', con 1 < pwr < 6 y que se cumpla que root**pwr sea igual al numero
# ingresado por el usuario

number = int(input("Ingrese un numero mayor a 2: "))

root = 1
pwr = 0

while(root < 1000 and pwr == 0):
    root +=1
    for i in range(1, 6):
        if(root**i == number):
            pwr = i

if root**pwr == number:
    print(f"El numero es igua a {root}^{pwr}")
else:
    print("El numero ingresado no se puede representar como n^x")

    
