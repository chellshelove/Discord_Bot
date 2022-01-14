import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
my_secret = os.environ['token']

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

sad_words = ["sad", "depressed", "unhappy", "miserable", "depressing", "lost", "rough"]

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
    print(f"{client.user.name} has connected to Discord!")

@client.event
async def on_member_join(member):
  guild = client.get_guild(930561768974073936)
  channel = guild.get_channel(930561768974073940)
  await channel.send(f"Welcome to the server {member.mention} ! :partying_face: Please type in 'help' so that I may assist you")
  await member.send(f"Welcome to {guild.name}'s server, {member.name}! :partying_face:")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  guild = client.get_guild(930561768974073936)
  if message.content.startswith("users"):
      await message.channel.send(f"Number of Members in this Server: {guild.member_count}")

  if message.content.startswith("help"):
        embed = discord.Embed(title = "Help on BOT", description = "Some useful commands (please type with lowercase letters)")
        embed.add_field(name = "hello, hi, hey, hai, yo", value = "Greets the user")
        embed.add_field(name = "wassup", value = "bot tells you what's up")
        embed.add_field(name = "how are you, how r u, hru", value = "bot replies with how they're feeling")
        embed.add_field(name = "aw", value = "bot loves you")
        embed.add_field(name = "users", value = "Prints out the number of people in the server")
        embed.add_field(name = "thanks, thx", value = "The bot is glad to be of help")
        embed.add_field(name = "lol, lmao", value = "The bot laughs along")
        embed.add_field(name="inspire", value = "Prints out random inspirational quotes")
        embed.add_field(name="congrats", value = "congratulates the user")
        embed.add_field(name = "responding true", value = "turns on encouraging bot response")
        embed.add_field(name = "responding false", value = "turns off encouraging bot response")
        embed.add_field(name = "new", value = "used to add new encouragements")
        embed.add_field(name = "list", value = "shows a list of newly added encouragements")
        embed.add_field(name = "del", value = "used to delete newly added encouragements")
        await message.channel.send(content=None, embed=embed)

  if message.content.startswith("hello"):
    await message.channel.send("Hello there")

  if message.content.startswith("hi"):
    await message.channel.send("Hello there")

  if message.content.startswith("hey"):
    await message.channel.send("Hello there")

  if message.content.startswith("hai"):
    await message.channel.send("Hello there")

  if message.content.startswith("yo"):
    await message.channel.send("Hello there")

  if message.content.startswith("wassup"):
    await message.channel.send("The sky lol")

  if message.content.startswith("how are you"):
    await message.channel.send("Good now that you're here")

  if message.content.startswith("how r u"):
    await message.channel.send("Good now that you're here")

  if message.content.startswith("hru"):
    await message.channel.send("Good now that you're here")

  if message.content.startswith("aw"):
    await message.channel.send(":smiling_face_with_3_hearts:")

  if message.content.startswith("AW"):
    await message.channel.send(":smiling_face_with_3_hearts:")
    
  if message.content.startswith("inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith("congrats"):
    await message.channel.send("Congratulations! 🎉")

  if message.content.startswith("thanks"):
    await message.channel.send("The pleasure is all mine")

  if message.content.startswith("thx"):
    await message.channel.send("The pleasure is all mine")

  if message.content.startswith("lol"):
    await message.channel.send(":rofl:")

  if message.content.startswith("LOL"):
    await message.channel.send(":rofl:")

  if message.content.startswith("lmao"):
    await message.channel.send(":rofl:")

  if message.content.startswith("LMAO"):
    await message.channel.send(":rofl:")

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