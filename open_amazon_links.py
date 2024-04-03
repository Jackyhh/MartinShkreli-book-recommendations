import webbrowser

# List of Amazon book links
urls = [
    "https://amzn.to/48I5plY",
    "https://amzn.to/4aH5xEi",
    "https://amzn.to/4aJRSvZ",
    # Add the rest of your URLs here...
]

# Open each URL in a new tab in the default browser
for url in urls:
    webbrowser.open_new_tab(url)

