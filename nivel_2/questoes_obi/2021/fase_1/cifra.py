
alfabeto = list(map(chr, range(97, 123)))

def ehVogal(letra):
  vogais = ['a', 'e', 'i', 'o', 'u',]

  if letra in vogais: 
    return True
  return False

def proximaConsoante(consoante: str):
  if consoante == 'z': return 'z'
  soConsoantes = list(filter(lambda letra: not ehVogal(letra), alfabeto))
  return soConsoantes[soConsoantes.index(consoante) + 1]

def vogalMaisProxima(consoante: str):
  # o index são fixos
    # "a" tem index 0
    # "e" tem index 4
    # "i" tem index 8
    # "o" tem index 14
    # "u" tem index 20

  listaDeIndexVogais = [0, 4, 8, 14, 20]
  
  indexConsoante = alfabeto.index(consoante)

  menorDistancia = 26

  for vogalIndex in listaDeIndexVogais:
    distanciaDesteIndex = (indexConsoante - vogalIndex)
    if(abs(distanciaDesteIndex) < menorDistancia): menorDistancia = distanciaDesteIndex

  return alfabeto[indexConsoante - menorDistancia]

def codificaLetra(letra):
  if(not ehVogal(letra)): 
    return letra+vogalMaisProxima(letra)+proximaConsoante(letra)
  else:
    return letra


palavra = input()
palavraCodificada = "".join(list(map(lambda letra: codificaLetra(letra), palavra)))

print(palavraCodificada)
  
