from queue import PriorityQueue

graph_data = {
    'S': {'A': 3, 'B': 1},
    'A': {'B': 2, 'C': 2},
    'B': {'C': 3},
    'C': {'D': 4, 'G': 4},
    'D': {'G': 1},
    'G': {}
}

heuristics_data = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}

start_node_data = 'S'
target_node_data = 'G'

def  depth_first_search(graph, start, target):
    stack_data = [(start, [])]
    visited_data = set()
    while stack_data:
        node_data, path_data = stack_data.pop()
        if node_data == target:
            return path_data + [node_data]
        if node_data not in visited_data:
            visited_data.add(node_data)
            neighbors_data = list(graph[node_data].keys())
            stack_data.extend((neighbor_data, path_data + [node_data]) for neighbor_data in reversed(neighbors_data) if neighbor_data not in visited_data)
    return None

start_node_data = 'S'
target_node_data = 'G'

dfs_path_data =  depth_first_search(graph_data, start_node_data, target_node_data)

if dfs_path_data:
    print("DFS Path:", dfs_path_data)
else:
    print("No path found from 'S' to 'G' using DFS.")

def  breadth_first_search(graph, start, target):
    queue_data = [(start, [start])]
    visited_data = set()
    while queue_data:
        (node_data, path_data) = queue_data.pop(0)
        visited_data.add(node_data)
        if node_data == target:
            return path_data
        neighbors_data = graph[node_data]
        for neighbor_data in neighbors_data:
            if neighbor_data not in path_data and neighbor_data not in visited_data:
                queue_data.append((neighbor_data, path_data + [neighbor_data]))

bfs_path_data =  breadth_first_search(graph_data, start_node_data, target_node_data)
print("BFS Path:", bfs_path_data)

def  uniform_cost_search(graph, start, target):
    priority_queue_data = [(0, start, [start])]
    visited_data = set()
    while priority_queue_data:
        (cost_data, node_data, path_data) = priority_queue_data.pop(0)
        visited_data.add(node_data)
        if node_data == target:
            return path_data
        neighbors_data = graph_data[node_data]
        for neighbor_data, neighbor_cost_data in neighbors_data.items():
            if neighbor_data not in path_data and neighbor_data not in visited_data:
                new_cost_data = cost_data + neighbor_cost_data
                priority_queue_data.append((new_cost_data, neighbor_data, path_data + [neighbor_data]))
                priority_queue_data.sort(key=lambda x: x[0])

ucs_path_data =  uniform_cost_search(graph_data, start_node_data, target_node_data)
print("UCS Path:", ucs_path_data)

def  greedy_search(graph, start, target, heuristics):
    priority_queue_data = [(heuristics[start], start, [start])]
    visited_data = set()
    while priority_queue_data:
        (_, node_data, path_data) = priority_queue_data.pop(0)
        visited_data.add(node_data)
        if node_data == target:
            return path_data
        neighbors_data = graph_data[node_data]
        for neighbor_data in sorted(neighbors_data, key=lambda x: heuristics_data[x]):
            if neighbor_data not in path_data and neighbor_data not in visited_data:
                priority_queue_data.append((heuristics_data[neighbor_data], neighbor_data, path_data + [neighbor_data]))
                priority_queue_data.sort(key=lambda x: x[0])

greedy_path_data =  greedy_search(graph_data, start_node_data, target_node_data, heuristics_data)
print("Greedy Search Path:", greedy_path_data)

def  a_star_search(graph, start, target, heuristics):
    priority_queue_data = [(heuristics[start], 0, start, [start])]
    visited_data = set()
    while priority_queue_data:
        (_, cost_data, node_data, path_data) = priority_queue_data.pop(0)
        visited_data.add(node_data)
        if node_data == target:
            return path_data
        neighbors_data = graph_data[node_data]
        for neighbor_data, neighbor_cost_data in sorted(neighbors_data.items(), key=lambda x: heuristics_data[x[0]]):
            if neighbor_data not in path_data and neighbor_data not in visited_data:
                new_cost_data = cost_data + neighbor_cost_data
                priority_queue_data.append((new_cost_data + heuristics_data[neighbor_data], new_cost_data, neighbor_data, path_data + [neighbor_data]))
                priority_queue_data.sort(key=lambda x: x[0])

a_star_path_data =  a_star_search(graph_data, start_node_data, target_node_data, heuristics_data)
print("A* Search Path:", a_star_path_data)
