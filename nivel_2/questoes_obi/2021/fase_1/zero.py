quantidadeDeNumeros = int(input())

listaDeNumeros = []

while int(quantidadeDeNumeros) > 0:
  numero = int(input())

  if(numero == 0):
    listaDeNumeros.pop()
  else:
    listaDeNumeros.append(numero)


  quantidadeDeNumeros = quantidadeDeNumeros - 1

print(sum(listaDeNumeros))


## Passa 100/100