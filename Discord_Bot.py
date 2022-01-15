import discord # I used the discord.py library therefore i need to import it by typing in "import discord"
import os # used so that the token can run in the main file 
import requests # this module allows the code to make a HTTP request to get data form the API
import json # the API will then return JSON so that it will make it easier to work with the data when it's returned
import random # import a random module because the bot will choose a random starter encouragement
from replit import db # replit's built in database to store user submitted messages  
from keep_alive import keep_alive # to make sure our bot keeps running even though we close our tab
# create an .env file on replit to save the token to prevent it from being shared
my_secret = os.environ['token'] # to get the token, go to the discord developer website, go to your application and press the Bot tab then copy the token

intents = discord.Intents.default() # got to pass the intent after it is turned on from the bot setting in the discord developer website
intents.members = True
client = discord.Client(intents = intents) # create an instance of a client and it is part of the discord.py library, this is going to be the connection to discord 

sad_words = ["sad", "depressed", "unhappy", "miserable", "depressing", "lost", "rough"] # create a variable and put it in sad words 

starter_encouragements = ["Cheer up!", "Hang in there :)", "You got this!", "You are a great person :)", "We are here for you <3", "Care to share?"] # make a variable and put it starter encouragements to be used to repsond to sad words

if "responding" not in db.keys(): # new key in the database 
  db["responding"] = True # start off as true

def get_quote(): # helper function that we can call to return a quote from the API
  response = requests.get("https://zenquotes.io/api/random") # zenquotes.io API will generate random inspirational quotes, used the request module to request data from the API URL
  json_data = json.loads(response.text) #convert the response in JSON
  quote = json_data[0]["q"] + " -" + json_data[0]["a"] # getting the quote out from JSON
  return quote # return the quote as a message on discord

def update_encouragements(encouraging_message): # make a function that will update encouragments to the database 
  if "encouragements" in db.keys(): # check if encouragements is a key in the database 
    encouragements = db["encouragements"] # get the value form the database stored under a certain key
    encouragements.append(encouraging_message) # add new encouraging message to the list
    db["encouragements"] = encouragements # after we add the new encouraging message to the old encouraging message we need to save it to the database
  else:
    db["encouragements"] = [encouraging_message] 

def delete_encouragements(index): # a fucntion that will delet any added new encouragements
  encouragements = db["encouragements"] # list all the messages from the database 
  if len(encouragements) > index: # check if the lenght of encouragements is more than the index 
    del encouragements[index] # if it is more then we are going to delete
    db["encouragements"] = encouragements # save it into the database again

@client.event # used a client.event decorator to register an event, this client uses events to make it work 
async def on_ready(): # this is also an asynchronous library on discord.py so things are done in call backs, a callback is a function that is called when something else happens, so the on_ready event is going to be called when the bot is ready to be used
    print(f"{client.user.name} has connected to Discord!") # when the bot is ready it's going to print in the console

@client.event # register event 
async def on_member_join(member): # name of the event 
  guild = client.get_guild(930561768974073936) # get the server id so the bot knows which server its gonna welcome the new member in
  channel = guild.get_channel(930561768974073940) # get the channel id so the bot knows which channel its gonna welcome the new member in
  await channel.send(f"Welcome to the server {member.mention} ! :partying_face: Please type in 'help' so that I may assist you.") # the message that will be sent in the server
  await member.send(f"Welcome to {guild.name}'s server, {member.name}! :partying_face:") # the message that will be sent through private message

@client.event # register an event
async def on_message(message): # this on_message event triggers each time a message is recieved  
  if message.author == client.user: # we don't want it to do anything if the message is from ourselves, so we check using this line
    return

  guild = client.get_guild(930561768974073936) # get the server id 
  if message.content.startswith("users"):
      await message.channel.send(f"Number of Members in this Server: {guild.member_count}") # it will count the number of users in this particular server 

# embedding all the commands into one clean table
  if message.content.startswith("help"): # if the user types help a list of commands will be presented in an embedded table
        embed = discord.Embed(title = "Help on BOT", description = "Some useful commands (please type with all lowercase or uppercase letters)")
        embed.add_field(name = "hello, hi, hey, hai, yo", value = "Greets the user")
        embed.add_field(name = "wassup", value = "Bot tells you what's up")
        embed.add_field(name = "how are you, how r u, hru", value = "Bot replies with how they're feeling")
        embed.add_field(name = "aw", value = "Bot loves you")
        embed.add_field(name = "users", value = "Prints out the number of people in the server")
        embed.add_field(name = "thanks, thx", value = "The bot is glad to be of help")
        embed.add_field(name = "i love you, i love u, i luv u, ily, ilu", value = "The bot will send love")
        embed.add_field(name = "wish me luck", value = "The bot bids you good luck")
        embed.add_field(name = "lol, lmao, haha, lmfao", value = "The bot laughs along")
        embed.add_field(name="inspire", value = "Prints out random inspirational quotes")
        embed.add_field(name="congrats", value = "Congratulates the user")
        embed.add_field(name = "responding true", value = "Turns on encouraging bot response")
        embed.add_field(name = "responding false", value = "Turns off encouraging bot response")
        embed.add_field(name = "new", value = "Used to add new encouragements")
        embed.add_field(name = "list", value = "Shows a list of newly added encouragements")
        embed.add_field(name = "del", value = "Used to delete newly added encouragements")
        await message.channel.send(content=None, embed=embed)

