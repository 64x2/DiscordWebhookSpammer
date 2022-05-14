from discord_webhook import DiscordWebhook
import time

print("Webhook Spammer by xofo#1749, educational purposes only!")
print("github.com/64x2/DiscordWebhookSpammer\n")

def spammer():
    url = input("Enter the webhook you would like to spam: \n> ")
    value = input("Enter what you would like to send to the webook: \n> ")
    times = int(input ("Enter the amount of times you would like to send the message: \n> "))
    delay = int(input ("Enter delay between messages in milliseconds, recomended to use 500ms or more: \n> "))

    for i in range (times):
        webhook = DiscordWebhook(url=url, rate_limit_retry=True, content=f"{value}")
        response = webhook.execute()
        time.sleep(delay/1000)

if __name__ == "__main__": # Credit to @Invy55 for this area :^)
    spammer()
    while True:
        try:
            if "y" in input("Would you like to start over? (Y/N) \n").lower():
                spammer()
            else:
                break
        except KeyboardInterrupt:
            break
