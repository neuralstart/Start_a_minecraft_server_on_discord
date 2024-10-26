import discord
import subprocess
import os

TOKEN = ""
SERVER_PATH = r"PATH"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

server_process = None

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    global server_process
    if message.content.startswith("/start"):
        server_process = start_server()
        await message.channel.send("Minecraft server is up and running!")
    elif message.content.startswith("/stop"):
        if server_process is not None and server_process.poll() is None:
            stop_server(server_process)
            await message.channel.send("Minecraft server has been shut down.")
            server_process = None
        else:
            await message.channel.send("Server is already down.")

def start_server():
    return subprocess.Popen([SERVER_PATH])

def stop_server(process):
    process.terminate() 

client.run(TOKEN)
