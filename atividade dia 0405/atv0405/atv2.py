from collections import deque

# Grafo de rotas de ônibus
rotas = {
    "Twin Peaks": ["Castro", "Forest Hill"],
    "Castro": ["Downtown", "Mission"],
    "Forest Hill": ["Sunset"],
    "Mission": ["Downtown"],
    "Sunset": ["Golden Gate Park"],
    "Golden Gate Park": ["Ponte Golden Gate"],
    "Downtown": ["Ponte Golden Gate"],
    "Ponte Golden Gate": []
}

# BFS para encontrar menor caminho
def menor_caminho(inicio, destino):
    fila = deque([[inicio]])  # fila guarda caminhos completos
    visitados = set()

    while fila:
        caminho = fila.popleft()
        ultimo = caminho[-1]

        if ultimo == destino:
            print("Menor caminho:", " -> ".join(caminho))
            print("Número de etapas:", len(caminho) - 1)
            return caminho

        if ultimo not in visitados:
            for vizinho in rotas[ultimo]:
                novo_caminho = caminho + [vizinho]
                fila.append(novo_caminho)
            visitados.add(ultimo)

    print("Não há rota disponível.")
    return None

# Teste
menor_caminho("Twin Peaks", "Ponte Golden Gate")
