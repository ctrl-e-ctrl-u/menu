import subprocess

def backupScript():
    print("Simulating execution of backupScript.py script")
    # subprocess.run(['python3', '/home/Network-team/scripts/backupScript.py'])

def inventoryScript():
    print("Simulating execution of inventoryScript.py script")
    # subprocess.run(['python3', '/home/Network-team/scripts/inventoryScript.py'])

def exitProgram():
    print("Exiting. have fun at the lake!")
    exit()

optionsMenu = {
    "1": ("Backup Device", backupScript),
    "2": ("Pull Inventory inventoryScript", inventoryScript),
    "3": ("Exit", exitProgram),
}

def printOfMenu():
    print("\n--- Network Automation Menu ---")
    for key, (desc, _) in optionsMenu.items():
        print(f"{key}. {desc}")

def main():
    while True:
        printOfMenu()
        choice = input("Select an option: ").strip()
        if choice in optionsMenu:
            optionsMenu[choice][1]()  # call the function
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
