import discord
from discord.ext import commands
import datetime
from random import randint
from urllib import parse, request
import re

bot = commands.Bot(command_prefix='7', description="Partie v2 de Napoleon ;)")

@bot.listen()
async def on_message(message):
    if "salut" in message.content.lower():
        await message.channel.send('Hey , Napoleon est dans la place' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "joyeux anniversaire" in message.content.lower():
        await message.channel.send('WHOUHOU JOYEUX ANNIV\' mon pote :birthday: :tada: ! ' )
        await bot.process_commands(message)

@bot.listen()
async def on_message(message):
    if "napoleon" in message.content.lower():
        await message.channel.send('Ca parle de moi dans mon dos ? ' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
        if "non" in message.content.lower():
            await message.channel.send('Mouais ... Perso je te crois pas ! ' )
            await bot.process_commands(message)
@bot.listen()
async def on_message(message):
        if "chien" in message.content.lower():
            await message.channel.send('Ouaf Ouaf , jfais bien le toutou?' )
            await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "chat" in message.content.lower():
        await message.channel.send('miaou miaou , dit le matou' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "quoi" in message.content.lower():
        await message.channel.send('Qu\'est ce que tu racontes toi' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "oui" in message.content.lower():
        await message.channel.send('Ok perso je te crois' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "dur" in message.content.lower():
        await message.channel.send('Ouf , tu peux me dire de le faire !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "facile" in message.content.lower():
        await message.channel.send('Alors fais le !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "wtf" in message.content.lower():
        await message.channel.send('Aussi what the fuck que la bataille de Waterloo ...' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "etrange" in message.content.lower():
        await message.channel.send('Aussi étrange que la bataille de Waterloo ...' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "bizzare" in message.content.lower():
        await message.channel.send('Aussi bizare que la bataille de Waterloo ...' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "chouchoupeek" in message.content.lower():
        await message.channel.send('Yanis le mec qui se fait Piocher sur fortnite et qui dit qu il est fort a cs alors qu il silver 4!' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "ace_23" in message.content.lower():
        await message.channel.send('Le mec le plus fort de F0RNITE !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "gibier" in message.content.lower():
        await message.channel.send('Ouais mais c\'est un bébé gibié !' )
        await bot.process_commands(message)

@bot.listen()
async def on_message(message):
    if "fornite" in message.content.lower():
        await message.channel.send('ace 23#4396 peux tous vous exploser a F0RNITE !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "csgo" in message.content.lower():
        await message.channel.send('ace 23#4396 peux tous vous exploser a Counter Strike Global offensive !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "ok" in message.content.lower():
        await message.channel.send('Pourqwa tu dis 0ui?' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "mdr" in message.content.lower():
        await message.channel.send('C\'est pas drôle ...' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "genie" in message.content.lower():
        await message.channel.send('Wow c\'est trop marrant!' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "cheat" in message.content.lower():
        await message.channel.send('Tu as un Aimbot!Je t\'ai vu' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "mais" in message.content.lower():
        await message.channel.send('Wow quelle répartie incroyable !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "ntm" in message.content.lower():
        await message.channel.send('Wow quelle répartie incroyable !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "mee6" in message.content.lower():
        await message.channel.send('C\'est mon cousin !Comment le connaissez vous ?' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "dieu" in message.content.lower():
        await message.channel.send('Mais pourquoi Dieu m\'a t\'il crée si il existe ?' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "pute" in message.content.lower():
        await message.channel.send('Wow quelle répartie incroyable !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "nique" in message.content.lower():
        await message.channel.send('Wow quelle répartie incroyable !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "tg" in message.content.lower():
        await message.channel.send('Wow quelle répartie incroyable !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "guel" in message.content.lower():
        await message.channel.send('Wow quelle répartie incroyable !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "rigolo" in message.content.lower():
        await message.channel.send(' A se plier de rire !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "blague" in message.content.lower():
        answers = ['Quelle mamie fait peur aux voleurs ? Mamie Traillette. ', 'J\'ai une blague sur les magasins Mais elle a pas supermarché', 'Pourquoi est-ce c\'est difficile de conduire dans le Nord ? Parce que les voitures arrêtent PAS DE CALER.', 'Comment fait-on pour allumer un barbecue breton ? On utilise des breizh.',
                   'Comment est-ce que la chouette sait que son mari fait la gueule ? Parce qu’HIBOUDE', 'Pourquoi est-ce qu\'on dit que les bretons sont tous frères et sœurs ? Parce qu’ils n’ont Quimper..', ' Pourquoi est-ce qu\'on met tous les crocos en prison ?Parce que les crocos dealent.', 'Quel est l\'arbre préféré des chômeurs ? Le bouleau ',
                   'Pourquoi dit-on que les poissons travaillent illégalement ? Parce qu’ils n’ont pas de FISH de paie.', 'Quel est le bar préféré des espagnols ? Le Bar-celone', 'Qu\'est-ce qu\'un tennisman adore faire ? Rendre des services','JE SAIS PAS MOI']
        embed = discord.Embed(title='**Ma blague:** ', description='{0}'.format(answers[randint(0, len(answers))]), color=0x00FF00)
        await message.channel.send(embed=embed)
@bot.listen()
async def on_message(message):
    if "internet" in message.content.lower():
        await message.channel.send('Pff Moi j\'utilise le MINITEL, c\'est bien mieux !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "menteur" in message.content.lower():
        await message.channel.send('Mythomane!' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "alexdieu" in message.content.lower():
        await message.channel.send('MON CREATEUR! PAPA!' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "roblox" in message.content.lower():
        await message.channel.send('C\'est le minecraft en deux fois plus moche ?' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "croco" in message.content.lower():
        await message.channel.send('Je vais te croquer!' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "minecraft" in message.content.lower():
        await message.channel.send('Je préfère CS ou F0RNITE!' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "nul" in message.content.lower():
        await message.channel.send('Oui toi t\' es nul!' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "python" in message.content.lower():
        await message.channel.send('Tu sais coder ? Wow tu as réussi à coder trois lignes https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/source.gif !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "java" in message.content.lower():
        await message.channel.send('Oracle , c\'est son papa https://media.giphy.com/media/8Zef2waxYtviobBI3a/source.gif' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "pere" in message.content.lower():
        await message.channel.send('Mon papa c\'est alexdieu!' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "ban" in message.content.lower():
        await message.channel.send('Un ban c\'est un peu sévère!' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "alexdieu" in message.content.lower():
        await message.channel.send('MON CREATEUR! PAPA!' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "chouchoupik" in message.content.lower():
        await message.channel.send('le bot qui fait rien ?' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "bot" in message.content.lower():
        await message.channel.send('Pff tous ces programmes sont inutiles comparés a moi!' )
        await bot.process_commands(message)
bot.listen()
async def on_message(message):
    if "minitel" in message.content.lower():
        await message.channel.send('C\'est mon préféré !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "qui" in message.content.lower():
        await message.channel.send('De quelle personne parlez vous?' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "jsp" in message.content.lower():
        await message.channel.send('Moi non plus !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "Youtube" in message.content.lower():
        await message.channel.send('Worst platform ever !' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "maths" in message.content.lower():
        await message.channel.send('Vous saviez que je faisais fonction calculatrice aussi ? https://media.giphy.com/media/cRMgB2wjHhVN2tDD2z/source.gif!' )
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):
    if "choucoupeek" in message.content.lower():
        await message.channel.send('Yanis le mec qui se fait Piocher sur fortnite et qui dit qu il est fort a cs alors qu il silver 4!' )
        await bot.process_commands(message)

bot.run('Njk5OTA3NjQ4NjEwNjMxNzIw.Xpyq6A.mc_BEtT7Yzn1Rk9tj09fRTP0ibc')
