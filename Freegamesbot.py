#essential discord imports
import discord
from discord.ext import commands

#imports for commands and reddit
import asyncio
import praw

#importing necessary variables from auth
from auth import token, PASSWORD, secret, Id, name

#for shorting down code and adding prefix
client = commands.Bot(command_prefix = '¤')

#event when you start the bot
@client.event
async def on_ready():
    print("Bot is ready")
        
#ping command to check if bot has connection to discord
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

#help command
@client.command()
async def helpme(ctx):
    await ctx.send("för att använda mig skriv in 'freegames'. Då kommer jag skicka en lista över de fem bästa spelen som är gratis under de senaste sju dagarn. :)")

#discord command
@client.command()
async def freegames(ctx):
    #Personal variables is found under auth.py
    #user_agent can be anything in this case i have named it "discordreddit"
    reddit = praw.Reddit(client_id=Id,
                     client_secret=secret, password=PASSWORD,
                     user_agent='discordreddit', username=name)

    #checking which timeframe should be checked and how many post in that timeframe should be checked
    for submission in reddit.subreddit('FreeGameFindings').top('week', limit=5):
        #checking if the post have flair "expired" and ignoring if it have
        if submission.link_flair_css_class == 'Expired':
            pass
        else:
            await ctx.send(submission.title + submission.url)

#main function
if __name__ == "__main__":
    client.run(token)