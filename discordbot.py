import discord
import socket

ip = '127.0.0.1'
port = 2005

class MyClient(discord.Client):
    async def on_ready(self):
        print(self.user, "active")

    async def on_message(self, message):
        print(message.author, message.content)
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content.startswith("sendmessage"):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            f1 = (message.content + "PZ2W")
            result = f1.encode('utf_8')
            sock.send(result)
            sock.close()
        if message.content == "ping":
            await message.channel.send("pong")
        if message.content.startswith("talk"):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            author = message.author.name
            f1 = (author + ": "+ message.content + "TPZ0")
            result = f1.encode('utf_8')
            sock.send(result)
            sock.close()

client = MyClient()
client.run('DiscordBotToken')
