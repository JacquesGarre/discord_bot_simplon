# coding: utf-8
import os
import mysql.connector 
from dotenv import load_dotenv
import discord

load_dotenv()

verbs = {
    'a_apporté' : ['riz', 'cafe_senseo', 'cafe_filtre','the','eponge','liquide_vaiselle'], 
    'est_en' : ['retard'], 
    'a_lavé' : ['torchons','micro_ondes']
}

def db_connect():
    db = mysql.connector.connect(
        host = os.getenv('DB_HOST'), 
        user = os.getenv('DB_USER'), 
        password = os.getenv('DB_PASSWORD'),
        database = os.getenv('DB_NAME')
    )
    return db

def version():
    return 'Version {}'.format(os.getenv('BOT_VERSION'))

def env():
    return '{}'.format(os.getenv('ENV'))

def help():
    help_message = 'Les commandes possibles sont:\n'
    if os.getenv('ENV') == 'DEV':
        help_message += '**!env**: *Retourne l\'environnement*\n'
        help_message += '**!version**: *Retourne la version*\n'
    help_message += '**!liste**: *Retourne la liste des apprenants*\n'
    help_message += '**!cmd**: *Retourne la liste des commandes*\n'
    return help_message

async def show_list(message):
    response = "Pour voir la liste des apprenants, rendez-vous sur ce lien! :point_down:\n"
    response += os.getenv('SITE_URL')
    await message.channel.send(response)

def pseudo_format(pseudo):
    while len(pseudo) <= 14:
        pseudo += ' '
    return pseudo

def int_format(value):
    value = str(value)
    return value

def get_pseudo(message):
    return message.mentions[0].nick if message.mentions[0].nick is not None else message.mentions[0].name

def show_commands():
    response = "\n\n\n"
    for verb, mots in verbs.items():
        response += "**" + verb + "** : "
        for mot in mots:
            response += mot + ', '
        response += '\n'
    response += "\nExemples : @bob a_apporté cafe_senseo, @john a_lavé torchons"
    return response

async def bot_retards_function(message):
    if message.channel.id == os.getenv('CHANNEL_ID'):
        if message.content == "!version":
            response = version()
            await message.channel.send(response)
        elif message.content == "!env":
            response = env()
            await message.channel.send(response)
        elif message.content == "!help":
            response = help()
            await message.channel.send(response)
        elif message.content == "!liste":
            await show_list(message)
        elif message.content == "!cmd":
            response = show_commands()
            await message.channel.send(response)
        elif "@" in message.content:
            pseudo = get_pseudo(message)
            message.content.replace(pseudo, '')
            parts = message.content.split(" ")
            print(pseudo)
            mention = parts[0]
            verb = parts[1]
            mot = parts[2]
            if verb in verbs.keys() and mot in verbs[verb]:
                await message.channel.send("Ok, je note ça!")
                print("mot", mot)
                print("verb", verb)
                db = db_connect()
                cursor = db.cursor()
                cursor.execute("SELECT " + mot + " FROM users WHERE pseudo='" + pseudo + "'")
                value = cursor.fetchone()[0] 
                print("valeur recuperee:" + str(value))
                value += 1
                
                if mot == "retard" and value == 3:
                    await message.channel.send("<@" + str(message.mentions[0].id) + "> est en retard pour la 3ème fois!! **GAGE!!** :grin: :grin: :grin:")
                    value = 0
                elif mot == "retard":
                    retards_restants = str(3-value)
                    await message.channel.send("C'est pô bien! Il te reste " + retards_restants + " retard(s) avant le gage ultime! :face_with_monocle:")
                else:
                    await message.channel.send("Merci à toi " + pseudo + "! :partying_face:")
                req = 'UPDATE users SET ' + mot + '="' + str(value) + '" WHERE pseudo="' + pseudo + '"'
                print(req)
                cursor.execute(req)
                db.commit()
                cursor.close()
                db.close()
                print(cursor.rowcount, "record(s) affected")
            elif verb in verbs.keys():
                await message.channel.send("Je n'ai pas compris, êtes-vous sûr que l'expression est correcte? Tapez '!cmd' pour en savoir plus.")
