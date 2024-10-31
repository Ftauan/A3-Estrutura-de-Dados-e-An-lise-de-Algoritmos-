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

