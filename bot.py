import json
import os
import time

import tweepy

global time, up, down
# local time settings
os.environ["TZ"] = "Turkey"
time = time.strftime("%d-%m-%Y %H:%M")
up = "⬆️"
down = "⬇️"


def btc():
    # BTC twitter account key and tokens
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    login = tweepy.OAuthHandler(consumer_key, consumer_secret)
    login.set_access_token(access_token, access_token_secret)
    api = tweepy.API(login)

    with open("ticker.json") as json_data:
        data = json.load(json_data)
        current = str(data["BTC"]["current"])
        change_a = str(float(data["BTC"]["change_amount"]))
        change = str(data["BTC"]["change_percentage"])

        if change[0:1] == "-":
            api.update_status(
                status="#BTC: " + current + "TL" + up + "(-" + change_a + ")\n" + time
            )
        elif change == "0":
            api.update_status(
                status="#BTC: " + current + "TL" + "(" + change_a + ")\n" + time
            )
        else:
            api.update_status(
                status="#BTC: " + current + "TL" + down + "(+" + change_a + ")\n" + time
            )


def eth():
    # ETH twitter account key and tokens
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    login = tweepy.OAuthHandler(consumer_key, consumer_secret)
    login.set_access_token(access_token, access_token_secret)
    api = tweepy.API(login)

    with open("ticker.json") as json_data:
        data = json.load(json_data)
        current = str(data["ETH"]["current"])
        change_a = str(float(data["ETH"]["change_amount"]))
        change = str(data["ETH"]["change_percentage"])

        if change[0:1] == "-":
            api.update_status(
                status="#ETH: " + current + "TL" + up + "(-" + change_a + ")\n" + time
            )
        elif change == "0":
            api.update_status(
                status="#ETH: " + current + "TL" + "(" + change_a + ")\n" + time
            )
        else:
            api.update_status(
                status="#ETH: " + current + "TL" + down + "(+" + change_a + ")\n" + time
            )


def ltc():
    # LTC twitter account key and tokens
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    login = tweepy.OAuthHandler(consumer_key, consumer_secret)
    login.set_access_token(access_token, access_token_secret)
    api = tweepy.API(login)

    with open("ticker.json") as json_data:
        data = json.load(json_data)
        current = str(data["LTC"]["current"])
        change_a = str(float(data["LTC"]["change_amount"]))
        change = str(data["LTC"]["change_percentage"])

        if change[0:1] == "-":
            api.update_status(
                status="#LTC: " + current + "TL" + up + "(-" + change_a + ")\n" + time
            )
        elif change == "0":
            api.update_status(
                status="#LTC: " + current + "TL" + "(" + change_a + ")\n" + time
            )
        else:
            api.update_status(
                status="#LTC: " + current + "TL" + down + "(+" + change_a + ")\n" + time
            )

if __name__ == "__main__":
    btc()
    eth()
    ltc()
