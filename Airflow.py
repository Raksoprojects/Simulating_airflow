import numpy as np
import scipy.linalg
import re


Qa = 200
ca = 2
Qb = 300
cb= 2
E12 = 25
E23 = 50
E35 = 25
E34 = 50
Qc = 150
Qd = 350
Wg = 2500
Ws = 1500

#Podpunkt 1
A = np.array([[E12+Qa, -E12, 0 , 0, 0],[-E12-Qa, E23+E12+Qa+Qb, -E23, 0, 0], [0, -E23-Qa-Qb, E35+E23+E34+Qa+Qb, -E34, -E35], [0, 0, -E34-Qc, E34+Qc, 0], [0, 0, -E35-Qd, 0, E35+Qd]],dtype=float)
#zmienne = np.array([c1,c2,c3,c4,c5])
B = np.array([Ws+Qa*ca,Qb*cb,0,0,Wg])

print('1. Macierz A: ')
print(F'{A}\n')
print('Macierz B: ')
print(B)

p,l,u = scipy.linalg.lu(A) 

linv = np.linalg.inv(l)
d = np.dot(linv,B)

uinv = np.linalg.inv(u)
x = np.dot(uinv,d)
print(f'\n2. Wektor stężeń CO: {x}\n')

Wg = 1200
Ws = 800
B = np.array([Ws+Qa*ca,Qb*cb,0,0,Wg])

d = np.dot(linv,B)
x = np.dot(uinv,d)
print(f'3. Wektor stężeń CO po ograniczeniach: {x}\n')

# Odwracanie macierzy A
A1 = np.array([1,0,0,0,0])
A2 = np.array([0,1,0,0,0])
A3 = np.array([0,0,1,0,0])
A4 = np.array([0,0,0,1,0])
A5 = np.array([0,0,0,0,1])

d1 = np.dot(linv, A1)
d2 = np.dot(linv, A2)
d3 = np.dot(linv, A3)
d4 = np.dot(linv, A4)
d5 = np.dot(linv, A5)

x1 = np.dot(uinv, d1.T)
x2 = np.dot(uinv, d2.T)
x3 = np.dot(uinv, d3.T)
x4 = np.dot(uinv, d4.T)
x5 = np.dot(uinv, d5.T)

Ainv = np.array([x1,x2,x3,x4,x5]).T

np.set_printoptions(precision=6)
np.set_printoptions(suppress=True)
print('4. Odwrotność macierzy A z użyciem metody LU: ')
print(Ainv)

print(f'\n5. Procentowy udział CO z grilla, papierosów i ulicy w pokoju dla dzieci:')
grill = Ainv[3,4]*Wg*100/x[3]
palacz = Ainv[3,0]*Ws*100/x[3]
ulica = (Ainv[3,0]*Qa*ca + Ainv[3,1]*Qb*cb) * 100/x[3]


print(f'Grill: {grill:.2f}%\nPalacze: {palacz:.2f}%\nUlica: {ulica:.2f}%')
