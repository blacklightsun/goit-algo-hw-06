# в цьому файлі стара версія функції dfs_recc()

import networkx as nx

def dfs_recc(graf, start_v, finish_v, visited_list=None, path_list=None)-> list:

    if path_list is None:
        path_list = list()

    if visited_list is None:
        visited_list = list()

    visited_list.append(start_v)

    if start_v == finish_v:
        path_list = visited_list[:]

    for neightbor in list(graf[start_v].keys()):
        if neightbor not in visited_list:
            path_list = dfs_recc(graf, neightbor, finish_v, visited_list, path_list)

    return path_list

def wfs_recc(graf, start_v, finish_v, visited_list=None, path_list=None)-> list:

    if visited_list is None:
        visited_list = list()

    visited_list.append(start_v)

    if start_v == finish_v:
        path_list = visited_list[:]
        return path_list

    neightbors_list = list(graf[start_v].keys())
    if finish_v in neightbors_list:
        visited_list.append(finish_v)
        path_list = visited_list[:]
        return path_list
    else:
        for neightbor in neightbors_list:
            if neightbor not in visited_list:
                path_list = wfs_recc(graf, neightbor, finish_v, visited_list)
                if path_list is not None :
                    return path_list

# дані для побудови схеми (малюнок тут же у теці)
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


# побудова схеми (графа)
G = nx.Graph()
G.add_edges_from(crossing_list)


start_node = "Гравітон"
finish_node = "Парк ім. Шевченка"

print('\n')
path_dfs = dfs_recc(G, start_node, finish_node)
if len(path_dfs) > 0:
    print(
        f"Шлях від {start_node} до {finish_node} по методу DFS знайдено після обходу {len(path_dfs)} вузлів:\n{path_dfs}"
    )
else:
    print("Шлях по методу DFS не знайдено.")

print('\n')

path_wfs = wfs_recc(G, start_node, finish_node)
if path_wfs is not None:
    print(
        f"Шлях від {start_node} до {finish_node} по методу WFS знайдено після обходу {len(path_wfs)} вузлів:\n{path_wfs}"
    )
else:
    print("Шлях по методу DFS не знайдено.")

print("\n")
