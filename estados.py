import copy
import random
import math
class Estado:
    def estados2(self,i,j):
        # Copiando a matriz
        matriz1 = copy.deepcopy(self.matriz)
        matriz2 = copy.deepcopy(self.matriz)
        # Movimento Horizontal
        # Guardando a posição vazia
        aux1 = matriz1[i][j]
        if j==0:
            matriz1[i][j] = matriz1[i][j+1]
            matriz1[i][j+1] = aux1
        else:
            matriz1[i][j] = matriz1[i][j-1]
            matriz1[i][j-1] = aux1
        # Movimento Vertical
        # Guardando a posição vazia
        aux2 = matriz2[i][j]
        if i==0:
            matriz2[i][j] = matriz2[i+1][j]
            matriz2[i+1][j] = aux2
        else:
            matriz2[i][j] = matriz2[i-1][j]
            matriz2[i-1][j] = aux2
        # 0 ou 1
        vetor = [matriz1,matriz2]
        # Embaralhando a ordem do vetor
        vetorFinal = []
        while len(vetor)>0:
            rand = round((len(vetor)-1)*random.random())
            vetorFinal.append(vetor[rand])
            vetor.pop(rand)
        return vetorFinal
    
    # Tem pelo menos 1 movimento Horizontal e 1 movimento Vertical   
    def estados3(self,i,j):
        matriz1 = copy.deepcopy(self.matriz)
        matriz2 = copy.deepcopy(self.matriz)
        matriz3 = copy.deepcopy(self.matriz)
        # Movimento Horizontal
        if i==0 or i==self.n-1:
            # 2 movimentos horizontais e 1 vertical
            # Esquerda
            aux1 = matriz1[i][j]
            matriz1[i][j] = matriz1[i][j-1]
            matriz1[i][j-1] = aux1
            # Direita
            aux2 = matriz2[i][j]
            matriz2[i][j] = matriz2[i][j+1]
            matriz2[i][j+1] = aux2
            # Movimento Vertical
            if i==0:
                # Troca com o de Baixo
                aux3 = matriz3[i][j]
                matriz3[i][j] = matriz3[i+1][j]
                matriz3[i+1][j] = aux3
            else:
                # Troca com o de Cima
                aux3 = matriz3[i][j]
                matriz3[i][j] = matriz3[i-1][j]
                matriz3[i-1][j] = aux3
        else:
            # 2 movimentos verticais e 1 horizontal
            # Cima
            aux1 = matriz1[i][j]
            matriz1[i][j] = matriz1[i+1][j]
            matriz1[i+1][j] = aux1
            # Baixo
            aux2 = matriz2[i][j]
            matriz2[i][j] = matriz2[i-1][j]
            matriz2[i-1][j] = aux2
            # Movimento Horizontal
            if j==0:
                # Troca com o da Direita
                aux3 = matriz3[i][j]
                matriz3[i][j] = matriz3[i][j+1]
                matriz3[i][j+1] = aux3
            else:
                # Troca com o da Esquerda
                aux3 = matriz3[i][j]
                matriz3[i][j] = matriz3[i][j-1]
                matriz3[i][j-1] = aux3
        # 0,1 ou 2
        vetor = [matriz1,matriz2,matriz3]
        # Embaralhando a ordem do vetor
        vetorFinal = []
        while len(vetor)>0:
            rand = round((len(vetor)-1)*random.random())
            vetorFinal.append(vetor[rand])
            vetor.pop(rand)
        return vetorFinal
    
    def estados4(self,i,j):
        matriz1 = copy.deepcopy(self.matriz)
        matriz2 = copy.deepcopy(self.matriz)
        matriz3 = copy.deepcopy(self.matriz)
        matriz4 = copy.deepcopy(self.matriz)
        # Cima
        aux1 = matriz1[i][j]
        matriz1[i][j] = matriz1[i+1][j]
        matriz1[i+1][j] = aux1
        # Baixo
        aux2 = matriz2[i][j]
        matriz2[i][j] = matriz2[i-1][j]
        matriz2[i-1][j] = aux2
        #Direita
        aux3 = matriz3[i][j]
        matriz3[i][j] = matriz3[i][j+1]
        matriz3[i][j+1] = aux3
        #Esquerda
        aux4 = matriz4[i][j]
        matriz4[i][j] = matriz4[i][j-1]
        matriz4[i][j-1] = aux4
        # 0,1,2 ou 3
        vetor = [matriz1,matriz2,matriz3,matriz4]
        # Embaralhando a ordem do vetor
        vetorFinal = []
        while len(vetor)>0:
            rand = round((len(vetor)-1)*random.random())
            vetorFinal.append(vetor[rand])
            vetor.pop(rand)
        return vetorFinal
    
    # Retorna um vetor de Estados com base na posição do espaço vazio
    def movimentos(self):
        for i in range(0,self.n):
            for j in range(0,self.n):
                if self.matriz[i][j]==" ":
                    # Gerar novas Matrizes
                    if i==0 or i==(self.n-1):
                        if j==0 or j==(self.n-1):
                            return self.estados2(i,j)
                        else:
                            return self.estados3(i,j)
                    else:
                        if j==0 or j==(self.n-1):
                            return self.estados3(i,j)
                        else: 

                            return self.estados4(i,j)
    def imprimirMatriz(self):
        print("-----------------------")
        for i in range(0, self.n):
            print(self.matriz[i])
    
    # "matriz = None" indica uma aridade múltipla(Sobrecarga)
    def __init__(self,n,matriz=None):
        if matriz == None:
            self.n = n
            self.matriz = []
            pecas = []
            # Gerar o estado inicial
            for i in range(1,n**2):
                pecas.append(i)
            pecas.append(" ")
            for i in range(0,n):
                linha = []
                for j in range(0,n):
                    index = round((len(pecas)-1)*random.random())
                    linha.append(pecas[index])
                    pecas.pop(index)
                self.matriz.append(linha)
        else:
            # Se a matriz já foi passada como parâmetro, não é necessário criar randomicamente
            self.n = n
            self.matriz = matriz

