import requests
import random
import time
import os
from colorama import Fore, Back, Style
from termcolor import colored

# Function to read proxies from a file in the current directory
def load_proxies(file_name="proxies.txt"):
    proxies_list = []
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    proxies_list.append({"http": line, "https": line})
    else:
        print(Fore.RED + f"Proxies file '{file_name}' not found!")
    return proxies_list

# List of proxies loaded from the file
proxies_list = load_proxies()

# Function to get a random proxy from the list
def get_random_proxy():
    if proxies_list:
        return random.choice(proxies_list)
    else:
        print(Fore.RED + "No proxies available!")
        return None

# Rainbow text function
def rainbow_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    colored_text = ""
    color_index = 0
    for char in text:
        colored_text += colors[color_index % len(colors)] + char
        color_index += 1
    return colored_text

# ASCII Logo for "Tool"
def print_logo():
    logo = """
    _______  _______  _______  _______ 
   (  __   )(  __   )(  __   )(  __   )
   | (  )  | (  )  | (  )  | (  )  |
   | | /   | | /   | | /   | | /   | 
   | (/ /) | (/ /) | (/ /) | (/ /) | 
   | |   ) | |   ) | |   ) | |   ) | 
   | (___/  | (___/  | (___/  | (___/  
    """
    print(rainbow_text(logo))

# Function to simulate Google Dork search for usernames
def google_dork_search(username):
    # Crafting the Google Dork query
    query = f"\"{username}\" site:linkedin.com OR site:github.com OR site:twitter.com"
    
    # Use a random proxy from the list
    proxy = get_random_proxy()
    if not proxy:
        print(Fore.RED + "No proxy available to make the request.")
        return
    
    print(Fore.YELLOW + f"Performing Google Dork search with query: {query}")
    print(Fore.YELLOW + f"Using proxy: {proxy}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    try:
        # Make a request to Google (in reality, you'd use Google Custom Search API or scrape SERPs)
        response = requests.get(f"https://www.google.com/search?q={query}", headers=headers, proxies=proxy, timeout=5)
        
        if response.status_code == 200:
            print(Fore.GREEN + "Results found:")
            # Fake the extraction of results (just an example)
            # In practice, you'd parse the page using BeautifulSoup
            print(Fore.GREEN + f"LinkedIn: https://www.linkedin.com/in/{username}")
            print(Fore.GREEN + f"GitHub: https://github.com/{username}")
            print(Fore.GREEN + f"Twitter: https://twitter.com/{username}")
        else:
            print(Fore.RED + "Error while performing search.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error with the request: {e}")

# Function to get IP geolocation
def get_ip_info(ip_address):
    print(Fore.YELLOW + f"Fetching geolocation data for IP: {ip_address}...")
    url = f"http://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url, proxies=get_random_proxy())
        
        if response.status_code == 200:
            data = response.json()
            location = data.get("city", "Unknown") + ", " + data.get("region", "Unknown") + ", " + data.get("country", "Unknown")
            print(Fore.GREEN + f"Location: {location}")
            print(Fore.GREEN + f"IP: {data.get('ip')}")
            print(Fore.GREEN + f"Hostname: {data.get('hostname')}")
        else:
            print(Fore.RED + "Error fetching IP data.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error with the IP request: {e}")

# Main tool interface with menu
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    
    print_logo()  # Display the ASCII logo

    print(rainbow_text("-" * 40))
    print(rainbow_text("  Welcome to the Advanced Deep Search Tool"))
    print(rainbow_text("-" * 40))
    
    print(rainbow_text("1. Google Dork Search for User Profiles"))
    print(rainbow_text("2. Get IP Geolocation"))
    print(rainbow_text("3. Exit"))
    
    choice = input(Fore.WHITE + "Enter choice (1/2/3): ")
    
    if choice == "1":
        username = input(Fore.WHITE + "Enter the username to search: ")
        google_dork_search(username)
    elif choice == "2":
        ip_address = input(Fore.WHITE + "Enter IP address to geolocate: ")
        get_ip_info(ip_address)
    elif choice == "3":
        print(Fore.CYAN + "Exiting...")
        time.sleep(1)
        exit()
    else:
        print(Fore.RED + "Invalid choice. Try again.")
        time.sleep(1)
        main_menu()

# Run the menu
if __name__ == "__main__":
    main_menu()
