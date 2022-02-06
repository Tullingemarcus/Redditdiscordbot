# Redditdiscordbot
## Requirements
**Required libraries**
* PRAW
* discord.py

### PRAW
PRAW is short for Python Reddit API Wrapper and is a python package that allows for simple access to reddit's API. <br>
For more information about how to install and use PRAW follow this link https://praw.readthedocs.io/en/stable/

### discord.py
discord.py is an API wrapper for Discord that is modern, easy to use, feature-rich, and async ready <br>
For more information about how to install and use discord.py follow this link https://discordpy.readthedocs.io/en/stable/

## Commands
In freegamesbot.py I have used a prefix of "¤", this symbol however can be changed to anything or even removed entirely. The prefix indicates that a commands need to have that symbol at the start to be considered a command. <br>
The commands are as following: <br>

* helpme

Sends out a message on how to use the main command

* ping

This command just checks if the bot have connection to the discord server

* freegames

Sends out a list of five games from the last seven days from the subreddit [```FreeGameFindings```](https://www.reddit.com/r/FreeGameFindings/)

These commands can be changed and there is possibility to add commands in the code