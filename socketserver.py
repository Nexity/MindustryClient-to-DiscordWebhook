import socket
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File

webhook = Webhook.partial(
    "wbehookID",
    "webhookToken",\
 adapter=RequestsWebhookAdapter())

soc = socket.socket()
host = "localhost"
port = 2004
soc.bind((host, port))
soc.listen(5)
while True:
    try:
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
            webhook.send("```java\n" + sender + ": " + message + "```")
        if "PPRA" in r3:
            print(r3.replace("PPRA", ""))
            webhook.send("```java\n" + r3.replace("PPRA", "") + "```")
        if "PDDT" in r3:
            print(r3.replace("PDDT", ""))
            webhook.send("```java\n" + r3.replace("PDDT", "") + "```")
        if "PDDA" in r3:
            webhook.send("<@&756493233718165545> \n ```java\n" + r3.replace("PDDA", "") + "```")
        if "CPJS" in r3:
            webhook.send("```java\nBot joined```")
        if "CPDS" in r3:
            webhook.send("```java\nBot left```")
    except:
        print("Some kind of error occured")
        

