import numpy as np

# Nome, prioridade sendo 0 a maior, ID
tarefas = [
    ("Supermercado", 3, 0),
    ("Farmacia", 1, 1),
    ("Padaria", 2, 2),
    ("Banco", 5, 3),
    ("Correio", 4, 4),
    ("Casa", 0, 5)
]

# Matriz de distâncias entre locais
distancias = np.array([
    [0, 2, 9, 10, 5, 3],  # Supermercado
    [2, 0, 6, 4, 8, 6],   # Farmácia
    [9, 6, 0, 3, 7, 8],   # Padaria
    [10, 4, 3, 0, 2, 7],  # Banco
    [5, 8, 7, 2, 0, 4],   # Correio
    [3, 6, 8, 7, 4, 0]    # Casa
])

# Função para ordenar tarefas por prioridade


def ordenar_tarefas(tarefas):
    return sorted(tarefas, key=lambda x: x[1])

# Função para calcular o percurso baseado na ordem das tarefas


def calcular_percurso(tarefas, distancias):
    percurso = [tarefas[0]]  # Começar pela primeira tarefa
    total_distancia = 0

    distancias_individuais = []  # Lista para armazenar distâncias individuais

    for i in range(len(tarefas) - 1):
        origem = percurso[-1][2]  # ID da última tarefa no percurso
        destino = tarefas[i + 1][2]  # ID da próxima tarefa
        distancia = distancias[origem][destino]
        total_distancia += distancia
        # (tarefa atual, próxima tarefa, distância)
        distancias_individuais.append(
            (percurso[-1][0], tarefas[i + 1][0], distancia))
        percurso.append(tarefas[i + 1])

    return percurso, total_distancia, distancias_individuais


# Ordenar as tarefas
tarefas_ordenadas = ordenar_tarefas(tarefas)

# Calcular o percurso e a distância total
percurso, distancia_total, distancias_individuais = calcular_percurso(
    tarefas_ordenadas, distancias)

# Exibir o resultado
print("Tarefas ordenadas por prioridade:")
for tarefa in tarefas_ordenadas:
    print(f"- {tarefa[0]} (Prioridade: {tarefa[1]}, ID: {tarefa[2]})")

print("\nPercurso das tarefas:")
for tarefa in percurso:
    print(f"- {tarefa[0]}")

print("\nDistâncias entre as tarefas:")
for origem, destino, distancia in distancias_individuais:
    print(f"Distância de {origem} para {destino}: {distancia}")

print(f"\nDistância total do percurso: {distancia_total}")
