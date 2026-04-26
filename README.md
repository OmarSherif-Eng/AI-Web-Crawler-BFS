# AI Web Crawler - BFS Algorithm 🕷️

A Python-based crawler that simulates search engine behavior using the **Breadth-First Search (BFS)** algorithm to traverse, analyze, and map interconnected web pages.

## 🚀 What's New in this Version? (Advanced Graph Analysis)
The core logic has been heavily upgraded to include deep structural analysis of the web graph:
* **Tree-Style Visualization:** Generates a clean, level-by-level CLI tree diagram (`+-- [Level X]`) to easily visualize the hierarchy of the traversal.
* **Isolated Node Detection:** Automatically calculates and lists **Unreachable Pages** that cannot be accessed from the given root node.
* **Dead-End Identification:** Scans the network for nodes/pages with zero outbound links (Dead-ends).
* **Smart Input Validation:** Ensures the crawler respects strict boundary conditions, validating root page existence and enforcing a max search depth (1 to 4).

## 🛠️ Core Tech & Logic
* **Graph Representation:** Built using an Adjacency List via Python `Dictionaries`.
* **Traversal Engine:** Utilizes Python's `collections.deque` for optimized, thread-safe queue operations.
* **State Management:** Implements `Hash Sets` for O(1) time complexity when tracking visited nodes, preventing infinite loops.

## 🧠 Why this matters?
This project demonstrates a practical application of Data Structures (Graphs, Queues, Hash Maps) and algorithms to solve real-world mapping problems, mimicking the foundational logic of tools like Googlebot.
