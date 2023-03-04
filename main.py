from dotenv import load_dotenv
import os
import discord
import re
def ListToString(inString):
    emptyString = ""
    for x in inString:
        emptyString += x
    return emptyString

# Bot key
load_dotenv()
TOKEN = os.environ['ENVTOKEN']
# Permissions of bot in server that it's added to
intents = discord.Intents.default()
intents.message_content = True
intents.emojis = True
intents.reactions = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    # Checks if message is sent by bot, avoid accidental recursive calls
    if message.author == client.user:
        return
    # Check if first word in message string is keyword
    if message.content.startswith("poll:") or message.content.startswith("Poll:"):
        # Assign new string to 'emotes', message.content remains unaltered
        emotes = message.content.split('"',3)[2].split()
        # Isolate the substring question from the input string
        question = ListToString(re.findall('"([^"]*)"', str(message.content)))
        # Concatenate string to send as bot (User who intialized bot, their question)
        toSendString = str(message.author).split("#",1)[0] + " asks: " + question
        # Prepare message to send
        msg = await message.channel.send(toSendString)
        # Add reactions to message sent by bot
        for i in emotes:
            await msg.add_reaction(i)
client.run(TOKEN)
