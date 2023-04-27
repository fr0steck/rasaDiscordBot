import discord
import requests

INTERPRETER_URL = "http://localhost:5005/webhooks/rest/webhook"
BOT_TOKEN = "MTEwMTIyNzQ3MDM5ODcwMTU4OQ.GWDFtC.ThkYQYJ3hWGgkJKJZAtoxl0l4KBozdzCzVK8Zc"


# Set the intents you want to use
intents = discord.Intents().all()

# Create the client with the intents
client = discord.Client(intents=intents)

def interprete(message):
    data = {"sender": "user", "message": message}
    response = requests.post(INTERPRETER_URL, json=data)
    response_json = response.json()
    if response_json:
        text = response_json[0].get("text", "")
        return text
    return ""

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Send the message to the Rasa server for interpretation
    response = interprete(message.content)

    # Send the response back to the Discord chat
    await message.channel.send(response)

client.run(BOT_TOKEN)

