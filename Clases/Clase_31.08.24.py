

# def hoy():
#     print('Bienvenido a la clase')
# hoy()
# def Sumar(num1, num2):
#     global r #Es para declarar globalmente!!!!
#     r = num1 + num2
#     return r #Donde va a almacenar !!!!

# a = float(input('Ingrese un número: '))
# b = float(input('Ingrese un número: '))

# laura = Sumar(a, b) #Se guarda en un valor!!!!
# print(Sumar(a, b))




def perimetro_triangulo(cateto1:float ,cateto2:float)->float: #Sirve para declarar primero como float
    hipotenusa = calcular_hip(cateto1, cateto2)
   
    return cateto1 + cateto2 + hipotenusa #Aquí se guarda 

def calcular_hip(cateto1:float ,cateto2:float)->float:
    suma_cuadrados = (pow(cateto1, 2)) + (cateto2**2)
    hipotenusa = pow(suma_cuadrados, 0.5)

    return hipotenusa

cadena_cat_1 = input("Indique la longitud del primer cateto: ")
cadena_cat_2 = input("Indique la longitud del segundo cateto: ")

cat_1 = float(cadena_cat_1)
cat_2 = float(cadena_cat_2)

perimetro = perimetro_triangulo(cat_1, cat_2)
print("El perímetro de un triángulo rectángulo que tenga catetos de longitud", cat_1, "y", cat_2, "es", round(perimetro, 3))














