from graph_builder import load_graph
from collections import deque

def bfs_logic(graph: dict, rootPage: str, maxDepth: int):
    
    visited = set()
    queue = deque([(rootPage, 0)])
    visited.add(rootPage)
    levels_dict: dict[int, list[str]] = {}
    traversal_order: list[tuple[str, int]] = []
    while queue:
        currentNode, currentDepth = queue.popleft()
        if currentDepth not in levels_dict:
            levels_dict[currentDepth] = []
        levels_dict[currentDepth].append(currentNode)
        traversal_order.append((currentNode, currentDepth))
        if currentDepth < maxDepth:
            for neighbor in graph[currentNode]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, currentDepth + 1))
    all_pages = set(graph.keys())
    reachable = visited
    unreachable = all_pages - reachable
    dead_ends = [page for page,links in graph.items() if len(links) == 0 ]
    return  {
        "levels": levels_dict,
        "totalPages": len(all_pages),
        "reachable": reachable,
        "unreachable": unreachable,
        "dead_ends": dead_ends,
        "rootPage": rootPage,
        "maxDepth": maxDepth,
        "traversal": traversal_order

    }

def print_levels(levels_dict: dict):
    print("\n" + "=" * 50)
    print("  OUTPUT (1): Pages Discovered Per Level")
    print("=" * 50)
    for depth, pages in levels_dict.items():
        print(f"Level {depth} ({len(pages)} page{'s' if len(pages) != 1 else ''}): {', '.join(pages)}")

def print_reachability(data:dict):
    print("\n"+50*"=")
    print("  OUTPUT (2): Reachable vs. Unreachable Pages")
    print(50*"=")
    print(f"    Home page     : {data['rootPage']}.")
    print(f"    Max depth     : {data['maxDepth']}.")
    print(f"    Total pages   : {data['totalPages']}")
    print(f"    Reachable     : {len(data['reachable'])} -> {sorted(data['reachable'])}")
    print(f"    Unreachable   : {len(data['unreachable'])} -> {sorted(data['unreachable'])}")

def print_traversal_order(traversal_order:list):
    print("\n"+ 50 *"=")
    print("  OUTPUT (3): Full BFS Traversal Order")
    print(50*"=")
    for index, (page, depth)in enumerate(traversal_order, start=1):
        print(f"    {index:>3}. [Depth {depth}]  {page}")
def print_dead_ends(dead:list):
    print("\n"+50*"=")
    print("  OUTPUT (4): Dead-End Pages (No Outgoing Links)")
    print("=" * 50)
    if dead:
        for page in dead:
            print(f"  - {page}")
    else:
        print("  No dead-end pages found.")
def print_tree(levels_dict: dict):
    print("\n"+50*"=")
    print("  Tree-Style Level-by-Level Diagram")
    print(50*"=")
    for depth, pages in levels_dict.items():
        indent = "     "*depth
        connector = "+--" if depth >0 else ""
        print(f"{indent}{connector}[Level {depth}]")
        for page in pages:
            page_indent = "     "*(depth + 1)
            print(f"{page_indent}> {page}")  
def run_crawler(rootPage: str, maxDepth: int):
    graph = load_graph("website_data.txt")
    if not graph:
        return "Error loading graph!"
    #Input Validation
    if rootPage not in graph:
        print(f"Page {rootPage} doesn't exist in graph")
        print(f"Available pages: {sorted(graph)}")
        return
    if maxDepth <1 or maxDepth >4:
        print(f"[Error]! Max depth should be between 1 and 4")
        return
    bfs_data = bfs_logic(graph, rootPage, maxDepth)
    print_levels(bfs_data["levels"])
    print_reachability(bfs_data)
    print_traversal_order(bfs_data["traversal"])
    print_dead_ends(bfs_data["dead_ends"])
    print_tree(bfs_data["levels"])

    print("\n"+ "=" * 50)
    print("  BFS Crawl Complete!")
    print("=" * 50 + "\n")
    
if __name__ == "__main__":
    print("=" * 50)
    print("   Welcome to the AI Web Crawler (BFS)")
    print("=" * 50)
    user_root = input("Enter the Root Page (e.g., Home): ").strip()
    user_depth = int(input("Enter Max Depth (1 to 4): ").strip())


    run_crawler(user_root, user_depth)
