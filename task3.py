import networkx as nx
import matplotlib.pyplot as plt

# дані для побудови схеми (вихідний малюнок тут же у теці)
crossing_list = [
    ("Заводська", "Прутська"),
    ("Прутська", "Вокзальна"),
    ("Вокзальна", "Центральна"),
    ("Центральна", "Зелена"),
    ("Зелена", "Фастівська"),
    ("Фастівська", "Гравітон"),
    ("Московська", "Садгірська"),
    ("Садгірська", "Калинівський ринок"),
    ("Калинівський ринок", "Центральна"),
    ("Центральна", "Парк ім. Шевченка"),
    ("Парк ім. Шевченка", "Проспект Незалежності"),
    ("Проспект Незалежності", "Озерна"),
    ("Університет", "Вокзальна"),
    ("Вокзальна", "Калинівський ринок"),
    ("Калинівський ринок", "Фастівська"),
    ("Фастівська", "Аеропорт"),
    ("Аеропорт", "Проспект Незалежності"),
    ("Проспект Незалежності", "Дубинська"),
    ("Дубинська", "Горіхівська"),
    ("Горіхівська", "Цецино"),
    ("Цецино", "Університет"),
]

edge_lenght_list = [2.5, 7.0, 3.0, 1.5, 4.0,
                    2.0, 3.0, 5.0, 1.5, 2.0,
                    6.0, 1.0, 5.5, 3.0, 1.5,
                    1.0, 3.5, 5.0, 2.5, 4.5,
                    1.5]

# створюємо зважений граф
G = nx.Graph(crossing_list)
for i, edge in enumerate(crossing_list):
    G[edge[0]][edge[1]]['lenght'] = edge_lenght_list[i]

def dijkstra(graph, start_node):
    # функція написана по опису алгоритму з конспекту, без підглядання в код з конспекту
    dist_dict = {node: float('inf') for node in graph.nodes}
    dist_dict[start_node] = 0
    unvisited_list = list(graph.nodes)

    while unvisited_list:
        # print(start_node)
        # print(unvisited_list)
        for node in graph[start_node]:
            if dist_dict[node] > dist_dict[start_node] + graph[start_node][node]['lenght']:
                dist_dict[node] = dist_dict[start_node] + graph[start_node][node]['lenght']
        # print(dist_dict)
        unvisited_list.pop(unvisited_list.index(start_node))

        # пошук найближчої ноди
        near_node = None
        near_node_distance = float('inf')
        # for node in graph[start_node]:
        for node in dist_dict:
            if dist_dict[node] < near_node_distance and node in unvisited_list:
                near_node = node
                near_node_distance = dist_dict[node]
        if near_node is not None:
            start_node = near_node

    return dist_dict

start = "Центральна"
print(f'\nНайкоротші дистанції від станції {start}:')
for node, dist in dijkstra(G, start).items():
    print(node, dist)