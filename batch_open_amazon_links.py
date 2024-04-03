import argparse
import json
import webbrowser

def open_links(start, end, json_file_path):
    # Load the JSON data from the file
    with open(json_file_path, 'r') as file:
        links = json.load(file)
    
    # Convert the keys from string back to integers for comparison
    links = {int(k): v for k, v in links.items()}
    
    # Open the links in the specified range
    for key in range(start, end + 1):
        if key in links:
            webbrowser.open_new_tab(links[key])
        else:
            print(f"Link for key {key} not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Open a range of Amazon book links from a JSON file.")
    parser.add_argument("start", type=int, help="The starting key of the link range to open.")
    parser.add_argument("end", type=int, help="The ending key of the link range to open.")
    parser.add_argument("json_file_path", type=str, help="Path to the JSON file containing the links.")
    
    args = parser.parse_args()
    
    open_links(args.start, args.end, args.json_file_path)

