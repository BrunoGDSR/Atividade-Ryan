from collections import deque

# Grafo de amizades
grafo = {
    "voce": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

# Função para verificar se é vendedor de mangas
def eh_vendedor(nome):
    return nome.endswith("m")

# BFS para encontrar o vendedor
def busca_vendedor(inicio):
    fila = deque(grafo[inicio])  # fila inicial com amigos diretos
    verificados = set()          # evitar loops infinitos

    while fila:
        pessoa = fila.popleft()
        if pessoa not in verificados:
            if eh_vendedor(pessoa):
                print(f"{pessoa} é um vendedor de mangas!")
                return pessoa
            else:
                fila.extend(grafo[pessoa])
                verificados.add(pessoa)
    print("Nenhum vendedor encontrado.")
    return None

# Teste
busca_vendedor("voce")