def buscaEmLargura(estadoInicial : Estado, estadoFinal: Estado):
    fila = [estadoInicial.matriz]
    while estadoFinal.matriz not in fila:
        # Adicionando novos elementos na fila
        for matriz in Estado(len(fila[0]),fila[0]).movimentos():
            Estado(len(matriz),matriz).imprimirMatriz()
            fila.append(matriz)
        # Retirando o elemento na frente da fila
        fila.pop(0)
    return len(fila)

def buscaEmProfundidade(estadoInicial: Estado ,estadoFinal : Estado):
    cont=0
    fila = [estadoInicial]
    while fila[0].matriz != estadoFinal.matriz:
        fila[0].imprimirMatriz()
        cont+=1
        novasMatrizes = fila[0].movimentos()
        index = 1
        for matriz in novasMatrizes:
            fila.insert(index,Estado(len(matriz),matriz))
            index+=1
        fila.pop(0)
    return cont

def buscaIterativaEmProfundidade(estadoInicial : Estado,estadoFinal : Estado,limite=5):
    cont=0
    nivel = 0
    fila = [estadoInicial]
    print("Estado Inicial")
    while fila[0].matriz != estadoFinal.matriz:
        cont+=1
        if nivel<limite:
            fila[0].imprimirMatriz()
            novasMatrizes = fila[0].movimentos()
            index = 1
            for matriz in novasMatrizes:
                fila.insert(index,Estado(len(matriz),matriz))
                index+=1
            fila.pop(0)
            nivel+=1
        elif nivel==limite:
            # Cheguei até o limite da profundidade
            for i in range(0,len(novasMatrizes)):
                if fila[0].matriz != estadoFinal.matriz:
                    fila[0].imprimirMatriz()
                    cont+=1
                    fila.pop(0)
                else:
                    fila[0].imprimirMatriz()
                    return cont
            nivel-=1
        if len(fila)==0:
            fila=[estadoInicial]
            # Incrementando o Limite
            limite+=1
            
    fila[0].imprimirMatriz()
    return cont

# Heurística 1(Número de Peças na posição Correta)
def posicoesCorretas(estadoInicial : Estado,estadoFinal : Estado):
    cont = 0
    for i in range(0,len(estadoInicial.matriz)):
        for j in range(0,len(estadoInicial.matriz)):
            if estadoInicial.matriz[i][j] == estadoFinal.matriz[i][j]:
                cont+=1
    return cont

# Heurística 2 (Menor número de movimentos que ainda faltam para terminar o jogo)
def movimentosFaltantes(movimentosdoEstado, estadoFinal : Estado,cont=1):
    novasMatrizes = []
    for matriz in movimentosdoEstado:
        matrizes = Estado(len(matriz),matriz).movimentos()
        if estadoFinal.matriz not in matrizes:
            # Abastece as novas Matrizes
            for matriz2 in matrizes:
                novasMatrizes.append(matriz2)
        else:
            return cont+1
    return movimentosFaltantes(novasMatrizes,estadoFinal,cont+1)

def buscaHeuristica(estadoInicial : Estado, estadoFinal : Estado):
    estadoInicial.imprimirMatriz()
    novasMatrizes = estadoInicial.movimentos()
    menor = math.inf
    melhorEstado = None
    for matriz in novasMatrizes:
        estado = Estado(len(matriz),matriz)
        if movimentosFaltantes(estado.movimentos(),estadoFinal)<menor:
            menor = movimentosFaltantes(estado.movimentos(),estadoFinal)
            melhorEstado = estado
        elif movimentosFaltantes(estado.movimentos(),estadoFinal)==menor:
            if posicoesCorretas(estado,estadoFinal)>posicoesCorretas(melhorEstado,estadoFinal):
                menor = movimentosFaltantes(estado.movimentos(),estadoFinal)
                melhorEstado = estado
    if melhorEstado.matriz == estadoFinal.matriz:
        melhorEstado.imprimirMatriz()
    else:
        buscaHeuristica(melhorEstado,estadoFinal)
#main            
num = 3
# Exemplo simples de Matriz Inicial
matrizInicial = [[2, 3, 4], [1, 5, 6], [7, " ", 8]]
# Criando o Estado Inicial
estadoInicial = Estado(num,matrizInicial)
matrizFinal = [[1, 2, 3], [8, " ", 4], [7, 6, 5]]
estadoFinal = Estado(num, matrizFinal)
# print(f"Total de Buscas = {buscaIterativaEmProfundidade(estadoInicial,estadoFinal)}")
buscaHeuristica(estadoInicial,estadoFinal)