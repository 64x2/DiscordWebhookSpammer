from discord_webhook import DiscordWebhook
import time

print("Webhook Spammer by xofo#1749, educational purposes only!")
print("github.com/64x2/DiscordWebhookSpammer\n")

url = input("Enter the webook you would like to spam:\n> ")
value = input("Enter what you would like to send to the webook:\n> ")
times = int(input("Enter the amount of times you would like to send the message:\n> "))
delay = int(input("Enter delay between messages in milliseconds, reccomended to use 500ms or more:\n> "))

for i in range(times):
    webhook = DiscordWebhook(url=url, rate_limit_retry=True, content=f"{value}")
    response = webhook.execute()
    time.sleep(delay/1000)
