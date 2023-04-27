import discord
import requests

INTERPRETER_URL = "http://localhost:5005/model/parse"
BOT_TOKEN = "MTEwMTIyNzQ3MDM5ODcwMTU4OQ.GWDFtC.ThkYQYJ3hWGgkJKJZAtoxl0l4KBozdzCzVK8Zc"


# Set the intents you want to use
intents = discord.Intents().all()

# Create the client with the intents
client = discord.Client(intents=intents)


def interprete(message):
    data = f'{{"text":"{message}"}}'
    response = requests.post(INTERPRETER_URL, data=data)
    return response.json()

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

    # Get the intent and confidence from the response
    intent = response["intent"]["name"]
    confidence = response["intent"]["confidence"]

    # Send the response back to the Discord chat
    await message.channel.send(f"{message.author.mention}: Rasa interpreted your message as '{intent}' with confidence {confidence}")

client.run(BOT_TOKEN)

