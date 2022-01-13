import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
my_secret = os.environ['token']

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "miserable", "depressing"]

starter_encouragements = ["Cheer up!", "Hang in there :)", "You got this!", "You are a great person :)", "We are here for you <3", "Care to share?"]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return quote

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragements(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("help"):
        embed = discord.Embed(title = "Help on BOT", description = "Some useful commands")
        embed.add_field(name = "hello", value = "Greets the user")
        embed.add_field(name="inspire", value = "Prints out random inspirational quotes")
        embed.add_field(name="congrats", value = "congratulates the user")
        embed.add_field(name = "responding true", value = "turns on bot response")
        embed.add_field(name = "responding false", value = "turns off bot response")
        embed.add_field(name = "new", value = "used to add new encouragements")
        embed.add_field(name = "list", value = "shows a list of newly added encouragements")
        embed.add_field(name = "del", value = "used to delete newly added encouragements")
        await message.channel.send(content=None, embed=embed)

  if message.content.startswith("hello"):
    await message.channel.send("Hello there")
    
  if message.content.startswith("inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith("congrats"):
    await message.channel.send("Congratulations! 🎉")

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + list(db["encouragements"])

  if any(word in message.content for word in sad_words):
    await message.channel.send(random.choice(options))

  if message.content.startswith("new"):
    encouraging_message = message.content.split("new ", 1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if message.content.startswith("del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(message.content.split("del", 1)[1])
      delete_encouragements(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if message.content.startswith("list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    
  if message.content.startswith("responding"):
    value = message.content.split("responding ", 1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    if value.lower() == "false": 
      db["responding"] = False
      await message.channel.send("Responding is off.")

keep_alive()        
client.run(os.getenv("token"))