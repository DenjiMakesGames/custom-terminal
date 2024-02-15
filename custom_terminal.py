import os
import subprocess
import time
import webbrowser
import json
import sys
from dotenv import load_dotenv
from extras import matrix_rain

# Load .env credentials
load_dotenv()

# Password lock based on system's password
expected_password = os.getenv("LOCK_PASSWORD")
if expected_password is None:
    print("Error: The expected password is not set in the .env file.")
    sys.exit(1)

# Set the number of allowed attempts
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    entered_password = input("\033[33mEnter your system password: ")

    if entered_password == expected_password:
        print("\033[92mPassword correct. Proceeding to the terminal.")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"\033[91mIncorrect password. {remaining_attempts} attempts remaining.")
        else:
            print("\033[91mAccess denied. Maximum attempts reached. Exiting.")
            sys.exit(1)

def matrix():
    matrix_rain.app()
    time.sleep(5)
    return

print("\nStarted > Welcome to the Matrix!\n")
print("\033[34m┌─┐┌─┐┌┬┐┌┬┐┌─┐┌┐┌┌┬┐  ┌─┐┬─┐┌─┐┌┬┐┌─┐┌┬┐\033[0m")
print("\033[94m│  │ │││││││├─┤│││ ││  ├─┘├┬┘│ ││││├─┘ │  \033[0m")
print("\033[96m└─┘└─┘┴ ┴┴ ┴┴ ┴┘└┘─┴┘  ┴  ┴└─└─┘┴ ┴┴   ┴  \033[0m")

# Function to get a shortened path with ~
def shorten_path(path):
    home = os.path.expanduser("~")
    if path.startswith(home):
        return "~" + path[len(home):]
    return path

while True:
    # Get system information
    username = os.getenv("USERNAME") or os.getenv("USER")
    hostname = os.getenv("COMPUTERNAME") or os.getenv("HOSTNAME") or os.uname().nodename
    current_directory = os.getcwd()
    current_directory = shorten_path(current_directory)

    # ANSI escape codes for text colors and styles
    reset_color = "\033[0m"
    bold = "\033[1m"
    green_color = "\033[92m"
    yellow_color = "\033[33m"
    purple_color = "\033[35m"

    # Customize the prompt with a new format
    custom_prompt = (
        f"\n{green_color}┌──({username}㉿{hostname}){purple_color} MINGW12 {yellow_color}- [{current_directory}]\n"
        f"{green_color}└─"
        f"{reset_color} $ "
    )

    # Display the customized prompt and get user input
    user_input = input(custom_prompt)

    # Check if the user wants to exit the custom terminal
    if user_input.lower() == "exit":
        print("Closing The Matrix")
        time.sleep(1)
        break

    elif user_input.lower() == "splash":
        print("\033[34m┌─┐┌─┐┌┬┐┌┬┐┌─┐┌┐┌┌┬┐  ┌─┐┬─┐┌─┐┌┬┐┌─┐┌┬┐\033[0m")
        print("\033[94m│  │ │││││││├─┤│││ ││  ├─┘├┬┘│ ││││├─┘ │  \033[0m")
        print("\033[96m└─┘└─┘┴ ┴┴ ┴┴ ┴┘└┘─┴┘  ┴  ┴└─└─┘┴ ┴┴   ┴  \033[0m")

    # Check if the user wants to automate a web browser
    elif user_input.lower() == "browser":
        while True:
            browser_command = input("Enter a browser automation command (e.g., open, search, quit): ").lower()

            if browser_command == "open":
                url = input("Enter the URL to open: ")
                webbrowser.open(url)

            elif browser_command == "search":
                query = input("Enter your search query: ")
                search_url = f"https://www.google.com/search?q={query}"
                webbrowser.open(search_url)

            elif browser_command == "quit":
                break
            else:
                print("Invalid browser automation command.")

    elif user_input.lower() == "hidden":
        while True:
            hidden_command = input("Enter a hidden browser command (e.g., google dork, close): ").lower()

            if hidden_command == "google dork":
                with open('Data/google_dorks.json', 'r') as json_file:
                    data = json.load(json_file)

                print("You selected Google Dork.")
                while True:
                    operator_choice = input("Choose a Google Dork operator (1-34, or 'exit' to go back): ")
                    if operator_choice.lower() == 'exit':
                        break
                    elif operator_choice.isdigit() and 1 <= int(operator_choice) <= 17:
                        operator_number = int(operator_choice)
                        selected_operator = data["operators"][str(operator_number)]
                        search_query = input(f"Enter your search term with the '{selected_operator}' operator: ")
                        full_query = f"{selected_operator}{search_query}"
                        print(f"Your Google Dork query: {full_query}")
                        webbrowser.open(f"https://www.google.com/search?q={full_query}")
                    else:
                        print("Invalid operator choice. Please choose a valid operator number.")

            elif hidden_command == "close":
                break
            else:
                print("Invalid hidden browser command. Please enter 'google dork' or 'close'.")
   
    # Check if the user wants to run penetration testing tools
    elif user_input.lower() == "penetration":
        with open('Data/kali_commands.json', 'r') as json_file:
            data = json.load(json_file)

        for command in command:
            try:
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError:
                print(f"Error running command: {command}")

    # Use subprocess to execute other commands
    else:
        try:
            subprocess.run(user_input, shell=True, check=True)
        except subprocess.CalledProcessError:
            print("Error: Command execution failed.")
