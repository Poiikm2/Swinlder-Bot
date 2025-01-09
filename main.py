import discord
from discord.ext import commands
import os
import asyncio
import random

client = discord.Client()

#Welcome Users
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

bad_words = ["fuck", "Fuck", "Retard", "retard", "damn","sucks", "Sucks"]

meepodefense = ["You should be nicer to <@159985870458322944> !", "Be Nice!", "You should be nicer!", "Not nice Akudama....", "You sound like an executer...", "AKUDAMA!", "I'm calling cut-throat...", "(╯°□°）╯︵ ┻━┻  .........  ┬─┬ ノ( ゜-゜ノ)", "Poof!", "<@159985870458322944> is doing his best ok!", "(╯°□°）╯︵ ┻━┻  AKUDAMA!"]

mentionslist = ["<@!159985870458322944>", "<@!269705573795102720>"]

emoji = '\N{OCTAGONAL SIGN}'
#use emojipedia to find "unicode name"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if any(word in msg for word in bad_words) and any(word in msg for word in mentionslist):
        await message.channel.send(random.choice(meepodefense))
        
    elif "bitch" in message.content:
        await message.channel.send('Only Akudama say bad words, but I do love dogs')

        
    elif "ass" in message.content:
        await message.channel.send('Stop looking at mine!')

        
    elif "whore" in message.content:
        await message.channel.send('Like your mom? #Swindled')


    elif "damn" in message.content:
        await message.channel.send('Like what the beavers live in?')

        
    elif "shit" in message.content:
        await message.channel.send('You know, you can just go, No need to act like an Akudama')


    elif "Bitch" in message.content:
        await message.channel.send('Only Akudama say bad words, but I do love dogs')

        
    elif "Ass" in message.content:
        await message.channel.send('Stop looking at mine!')

        
    elif "Whore" in message.content:
        await message.channel.send('Like your mom? #Swindled')


    elif "Damn" in message.content:
        await message.channel.send('Like what the beavers live in?')

        
    elif "Shit" in message.content:
        await message.channel.send('You know, you can just go, No need to act like an Akudama')

    #Welcome Users Entry
    @bot.event
    async def on_member_join(member):
        channel = member.guild.system_channel  # Use the default system channel
        if channel is not None:
        await channel.send(f"Welcome to the server, {member.mention}!")


    if any(word in msg for word in bad_words):
        await message.add_reaction(emoji)


client.run(os.getenv('TOKEN'))

