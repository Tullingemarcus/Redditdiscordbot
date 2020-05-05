#essential discord imports
import discord
from discord.ext import commands

#imports for commands and reddit
import asyncio
import praw

#token import
from auth import token

#for shorting down code and adding prefix
client = commands.Bot(command_prefix = '¤')

#event when you start the bot
@client.event
async def on_ready():
    print("Bot is ready")
        
#ping command
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

#help command
@client.command()
async def helpme(ctx):
    await ctx.send("för att använda mig skriv in 'freegames'. Då kommer jag skicka en lista över de spel är gratis under de senaste sju dagarn. :)")

#discord command
@client.command()
async def freegames(ctx):
    reddit = praw.Reddit(client_id='3BqRqrMOaAKI9g',
                     client_secret='qClRMeV9jFOaOUv7AKOLaolpLGE', password='D1sc0rd02',
                     user_agent='discordreddit', username='discordbotonreddit')
                     
    for submission in reddit.subreddit('FreeGameFindings').top('week', limit=5):
        if submission.link_flair_css_class == 'Expired':
            pass
        else:
            await ctx.send(submission.title + submission.url)

#so that the code starts
if __name__ == "__main__":
    client.run(token)