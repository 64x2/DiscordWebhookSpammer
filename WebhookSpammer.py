from discord_webhook import DiscordWebhook
import time
from colorama import Fore 

print(Fore.RED + " /$$      /$$           /$$       /$$                           /$$        /$$$$$$                                                                     ")
print(Fore.RED + "| $$  /$ | $$          | $$      | $$                          | $$       /$$__  $$                                                                    ")
print(Fore.RED + "| $$ /$$$| $$  /$$$$$$ | $$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$| $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$ ")
print(Fore.RED + "| $$/$$ $$ $$ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/|  $$$$$$  /$$__  $$ |____  $$| $$_  $$_  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$")
print(Fore.RED + "| $$$$_  $$$$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$/  \____  $$| $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$ \ $$ \ $$| $$$$$$$$| $$  \__/")
print(Fore.RED + "| $$$/ \  $$$| $$_____/| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$_  $$  /$$  \ $$| $$  | $$ /$$__  $$| $$ | $$ | $$| $$ | $$ | $$| $$_____/| $$      ")
print(Fore.RED + "| $$/   \  $$|  $$$$$$$| $$$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$/| $$$$$$$/|  $$$$$$$| $$ | $$ | $$| $$ | $$ | $$|  $$$$$$$| $$      ")
print(Fore.RED + "|__/     \__/ \_______/|_______/ |__/  |__/ \______/  \______/ |__/  \__/ \______/ | $$____/  \_______/|__/ |__/ |__/|__/ |__/ |__/ \_______/|__/      ")
print(Fore.RED + "                                                                                   | $$                                                                ")
print(Fore.RED + "                                                                                   | $$                                                                ")
print(Fore.RED + "                                                                                   |__/                                                                ")
print("")
print(Fore.BLUE + "Welcome to Webhook Spammer! Made by Xofo @ github.com/64x2/DiscordWebhookSpammer for free use.")

def spammer():
    url = input(Fore.GREEN + "Enter the webhook you would like to spam: \n> ")
    value = input(Fore.GREEN + "Enter what you would like to send to the webook: \n> ")
    times = int(input (Fore.GREEN + "Enter the amount of times you would like to send the message: \n> "))
    delay = int(input (Fore.GREEN + "Enter delay between messages in milliseconds, recomended to use 500ms or more: \n> "))
    username = input(Fore.GREEN + "Set the username of the webhook: \n> ")

    for i in range (times):
        webhook = DiscordWebhook(url=url, rate_limit_retry=True, content=f"{value}", username=f"{username}")
        response = webhook.execute()
        time.sleep(delay/1000)

if __name__ == "__main__": # Credit to @Invy55 for this area :^)
    spammer()
    while True:
        try:
            if "y" in input(Fore.GREEN + "Would you like to start over? (Y/N) \n").lower():
                spammer()
            else:
                break
        except KeyboardInterrupt:
            break