# make up commands for the users to type in and what will the discord bot respond in return
  if message.content.startswith("hello"):
    await message.channel.send("Hello there, how are you doing ?")

  if message.content.startswith("HELLO"):
    await message.channel.send("Hello there, how are you doing ?")

  if message.content.startswith("hi"):
    await message.channel.send("Hello there, how are you doing ?")

  if message.content.startswith("HI"):
    await message.channel.send("Hello there, how are you doing ?")

  if message.content.startswith("hey"):
    await message.channel.send("Hello there, how are you doing ?")

  if message.content.startswith("hai"):
    await message.channel.send("Hello there, how are you doing ?")

  if message.content.startswith("HAI"):
    await message.channel.send("Hello there, how are you doing ?")

  if message.content.startswith("yo"):
    await message.channel.send("Hello there, how are you doing ?")

  if message.content.startswith("YO"):
    await message.channel.send("Hello there, how are you doing ?")

  if message.content.startswith("wassup"):
    await message.channel.send("The sky lol")

  if message.content.startswith("WASSUP"):
    await message.channel.send("The sky lol")

  if message.content.startswith("how are you"):
    await message.channel.send("Good now that you're here")
  
  if message.content.startswith("HOW ARE YOU"):
    await message.channel.send("Good now that you're here")

  if message.content.startswith("how r u"):
    await message.channel.send("Good now that you're here")
  
  if message.content.startswith("HOW R U"):
    await message.channel.send("Good now that you're here")

  if message.content.startswith("hru"):
    await message.channel.send("Good now that you're here")
  
  if message.content.startswith("HRU"):
    await message.channel.send("Good now that you're here")

  if message.content.startswith("aw"):
    await message.channel.send(":smiling_face_with_3_hearts:")

  if message.content.startswith("AW"):
    await message.channel.send(":smiling_face_with_3_hearts:")
    
  if message.content.startswith("inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith("INSPIRE"):
    quote = get_quote() 
    await message.channel.send(quote)

  if message.content.startswith("congrats"):
    await message.channel.send("Congratulations! 🎉")

  if message.content.startswith("CONGRATS"):
    await message.channel.send("Congratulations! 🎉")

  if message.content.startswith("thanks"):
    await message.channel.send("The pleasure is all mine")

  if message.content.startswith("THANKS"):
    await message.channel.send("The pleasure is all mine")

  if message.content.startswith("thx"):
    await message.channel.send("The pleasure is all mine")

  if message.content.startswith("THX"):
    await message.channel.send("The pleasure is all mine")

  if message.content.startswith("wish me luck"):
    await message.channel.send("Good Luck! :muscle: :star_struck:")

  if message.content.startswith("WISH ME LUCK"):
    await message.channel.send("Good Luck! :muscle: :star_struck:")

  if message.content.startswith("i love you"):
    await message.channel.send("I love you more!!")

  if message.content.startswith("I LOVE YOU"):
    await message.channel.send("I love you more!!")  

  if message.content.startswith("i luv you"):
    await message.channel.send("I love you more!!")

  if message.content.startswith("I LUV YOU"):
    await message.channel.send("I love you more!!")

  if message.content.startswith("i love u"):
    await message.channel.send("I love you more!!")

  if message.content.startswith("I LOVE U"):
    await message.channel.send("I love you more!!")

  if message.content.startswith("ily"):
    await message.channel.send("I love you more!!")

  if message.content.startswith("ILY"):
    await message.channel.send("I love you more!!")

  if message.content.startswith("ilu"):
    await message.channel.send("I love you more!!")

  if message.content.startswith("ILU"):
    await message.channel.send("I love you more!!")

  if message.content.startswith("lol"):
    await message.channel.send(":rofl:")

  if message.content.startswith("LOL"):
    await message.channel.send(":rofl:")

  if message.content.startswith("lmao"):
    await message.channel.send(":rofl:")

  if message.content.startswith("LMAO"):
    await message.channel.send(":rofl:")

  if message.content.startswith("lmfao"):
    await message.channel.send(":rofl: :rofl:")
  
  if message.content.startswith("LMFAO"):
    await message.channel.send(":rofl: :rofl:")

  if message.content.startswith("haha"):
    await message.channel.send(":rofl:")

  if message.content.startswith("HAHA"):
    await message.channel.send(":rofl:")

  if db["responding"]: # if its true then it will respond to the sad words 
    options = starter_encouragements # create a new variable
    if "encouragements" in db.keys(): # if there is any encouragement in the database 
      options = options + list(db["encouragements"]) # add them to the options of starter encouragements 

  if any(word in message.content for word in sad_words): # if the bot detects any of the words listed in sad words appear
    await message.channel.send(random.choice(options)) # send a random starter encouragements

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
    value = message.content.split("responding ", 1)[1] # get the value that the user typed in

    if value.lower() == "true": # if its true then the bot will repsond to sad words
      db["responding"] = True
      await message.channel.send("Responding is on.")
    if value.lower() == "false": # if its true then the bot will not repsond to sad words
      db["responding"] = False
      await message.channel.send("Responding is off.")

keep_alive() # this will run our web server     
client.run(os.getenv("token")) # using import os we are running our bot using the token from the .env file through replit