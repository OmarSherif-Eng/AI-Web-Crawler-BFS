from graph_builder import load_graph
from collections import deque
def run_crawler(rootPage, maxDepth):
    graph = load_graph("website_data.txt")
    if not graph:
        return "Error loading graph!"
    visited = set()
    queue = deque([(rootPage, 0)])
    visited.add(rootPage)
    levels_dict = {}
    while queue:
        currentNode, currentDepth = queue.popleft()
        if currentDepth not in levels_dict:
            levels_dict[currentDepth] = []
        levels_dict[currentDepth].append(currentNode)
        if currentDepth < maxDepth:
            for neighbor in graph[currentNode]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, currentDepth + 1))
    for depth, pages in levels_dict.items():
        print(f"Level {depth}: {pages}")
    return "BFS finished"
if __name__ == "__main__":
    print("=== Welcome to the AI Web Crawler ===")
    user_root = input("Enter the Root Page (e.g., Home): ")
    user_depth = int(input("Enter Max Depth (1 to 4): "))
    
    result = run_crawler(user_root, user_depth)
    print(result)
