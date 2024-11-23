import sympy as sp

x, y = sp.symbols('x y')

def calcular_derivadas(J_M, A_N):
    F_d1 = sp.diff(J_M, y)
    F_d2 = sp.diff(A_N, x)
    return F_d1, F_d2

def calcular_integrales(J_M, A_N):
    J_ix = sp.integrate(J_M, x)
    J_iy = sp.integrate(A_N, y)
    return J_ix, J_iy

print('Bienvenido a la calculadora, Ingrese los datos: \n')
J_M = input('Ingrese el valor de M: ')
A_N = input('Ingrese el valor de N: ')

F_d1, F_d2 = calcular_derivadas(J_M, A_N)

if F_d1 == F_d2:
    print(f'La ecuación diferencial {J_M}dx + {A_N}dy = 0')
    print('¡¡SI ES EXACTA!!')
    print(f'Derivadas = \n{F_d1}\n{F_d2}')
    
    J_ix, J_iy = calcular_integrales(J_M, A_N)
    
    print('El valor de las integrales son:')
    print('Integral respecto a x:', sp.expand(J_ix))
    print('Integral respecto a y:', sp.expand(J_iy))
else:
    print('¡¡LA ECUACIÓN DIFERENCIAL NO ES EXACTA!!')
    print(f'Derivadas = \n{F_d1}\n{F_d2}')



