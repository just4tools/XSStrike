import os
import subprocess
#########################
Green="\033[1;33m"
Blue="\033[1;34m"
Reset="\033[0m"
Red="\033[1;31m"
pink = "\033[95m"
#########################
os.system("clear")
print("")
print(
"""                     \033[36m/$$   /$$  /$$$$$$   /$$$$$$   \033[1;33m/$$               /$$ /$$                \033[0m
                    \033[36m| $$  / $$ /$$__  $$ /$$__  $$ \033[1;33m| $$              |__/| $$                \033[0m
                    \033[36m|  $$/ $$/| $$  \__/| $$  \__/\033[1;33m/$$$$$$    /$$$$$$  /$$| $$   /$$  /$$$$$$ \033[0m
                     \033[36m\  $$$$/ |  $$$$$$ |  $$$$$$\033[1;33m|_  $$_/   /$$__  $$| $$| $$  /$$/ /$$__  $$\033[0m
                      \033[36m>$$  $$  \____  $$ \____  $$ \033[1;33m| $$    | $$  \__/| $$| $$$$$$/ | $$$$$$$$\033[0m
                     \033[36m/$$/\  $$ /$$  \ $$ /$$  \ $$ \033[1;33m| $$ /$$| $$      | $$| $$_  $$ | $$_____/\033[0m
                    \033[36m| $$  \ $$|  $$$$$$/|  $$$$$$/ \033[1;33m|  $$$$/| $$      | $$| $$ \  $$|  $$$$$$$\033[0m
                    \033[36m|__/  |__/ \______/  \______/   \033[1;33m\___/  |__/      |__/|__/  \__/ \_______/  \033[0m """
)
print("")
url = input("" + Reset + "[" + Blue + "ENTER " + Red + "The " + Green + "Domain " + pink + "To Test" + Reset + "]" + Green + ": " + Reset)
subprocess.check_call(['python3', './tools/XSStrike/xsstrike.py', '-u', url])
