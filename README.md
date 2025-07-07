# Network Automation Menu Launcher

A simple Python-based CLI menu to organize and run your network automation scripts easily. Perfect for network engineers looking to centralize and simplify their automation toolkit!

---

## Features

- Interactive menu to select and run automation tasks
- Easily extendable by adding new scripts
- Placeholder commands to simulate script execution
- Designed for network device backups, inventory pulls, and more

---

## Getting Started

### Prerequisites

- Python 3.6 or higher
- (Optional) Install dependencies if your scripts require libraries like `netmiko`, `napalm`, etc.
- Uncomment the " # subprocess.run(['python3', '/home/Network-team/scripts/backupScript.py'])" line and replace the repo with the repo where your scripts exist, example "/home/user/scripts"

----

## More add ons?

To add in more scripts simply add the additonal option to optionsMenu, example


optionsMenu = {
    "1": ("Backup Device", backupScript),
    "2": ("Pull Inventory inventoryScript", inventoryScript),
    "3": ("Script3 thirdScript", thirdScript),
    "4": ("Script4 fourthScript", fourthScript),
    "5": ("Exit", exitProgram),
}

Then add in additional function to add in your addtional scripts, example

def thirdScript():
    # subprocess.run(['python3', 'home/Network-team/scripts/thirdScript.py'])

def fourthScript():
    # subprocess.run(['python3', 'home/Network-team/scripts/fourthScript.py'])



