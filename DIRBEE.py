import os
import requests
import re
from datetime import datetime
import whois
from ping3 import ping

# ANSI escape code for yellow text
YELLOW = "\033[93m"
# ANSI escape code for green text
GREEN = "\033[92m"
# ANSI escape code for white text
WHITE = "\033[97m"
# ANSI escape code for red text
RED = "\033[91m"
# ANSI escape code to reset text color
RESET = "\033[0m"

def scan_directory(base_url, directory, found_list):
    url = f"{base_url}/{directory}"
    response = requests.get(url)
    
    if response.status_code == 200:
        found_list.append(GREEN + url + RESET)

def perform_whois_search(domain):
    try:
        w = whois.whois(domain)
        whois_info = []
        whois_info.append("\nWHOIS Information:")
        whois_info.append("Domain Name: " + str(w.domain_name))
        whois_info.append("Registrar: " + str(w.registrar))
        whois_info.append("Creation Date: " + str(w.creation_date))
        whois_info.append("Expiration Date: " + str(w.expiration_date))
        whois_info.append("Updated Date: " + str(w.updated_date))
        whois_info.append("Name Servers: " + str(w.name_servers))
        return "\n".join(whois_info)
    except Exception as e:
        return "Error performing WHOIS search: " + str(e)

def save_report(found_directories, whois_results):
    filename = input("Enter a filename to save the report (without extension): ") + ".txt"
    with open(filename, "w") as report_file:
        # Get current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_file.write(f"Report generated by DIRBEE on: {current_datetime}\n\n")
        
        for directory in found_directories:
            # Remove ANSI escape codes before writing to file
            clean_directory = re.sub(r'\033\[\d+m', '', directory)
            report_file.write(clean_directory + "\n")
        
        # Write WHOIS information to the report
        report_file.write(whois_results)

    print(f"\033[32mReport saved as\033[0m {filename}")

def main():
    ascii_art = """
~~~~~~~~~~~~~~ KILLJOY.DEV ~~~~~~~~~~~~~~~ 
\033[33m██████╗~██╗██████╗ ██████╗ ███████╗███████╗
██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔════╝
██║~~██║██║██████╔╝██████╔╝█████╗~~█████╗  
██║~~██║██║██╔══██╗██╔══██╗██╔══╝~~██╔══╝  
██████╔╝██║██║~~██║██████╔╝███████╗███████╗
╚═════╝~╚═╝╚═╝~~╚═╝╚═════╝ ╚══════╝╚══════╝\033[0m
~~~~~~~~~~~~~~ DIRECTORY BEE ~~~~~~~~~~~~~~
    """
    print(ascii_art)

    exit_art = """
\033[33m
~~~~~~~~ THANKS FOR USING ~~~~~~~~

              \     / 
          \    o ^ o    / 
            \ (     ) / 
 ____________(%%%%%%%)____________ 
(     /   /  )%%%%%%%(  \   \     ) 
(___/___/__/           \__\___\___) 
   (     /  /(%%%%%%%)\  \     ) 
    (__/___/ (%%%%%%%) \___\__) 
            /(       ) | 
          /   (%%%%%)   \ 
         /     (%%%)      \ 
                 !

~~~~~~~~~~ DIRECTORY BEE ~~~~~~~~~~\033[0m
    """

    while True:
        target_url = input("\033[33mEnter the target URL: \033[0m")

        if target_url.lower() == 'exit':
            break

        # Perform a ping on the target URL
        try:
            response_time = ping(target_url, unit='ms')
            print(f"\033[32mTarget is online. Response time:\033[0m {response_time:.2f} ms")
        except:
            print("Target is offline.")

        wordlist_folder = os.path.join(os.path.dirname(__file__), "Wordlists")
        wordlists = [f for f in os.listdir(wordlist_folder) if f.endswith(".txt")]
        
        print("\033[33mAvailable wordlists:\033[0m")
        for idx, wordlist in enumerate(wordlists, start=1):
            print(f"{YELLOW}{idx}. {RESET}{WHITE}{wordlist}{RESET}")

        wordlist_choice = int(input("\033[33mEnter the number of the wordlist to use: \033[0m")) - 1
        if wordlist_choice < 0 or wordlist_choice >= len(wordlists):
            print("Invalid choice.")
            return

        wordlist_path = os.path.join(wordlist_folder, wordlists[wordlist_choice])

        found_directories = []

        with open(wordlist_path, "r") as wordlist_file:
            for line in wordlist_file:
                line = line.strip()
                # Skip lines starting with '#' (comments)
                if line and not line.startswith("#"):
                    scan_directory(target_url, line, found_directories)

        if found_directories:
            print("\n\033[33mReport\033[0m - Found Directories:")
            print("\n".join(found_directories))
            
            whois_option = input("\n\033[33mDo you want to perform a WHOIS search?\033[0m (yes/no): ")
            whois_results = ""
            if whois_option.lower() in ['yes', 'y']:
                whois_results = perform_whois_search(target_url)

            save_option = input("\n\033[33mDo you want to save the report?\033[0m (yes/no): ")
            if save_option.lower() in ['yes', 'y']:
                save_report(found_directories, whois_results)
                goodbye_option = input("\nWould you like to scan another target? (yes/no): ")
                if goodbye_option.lower() not in ['yes', 'y']:
                    print(exit_art)
                    break
            else:
                print(exit_art)
                break
        else:
            print(RED + "\nNo directories found." + RESET)
            goodbye_option = input("\nWould you like to scan another target? (yes/no): ")
            if goodbye_option.lower() not in ['yes', 'y']:
                print(exit_art)
                break

if __name__ == "__main__":
    main()
