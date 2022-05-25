valorDaSoma = int(input())

valorInicio = int(input())
valorFinal = int(input())

quantidadeDeNumeros = 0

while valorInicio <= valorFinal:
  totalDigitos = 0
  for digito in str(valorInicio):
    totalDigitos += int(digito)
  
  if(totalDigitos == valorDaSoma): quantidadeDeNumeros += 1

  totalDigitos = 0
  valorInicio += 1


print(quantidadeDeNumeros)