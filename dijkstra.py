from queue import PriorityQueue  #primeira mudança desse código pros outros: finalmente temos que importar uma classe de um módulo. Brabo. É uma fila de prioridade


class Graph:

  def __init__(self,
               numVertices):  #método construtor, recebe número de vértices
    self.numVertices = numVertices
    self.matriz_adj = [
      [-1 for i in range(numVertices)] for j in range(numVertices)
    ]  #ele exibe as arestas como uma matriz de adj, importante notar que ele inicializa os valores como -1

  def addAresta(self, vertice1, vertice2, peso):  #adicionando aresta
    self.matriz_adj[vertice1][vertice2] = peso
    self.matriz_adj[vertice2][vertice1] = peso

  def dijkstra(
    self, origem, destino
  ):  #método de dijkstra não gera uma árvore mínima, é um método de cálculo de caminhos mínimos.
    D = {
      vertice: float('inf')
      for vertice in range(self.numVertices)
    }  #D é a lista das distancias totais de cada caminho. Todas iniciando com valor infinito
    D[origem] = 0  #definimos a distância para o vértice inicial como 0
    Percursos = [[] for indice in range(self.numVertices)]  #lista de percursos
    Percursos[origem] = [origem]
    pq = PriorityQueue()  #pq é a fila de prioridade
    pq.put(
      (0,
       origem))  #o vértice inicial é colocado na frente da fila (prioridade 0)
    visitado = []  #essa lista vai armazenar os vértices que já visitamos

    while not pq.empty():  #A condição de repetição é a lista não vazia
      (dist, verticeAtual) = pq.get(
      )  #retiramos da fila o vértice que está sendo analisado atualmente e sua distância do ponto de origem
      visitado.append(
        verticeAtual
      )  #adicionamos o vértice que está sendo analisado na lista de vértices visitados

      for vizinho in range(
          self.numVertices
      ):  #vemos todos os possíveis vizinhos do nosso vértice atual (todos os vértices)
        if self.matriz_adj[verticeAtual][
            vizinho] != -1:  #se tiver uma aresta entre eles, o valor na matriz será diferente de -1
          distancia = self.matriz_adj[verticeAtual][
            vizinho]  #definimos a distância para esse vizinho como o valor da interseção na matriz (peso da aresta)
          if vizinho not in visitado:  #se esse vizinho ainda não estivar na lista de vértices já visitados, nós verificamos a distância
            distanciaAnterior = D[
              vizinho]  #vemos o custo antigo guardado para esse vizinho (inicializado como infinito ali quando declaramos D)
            distanciaNova = D[
              verticeAtual] + distancia  #novo custo é a distância do vértice origem até o atual + a distância desse atual até o vizinho
            if distanciaNova < distanciaAnterior:  #se o custo for menor, atualizamos o valor em D e colocamos a prioridade e o vértice na fila
              pq.put((distanciaNova, vizinho))
              Percursos[vizinho] = Percursos[verticeAtual].copy()
              Percursos[vizinho].append(vizinho)
              D[vizinho] = distanciaNova

    for vertice in range(
        len(D)
    ):  #impressão das distâncias partindo do vertice inicial a todos os outros vértices
      print("(", origem, ",", vertice, ") = ", D[vertice])
      print("Percurso: ", Percursos[vertice])

    print(
      "(", origem, ",", destino, ") = ", D[destino], ", Percurso = { ",
      Percursos[destino], "}"
    )  #impressão da distância do ponto de origem ao ponto de destino especificado


#iniciando o grafo: 'NomeDoGrafo = Graph(tamanho)
#adicionando aresta: NomeDoGrafo.addAresta(vertice1, vertice2, peso)
#usando dijkstra: NomeDoGrafo.dijkstra(origem, destino)  Obs: Foi adicionado 3 linhas para mostrar todos os caminhos possíveis partindo da origem.
neografo = Graph(7)
neografo.addAresta(0, 1, 3)
neografo.dijkstra(1, 5)

#créditos: https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/dijkstras-algorithm/
