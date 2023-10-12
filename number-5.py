import heapq

# Define the graph with new variable names
new_graph = {
    'S': {'neighbors': {'A': 3, 'B': 1}, 'heuristic': 7},
    'A': {'neighbors': {'B': 2, 'C': 2}, 'heuristic': 5},
    'B': {'neighbors': {'C': 3}, 'heuristic': 7},
    'C': {'neighbors': {'D': 4, 'G': 4}, 'heuristic': 4},
    'D': {'neighbors': {'G': 1}, 'heuristic': 1},
    'G': {'neighbors': {}, 'heuristic': 0}
}

# Depth-First Search (Tree Search)
def depth_first_search_tree(new_graph, start, goal):
    stack = [(start, [])]
    visited = set()
    expanded_states = []

    while stack:
        node, path = stack.pop()
        expanded_states.append(node)
        if node == goal:
            return (
                "Depth-First Search (Tree Search):",
                expanded_states,
                path + [node],
                list(set(new_graph.keys()) - set(expanded_states))
            )
        if node not in visited:
            visited.add(node)
            neighbors = [n for n in new_graph[node]['neighbors']]
            stack.extend((n, path + [node]) for n in neighbors if n not in visited)

# Breadth-First Search (Tree Search)
def breadth_first_search_tree(new_graph, start, goal):
    queue = [(start, [])]
    visited = set()
    expanded_states = []

    while queue:
        node, path = queue.pop(0)
        expanded_states.append(node)
        if node == goal:
            return (
                "Breadth-First Search (Tree Search):",
                expanded_states,
                path + [node],
                list(set(new_graph.keys()) - set(expanded_states))
            )
        if node not in visited:
            visited.add(node)
            neighbors = [n for n in new_graph[node]['neighbors']]
            queue.extend((n, path + [node]) for n in neighbors if n not in visited)

# Uniform Cost Search (Tree Search)
def uniform_cost_search_tree(new_graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()
    expanded_states = []

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        expanded_states.append(node)
        if node == goal:
            return (
                "Uniform Cost Search (Tree Search):",
                expanded_states,
                path + [node],
                list(set(new_graph.keys()) - set(expanded_states))
            )
        if node not in visited:
            visited.add(node)
            neighbors = [(n, cost + new_graph[node]['neighbors'][n]) for n in new_graph[node]['neighbors']]
            for n, new_cost in neighbors:
                heapq.heappush(priority_queue, (new_cost, n, path + [node]))

# Greedy Search (Tree Search)
def greedy_search_tree(new_graph, start, goal):
    priority_queue = [(new_graph[start]['heuristic'], start, [])]
    visited = set()
    expanded_states = []

    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)
        expanded_states.append(node)
        if node == goal:
            return (
                "Greedy Search (Tree Search):",
                expanded_states,
                path + [node],
                list(set(new_graph.keys()) - set(expanded_states))
            )
        if node not in visited:
            visited.add(node)
            neighbors = [n for n in new_graph[node]['neighbors']]
            priority_queue.extend((new_graph[n]['heuristic'], n, path + [node]) for n in neighbors if n not in visited)

# A* Search (Tree Search)
def a_star_search_tree(new_graph, start, goal):
    priority_queue = [(new_graph[start]['heuristic'], 0, start, [])]
    visited = set()
    expanded_states = []

    while priority_queue:
        _, cost_so_far, node, path = heapq.heappop(priority_queue)
        expanded_states.append(node)
        if node == goal:
            return (
                "A* Search (Tree Search):",
                expanded_states,
                path + [node],
                list(set(new_graph.keys()) - set(expanded_states))
            )
        if node not in visited:
            visited.add(node)
            neighbors = [(n, cost_so_far + new_graph[node]['neighbors'][n]) for n in new_graph[node]['neighbors']]
            for n, new_cost in neighbors:
                heapq.heappush(priority_queue, (new_cost + new_graph[n]['heuristic'], new_cost, n, path + [node]))

# Format and print results
def print_search_results(result):
    search_name, expanded_states, path, not_expanded = result
    print(f"{search_name}\nOrder: {expanded_states}\nPath: {path}\nNot Expanded: {not_expanded}\n\n")

# Test the search algorithms for Tree Search
goal_state = 'G'
dfs_result = depth_first_search_tree(new_graph, 'S', goal_state)
bfs_result = breadth_first_search_tree(new_graph, 'S', goal_state)
ucs_result = uniform_cost_search_tree(new_graph, 'S', goal_state)
greedy_result = greedy_search_tree(new_graph, 'S', goal_state)
a_star_result = a_star_search_tree(new_graph, 'S', goal_state)

# Print results
print_search_results(dfs_result)
print_search_results(bfs_result)
print_search_results(ucs_result)
print_search_results(greedy_result)
print_search_results(a_star_result)
