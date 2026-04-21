import os

def create_website_file(filename="website_data.txt"):
    pages = [
        "Home", "About_Us", "Contact_Us", "Services", "Blog_Main", 
        "Login", "Register", "User_Profile", "Settings", "Products_Catalog",
        "Electronics", "Clothing", "Appliances", "Search_Page", "FAQ",
        "Terms", "Privacy", "Help_Center", "Careers", "Press",
        "Investors", "Post_1", "Post_2", "Post_3", "Product_A",
        "Product_B", "Product_C", "Sales", "Cart", "Checkout",
        "Support", "Newsletter", "Forum", "Topic_1", "Topic_2",
        "Archive", "Feedback", "Sitemap", "Gallery", "Isolated_Page"
    ]

    adj_data = {
        "Home": ["About_Us", "Services", "Products_Catalog", "Login"],
        "About_Us": ["Contact_Us", "Careers", "Press"],
        "Contact_Us": ["FAQ", "Help_Center"],
        "Services": ["Electronics", "Clothing", "Appliances"],
        "Blog_Main": ["Post_1", "Post_2", "Post_3", "Home"],
        "Login": ["Register", "User_Profile"],
        "Register": ["Privacy", "Terms"],
        "User_Profile": ["Settings", "Cart"],
        "Settings": ["Privacy"],
        "Products_Catalog": ["Electronics", "Clothing", "Product_A", "Product_B"],
        "Electronics": ["Product_A", "Product_C"],
        "Clothing": ["Sales"],
        "Appliances": ["Product_B"],
        "Search_Page": ["Products_Catalog", "Blog_Main"],
        "FAQ": ["Help_Center", "Contact_Us"],
        "Terms": ["Privacy"],
        "Privacy": [], 
        "Help_Center": ["Support", "FAQ"],
        "Careers": ["About_Us"],
        "Press": ["Investors"],
        "Investors": ["Home"],
        "Post_1": ["Blog_Main", "Topic_1"],
        "Post_2": ["Blog_Main", "Topic_2"],
        "Post_3": ["Blog_Main"],
        "Product_A": ["Cart", "Product_B"],
        "Product_B": ["Cart", "Product_A"],
        "Product_C": ["Cart"],
        "Sales": ["Product_A", "Product_B", "Product_C"],
        "Cart": ["Checkout", "Products_Catalog"],
        "Checkout": ["Login"],
        "Support": ["Help_Center"],
        "Newsletter": ["Home"],
        "Forum": ["Topic_1", "Topic_2"],
        "Topic_1": ["Forum"],
        "Topic_2": ["Forum"],
        "Archive": [], 
        "Feedback": ["Contact_Us"],
        "Sitemap": ["Home", "Products_Catalog", "Archive"],
        "Gallery": ["Post_1", "Post_2"],
        "Isolated_Page": [] 
    }

    with open(filename, "w", encoding="utf-8") as f:
        for page, links in adj_data.items():
            line = f"{page}: {', '.join(links)}\n"
            f.write(line)
    
    total_links = sum(len(v) for v in adj_data.values())
    print("--- Graph Builder Summary ---")
    print(f"SUCCESS: File '{filename}' created.")
    print(f"Total Pages: {len(adj_data)}")
    print(f"Total Links: {total_links}")
    print("-----------------------------")

def load_graph(filename="website_data.txt"):
    website_graph = {}
    if not os.path.exists(filename):
        print(f"ERROR: File '{filename}' not found!")
        return {}
    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if ":" in line:
                parts = line.split(":")
                parent = parts[0].strip()
                children = [c.strip() for c in parts[1].split(",") if c.strip()]
                website_graph[parent] = children
    return website_graph

if __name__ == "__main__":
    create_website_file()
    graph_data = load_graph()
    print(f"Sample data - Links from Home: {graph_data.get('Home')}")