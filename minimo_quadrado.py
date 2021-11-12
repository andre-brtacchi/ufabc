"""
**********************************************************************************************************************


                          André Rodrigues Bertacchi, Universidade Federal do ABC

                          10 oct. 2021


                          mínimo quadrado


                          recebe resultados de teste experimental e fornece os parâmetros a e b para confecção de gráfico linear

"""


import math
n=int(input("Digite a quantidade de valores que serão analisados: "))

eixo_x=[]
eixo_y=[]
erro_y=[]
for i in range(n):
    temp=float(input("Digite o valor "+str(i+1)+" do eixo x: "))
    eixo_x.append(temp)
    print(eixo_x[i])
for i in range(n):  
    temp=float(input("Digite o valor "+str(i+1)+"  do eixo y: "))
    eixo_y.append(temp)
    print(eixo_y[i])
for i in range(n):
    temp=float(input("Digite o valor "+str(i+1)+"  do erro de y: "))
    erro_y.append(temp)
    print(erro_y[i])

sigma=float(0)
for i in range(n):
  sigma=sigma+(1/(erro_y[i]**2))

xy=float(0)
for i in range(n):
  xy=xy+((eixo_x[i]*eixo_y[i])/((erro_y[i])**2))
xy=(1/sigma)*xy

x_double=float(0)
for i in range(n):
  x_double=x_double+((eixo_x[i]*eixo_x[i])/((erro_y[i])**2))
x_double=(1/sigma)*x_double

x=float(0)
for i in range(n):
  x=x+((eixo_x[i])/((erro_y[i])**2))
x=(1/sigma)*x

y=float(0)
for i in range(n):
  y=y+((eixo_y[i])/((erro_y[i])**2))
y=(1/sigma)*y


a=float(x*y-xy)/((x**2)-(x_double))

b=y-a*x

delta_a=(1/sigma)/((x**2)-(x_double))
delta_a=(delta_a)**(1/2)

delta_b=(x_double/sigma)/((x**2)-(x_double))
delta_b=(delta_b)**(1/2)

matriz=[]

for i in range(n):
  line=[]
  matriz.append(line)
  for j in range(3):
    if j==0:
      matriz[i].append(eixo_x[i])
    elif j==1:
      matriz[i].append(eixo_y[i])
    else:
      matriz[i].append(erro_y[i])

for i in range(n):
  for j in range(3):
    print(str(matriz[i][j]),end=" | ")
  print("")
print(eixo_x)
minimo_quadrado=float(0)
for i in range(n):
  minimo_quadrado=minimo_quadrado+((eixo_y[i]-(a*eixo_x[i]+b))/sigma)**2

print("sigma dois: "+str(sigma))
print("x: "+str(x))
print("x^2: "+str(x_double))
print("xy: "+str(xy))
print("y: "+str(y))
print("a: "+str(a))
print("b: "+str(b))
print("mínimo quadrado: "+str(minimo_quadrado))