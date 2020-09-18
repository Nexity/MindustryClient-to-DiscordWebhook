import socket               # Import socket module
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File

webhook = Webhook.partial(
    "webhookID",
    "webhookToken",\
 adapter=RequestsWebhookAdapter())

soc = socket.socket()
host = "localhost"
port = 2004
soc.bind((host, port))
soc.listen(5)
while True:
    conn, addr = soc.accept()
    print ("Got connection from",addr)
    msg = conn.recv(1024)
    result = msg.decode("UTF-8")
    r2 = result.replace("@everyone", "@ everyone")
    r3 = r2.replace("@here", "@ here")
    if "DPrT" in r3:
        split = r3.split("DPrT")
        sender = split[0].split(']', 1)[1]
        message = split[1]
        print(sender, ":", message)
        webhook.send(sender + ": " + message)
    elif "PPRA" in r3:
        print(r3.replace("PPRA", ""))
        webhook.send(r3.replace("PPRA", ""))
        

