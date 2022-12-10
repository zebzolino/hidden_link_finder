import tkinter as tk
import requests
from bs4 import BeautifulSoup

# Function to test if a URL is valid
def test_url(url):
    try:
        # Send a HEAD request to the URL
        response = requests.head(url)

        # Return True if the response is successful (2xx status code)
        return response.status_code // 100 == 2
    except:
        # Return False if there is an error
        return False

# Function to find and print the hidden links on the website
def find_hidden_links():
    # Get the URL from the user input
    url = url_entry.get()

    # Download the website's HTML
    response = requests.get(url)

    # Parse the HTML using Beautiful Soup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the links from the HTML
    links = []
    for link in soup.find_all("a"):
        if link.has_attr("href"):
            url = link["href"]
            if url not in links:
                links.append(url)

    # Test each link and print the valid ones
    output_label.config(text="Links:")
    for url in links:
        if test_url(url):
            # Check if the link is hidden
            if link.has_attr("hidden"):
                output_label.config(text=output_label.cget("text") + "\n" + url + " (hidden)")
            else:
                output_label.config(text=output_label.cget("text") + "\n" + url)

# Create the tkinter window
root = tk.Tk()

# Create a label and entry field for the URL
url_label = tk.Label(root, text="URL:")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

# Create a label for the output
output_label = tk.Label(root, text="")
output_label.pack()

# Create a button to find the hidden links
find_button = tk.Button(root, text="Find Hidden Links", command=find_hidden_links)
find_button.pack()

# Start the tkinter event loop
root.mainloop()
