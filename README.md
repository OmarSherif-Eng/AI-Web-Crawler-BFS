# AI Web Crawler - BFS Algorithm 🕷️

This is a Python project I built to explore how search engine crawlers (like Google) navigate the web. It uses the **Breadth-First Search (BFS)** algorithm to traverse a simulated network of web pages and map out their connections level by level.

## 📌 Why I built this
I wanted to see how algorithms like BFS can be applied to real-world structures like the internet. Instead of just "finding a path," this crawler systematically visits every page at a certain "depth" before moving deeper, ensuring a complete map of the site's structure.

## 🛠️ How it Works (The Logic)
The project is split into two main parts:
1. **Graph Construction:** I used a `Dictionary` (Hash Map) to represent the website's structure (Adjacency List), where every page is a "node" and its links are "edges".
2. **BFS Traversal:** * I used a `Queue` (via Python's `collections.deque`) to manage the order of pages to visit.
   * I implemented a `Visited Set` (Hash Set) to make sure the crawler doesn't get stuck in infinite loops by visiting the same page twice.
   * The crawler respects a **Max Depth** limit, so it doesn't run forever and stays focused on the target area.

## ⚙️ Features
* **Efficient Traversal:** Uses BFS to ensure level-by-level mapping.
* **Smart Data Management:** Uses Hash-based structures for O(1) lookup time when checking visited pages.
* **Scalable:** Can handle complex simulated networks defined in a simple text file.

## 🚀 Tech Stack
* **Language:** Python 3.x
* **Core Algorithm:** Breadth-First Search (BFS)
* **Data Structures:** Queues, Sets, and Dictionaries (Hash Maps)

## 📁 Project Structure
* `crawler_bfs.py`: The main engine that runs the BFS logic.
* `graph_builder.py`: A helper script that builds and loads the website map.
* `website_data.txt`: The simulated "web" data.
