import networkx as nx
import matplotlib.pyplot as plt

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

lines_dict = {
    "Прутська": ["red"],
    "Садгірсько-південна": ["blue"],
    "Кільцева": ["green"],
}
edge_weight_list = [2.5, 7.0, 3.0, 1.5, 2.0,
                    2.0, 3.0, 5.0, 1.5, 2.0,
                    6.0, 1.0, 5.5, 3.0, 1.5,
                    1.0, 3.5, 5.0, 2.5, 4.5,
                    1.5]

# побудова схеми (графа)
G = nx.Graph()
G.add_edges_from(crossing_list)

for i, edge in enumerate(crossing_list):
    G[edge[0]][edge[1]]['lenght'] = edge_weight_list[i]

for edge in crossing_list[:6]:
    G.edges[edge]["line_name"] = "Прутська"

for edge in crossing_list[6:12]:
    G.edges[edge]["line_name"] = "Садгірсько-південна"

for edge in crossing_list[12:]:
    G.edges[edge]["line_name"] = "Кільцева"


# визначаємо на якій лінії знаходиться станція і кількість ліній до яких відноситься станція
for node in G.nodes:
    lines_set = set() #атрибути можуть бути тільки рядками, тому використовуємо множину, яка до того ж відкидає повтори

    for edge in G.edges:
        if node in edge:
            lines_set.add(G[edge[0]][edge[1]]["line_name"])

    string = ""
    for i in lines_set:
        string += i + "|"

    G.nodes[node]["line_names"] = string.rstrip("|")
    G.nodes[node]["lines_qty"] = len(lines_set)
    # print(node, G.nodes[node]['line_names'], G.nodes[node]['lines_qty'])

# створюємо список кольорів для розфарбовки станцій
node_list = []
node_color_list = []
for node in G.nodes:
    if G.nodes[node]["lines_qty"] > 1:
        node_list.append(node)
        node_color_list.append("violet") # перехідні станції
    else:
        node_list.append(node)
        node_color_list.append(lines_dict[G.nodes[node]["line_names"]][0])
# print(node_list)
# print(node_color_list)

# створюємо список кольорів для розфарбовки ліній
edge_list = []
edge_color_list = []
for edge in G.edges:
    edge_list.append(edge)
    edge_color_list.append(lines_dict[G.edges[edge]["line_name"]][0])
# print(edge_list)
# print(edge_color_list)

# відмальовуємо схему
plt.figure(figsize=(10, 10))

pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'lenght')

nx.draw(
    G,
    pos,
    nodelist=node_list,
    edgelist=edge_list,
    node_color=node_color_list,
    edge_color=edge_color_list,
    with_labels=True,
)
nx.draw_networkx_edge_labels(G,
                             pos,
                          edge_labels=edge_labels,
                          )
plt.title("Схема метрополітену м. Чернівці")
plt.show()

# характеристики схеми метрополітену
print('\n' * 3)

print(f"Кількість ліній: {len(lines_dict)}")
print(f"Кількість станцій: {len(G.nodes)}")
print(f"Кількість міжстанційних перегонів: {len(G.edges)}")
print(
    f'Кількість переходів між лініями: {len([node for node in G.nodes if G.nodes[node]["lines_qty"] > 1])}'
)
print("Кількість інших станцій з якими безпосердньо з'єднана станція:")
for node in G.nodes:
    print(f"    -{node:22s}: {len(G[node])} {list(G[node].keys())}")

print("\n" * 3)
