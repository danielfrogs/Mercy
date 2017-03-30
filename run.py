import discord
import asyncio
import json

client = discord.Client()

@client.event
async def on_ready():
    """This prints that the bot has started"""
    print("Mercy is online!")

@client.event
async def on_message(message):
    if message.content.lower() == ("~hi"):
        await client.send_message(message.channel, "Hello " + message.author.mention + ", my name is Mercy!")
        #message.channel sends the message to the channel in which the string entered was detected
        #message.author.mention mentions the person who sent the message to Mercy
    # We use an elif  here to only check if the command is help if the hi command wasn't issued.
    elif message.content.lower() == ("~help"):
        await client.send_message(message.channel, message.author.mention + ", sending some help now!")

if __name__ == "__main__":
    #The Discord Bot token is loaded from the config file
    try:
        with open("config.json", mode="r") as config_file:
            token = json.load(config_file)["token"]
            assert type(token) == str
    except (IOError, json.JSONDecodeError, KeyError):
        print("Config file was unable to load successfully")
        exit()
    client.run(token)
    print("Mercy is offline!")

