"""

           André Rodrigues Bertacchi, Universidade Federal do ABC

           Calculadora de média e desvio-padrão

           Recebe como input uma série de valores e calcula a média e o desvio-padrão

"""


import math
n=int(0)
vetor=[]
valor=float(input("Digite um valor diferente de zero: "))
while(valor!=0):
  vetor.append(valor)
  n+=1
  valor=float(input("Digite um valor diferente de zero: "))

for i in range(len(vetor)):
  print("valor "+str(i)+" "+str(vetor[i]))

print("")
media=float(0)
for i in range(len(vetor)):
  media=media+vetor[i]

media=media/n

desvio=float(0)
for i in range(len(vetor)):
  desvio=desvio+(media-vetor[i])**2

desvio=desvio/(n*(n-1))
desvio=math.sqrt(desvio)

print("Média: "+str(media)+", desvio-padrão: "+str(desvio))
