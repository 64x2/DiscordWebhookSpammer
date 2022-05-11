from discord_webhook import DiscordWebhook
import time
url = input("Enter what webook to spam:\n> ")
value = input("Enter what you would like to send to the webook:\n> ")
times = int(input("Enter the amount of times you would like to send the message:\n> "))
delay = int(input("Enter delay between messages in milliseconds:\n> "))

for i in range(times):
    webhook = DiscordWebhook(url=url, content=f"{value}")
    response = webhook.execute()
    time.sleep(delay/1000)