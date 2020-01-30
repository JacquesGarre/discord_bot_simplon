# Liste d'import
import os
import datetime as mDate
import bot_retards  
import discord
from dotenv import load_dotenv

import logs

#load_dot_env
load_dotenv()

# Creation du bot
bot = discord.Client()

# Chargement du bot
os.system('cls' if os.name == 'nt' else 'clear')
print('Chargement du programme \n')

# Création des événements
@bot.event
async def on_ready():
    os.system('cls' if os.name=='nt' else 'clear')

# on user message
@bot.event
async def on_message(message):
        if message.author == bot.user:
            pass
        else:
            await bot_retards.bot_retards_function(message)

@bot.event
async def on_error(p_error):
    er_date = mDate.datetime.now()
    error_log = 'ERROR : {}'.format(p_error)
    logs.Full(er_date,error_log)

# Lancement du bot
bot.run(os.getenv('DISCORD_TOKEN'))