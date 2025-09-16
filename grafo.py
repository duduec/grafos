# Definição do grafo com as cidades e as distâncias entre elas
grafo = {
    "Pelotas": [("Camaquã", 150), ("Rio Grande", 55), ("Bagé", 180), ("Santa Maria", 370)],
    "Camaquã": [("Pelotas", 150), ("Guaíba", 65), ("Porto Alegre", 125)],
    "Guaíba": [("Camaquã", 65), ("Porto Alegre", 30)],
    "Rio Grande": [("Pelotas", 55), ("Porto Alegre", 320)],
    "Bagé": [("Pelotas", 180), ("Porto Alegre", 380)],
    "Santa Maria": [("Pelotas", 370), ("Porto Alegre", 290)],
    "Porto Alegre": [("Camaquã", 125), ("Guaíba", 30), ("Rio Grande", 320), ("Bagé", 380), ("Santa Maria", 290)]
}

# -------------------------------
# Algoritmo de Busca em Largura (BFS)
# -------------------------------
def bfs(inicio, objetivo):
    visitados = set()
    fila = [(inicio, [inicio])]  # cidade_atual, caminho_percorrido

    while fila:
        cidade, caminho = fila.pop(0)  # Remove o primeiro da fila

        if cidade == objetivo:
            return caminho  # Caminho encontrado

        if cidade not in visitados:
            visitados.add(cidade)
            for vizinho, _ in grafo[cidade]:
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho]))

    return None

# -------------------------------
# Algoritmo de Busca em Profundidade (DFS)
# -------------------------------
def dfs(inicio, objetivo, caminho=None, visitados=None, custo=0):
    if caminho is None:
        caminho = [inicio]
    if visitados is None:
        visitados = []

    if inicio == objetivo:
        return caminho, custo  # Caminho encontrado com o custo

    visitados.append(inicio)

    for vizinho, peso in grafo[inicio]:
        if vizinho not in visitados:
            resultado = dfs(vizinho, objetivo, caminho + [vizinho], visitados, custo + peso)
            if resultado[0] is not None:
                return resultado  # Retorna o caminho encontrado

    return None, 0  # Se não encontrar caminho

# -------------------------------
# Algoritmo de Dijkstra
# -------------------------------
def dijkstra(inicio, objetivo):
    custos = {cidade: float('inf') for cidade in grafo}  # Inicializa custos como infinito
    caminhos = {cidade: [] for cidade in grafo}  # Armazena os caminhos
    visitados = []

    custos[inicio] = 0
    caminhos[inicio] = [inicio]

    while True:
        atual = None
        menor = float('inf')

        # Pega o vértice não visitado com menor custo
        for cidade in grafo:
            if cidade not in visitados and custos[cidade] < menor:
                menor = custos[cidade]
                atual = cidade

        if atual is None:
            break

        if atual == objetivo:
            return caminhos[atual], custos[atual]

        visitados.append(atual)

        # Atualiza custos dos vizinhos
        for vizinho, peso in grafo[atual]:
            if custos[atual] + peso < custos[vizinho]:
                custos[vizinho] = custos[atual] + peso
                caminhos[vizinho] = caminhos[atual] + [vizinho]

    return None, 0

# -------------------------------
# Execução dos algoritmos e comparação
# -------------------------------
inicio = "Pelotas"
objetivo = "Porto Alegre"

# Executando BFS
caminho_bfs = bfs(inicio, objetivo)

# Executando DFS
caminho_dfs, custo_dfs = dfs(inicio, objetivo)

# Executando Dijkstra
caminho_dij, custo_dij = dijkstra(inicio, objetivo)

# Exibindo resultados

# BFS: ['Pelotas', 'Camaquã', 'Porto Alegre'] | Passos: 2
# DFS: ['Pelotas', 'Camaquã', 'Guaíba', 'Porto Alegre'] | Passos: 3 | Custo total: 245 km
# Dijkstra: ['Pelotas', 'Camaquã', 'Guaíba', 'Porto Alegre'] | Passos: 3 | Custo total: 245 km