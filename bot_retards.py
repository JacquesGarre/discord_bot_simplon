# coding: utf-8
import os
import mysql.connector 
from dotenv import load_dotenv
import discord

load_dotenv()
db = mysql.connector.connect(
    host = os.getenv('DB_HOST'), 
    user = os.getenv('DB_USER'), 
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME'))
cursor = db.cursor()


verbs = {
    'a_apporté' : ['riz', 'cafe_senseo', 'cafe_filtre','the','eponge','liquide_vaiselle'], 
    'est_en' : ['retard'], 
    'a_lavé' : ['torchons','micro_ondes']
}

def create_db():
    req1 = "CREATE TABLE IF NOT EXISTS `users` ("
    req1 += "`pseudo` varchar(255) NOT NULL,"
    req1 += "`retard` int(11) NOT NULL,"
    req1 += "`riz` int(11) NOT NULL,"
    req1 += "`cafe_senseo` int(11) NOT NULL,"
    req1 += "`cafe_filtre` int(11) NOT NULL,"
    req1 += "`the` int(11) NOT NULL,"
    req1 += "`eponge` int(11) NOT NULL,"
    req1 += "`liquide_vaiselle` int(11) NOT NULL,"
    req1 += "`torchons` int(11) NOT NULL,"
    req1 += "`micro_ondes` int(11) NOT NULL"
    req1 += ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    req2 = "INSERT INTO `users` (`pseudo`, `retard`, `riz`, `cafe_senseo`, `cafe_filtre`, `the`, `eponge`, `liquide_vaiselle`, `torchons`, `micro_ondes`) VALUES"
    req2 += "('20.100.', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Adeline', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Attila Kaya', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('charles', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Clément', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Clément B', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Colombe', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Damos (Damien)', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Emilie', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Fakhredine', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Guillaume', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('jaks', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Jason', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Mickael', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Nicolas.Duval', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Quentin', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Samuel', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Simon', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Thibaut', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Dino', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('karima', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Nicolas Plumet', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('Pierre Epron', 0, 0, 0, 0, 0, 0, 0, 0, 0),"
    req2 += "('reem', 0, 0, 0, 0, 0, 0, 0, 0, 0);"
    cursor.execute(req1)
    cursor.execute(req2)
    db.commit()
    print('DATABASE CREATED')

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
    response += "http://localhost/bot_discord/"
    await message.channel.send(response)
            
    # liste = '.\n'
    # liste += "**------ LEGENDE ------**\n"
    # liste += '1 : retard\n'
    # liste += '2 : riz\n'
    # liste += '3 : cafe_senseo\n'
    # liste += '4 : cafe_filtre\n'
    # liste += '5 : the\n'
    # liste += '6 : eponge\n'
    # liste += '7 : liquide_vaiselle\n'
    # liste += '8 : torchons\n'
    # liste += '9 : micro_ondes\n\n'
    # liste += "```pseudo          (1,2,3,4,5,6,7,8,9)\n\n"
    # for row in rows:
    #     print(row)
    #     liste += pseudo_format(row[0]) + ' (' + int_format(row[1]) + ',' + int_format(row[2]) + ',' + int_format(row[3]) + ',' + int_format(row[4]) + ',' + int_format(row[5]) + ',' + int_format(row[6]) + ',' + int_format(row[7]) + ',' + int_format(row[8]) + ',' + int_format(row[9]) + ')\n'       
    # liste += "```"
    # await message.channel.send(liste)

def pseudo_format(pseudo):
    while len(pseudo) <= 14:
        pseudo += ' '
    return pseudo

def int_format(value):
    value = str(value)
    return value

def get_pseudo(message):
    return message.mentions[0].name

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
        parts = message.content.split(" ")
        mention = parts[0]
        verb = parts[1]
        mot = parts[2]
        if verb in verbs.keys() and mot in verbs[verb]:
            await message.channel.send("Ok, je note ça!")
            print("mot", mot)
            print("verb", verb)
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
            print(cursor.rowcount, "record(s) affected")
        elif verb in verbs.keys():
            await message.channel.send("Je n'ai pas compris, êtes-vous sûr que le verbe correspond au mot? Tapez '!cmd' pour connaîtres les commandes.")
