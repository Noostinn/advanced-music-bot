import discord
from discord.ext import commands

import os

#import all of the cogs
from main_cog import main_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='!')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(main_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with token
bot.run("YOUR TOKEN HERE")