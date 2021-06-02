from nomics import Nomics
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import time

nomics = Nomics("API-KEY-HERE")


# Quick function for dealing with rounding prices

def get_rounded_float(number, decimals):
    return round(float(number), decimals)

while True:

    # Sets current time

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Gets current API Data

    data = nomics.Currencies.get_currencies(ids = "ETH,BTC,ETC")

    # Sets data to variables and rounds long number to the 2nd decimal

    btc_price = get_rounded_float(data[0]['price'], 2)
    eth_price = get_rounded_float(data[1]['price'], 2)
    etc_price = get_rounded_float(data[2]['price'], 2)

    # Puts all the data into an easy variable

    price=f"Bitcoin Price: {btc_price} USD\n\nEthereum Price: {eth_price} USD\n\nEthereum Classic Price: {etc_price} USD"

    # Embed for discord and execution

    embed = DiscordEmbed(title="Price at " + current_time, description=price)
    webhook = DiscordWebhook(url='WEBHOOK-LINK-HERE')
    webhook.add_embed(embed)
    response = webhook.execute()

    #Repeats every 10 seconds

    time.sleep(10)