
import logging
import discord
import asyncio
import aiohttp
import json
from discord.ext.commands import Bot
from random import randint
from discord.ext import commands
from discord.ext.commands import Bot
from platform import python_version
import os
import platform
import socket
import datetime
from urllib import parse, request
import re



BOT_PREFIX = ('n!')
TOKEN = 'token'
OWNERS = [516709993005973538 , 443484634806878208 , 420970087013679105 ]
BLACKLIST = [353873396481785857, 588334404187848733, 372848163616194561, 690955197651877928]
client = Bot(command_prefix=BOT_PREFIX)
bot = commands.Bot(command_prefix=BOT_PREFIX)

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game("vous créer!"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game("créer avec ALEXDIEU !"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game("n!AIDE"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game("créer avec des humains!"))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print('Enregistré en tant que ' + client.user.name)
    print("Discord.py la version de l'API:", discord.__version__)
    print("Version de Python:", platform.python_version())
    print("Qui fonctionne sous:", platform.system(), platform.release(), "(" + os.name + ")")
    print('-------------------')

@client.command(name='additionne', pass_context=True)
async def ajoute(context, a: int, b: int):
    await context.send(a+b)

@client.command(name='multiplie', pass_context=True)
async def multiplie(context, a: int, b: int):
    await context.send(a*b)

@client.command(name='divise', pass_context=True)
async def divise(context, a: int, b: int):
    await context.send(a/b)

@client.command(name='soustrait', pass_context=True)
async def soustrait(context, a: int, b: int):
    await context.send(a-b)

@client.command(name='salut', pass_context=True)
async def salut(context):
    await context.send(":smiley: :wave: Bonjour !Je suis le plus rapide pour taper au clavier!{0}".format(context.message.author))
    await context.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@client.command(name='youtube', pass_context=True)
async def youtube(context, *, search):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:                                
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
        search_results = re.findall('href=\"\\/watch\\?v=(.{30})', html_content.read().decode())
        print(search_results)
        await context.send('https://www.youtube.com/watch?v=' + search_results[0])

@client.command(name='info', pass_context=True)
async def info(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        e = discord.Embed(description='ALEXDIEU prog info ', color=0x00FF00)
        e.set_author(name="Informations sur le bot")
        e.add_field(name="Créateur:", value="ALEXDIEU", inline=True)
        e.add_field(name="Version de Python:", value="{0}".format(python_version()), inline=True)
        e.add_field(name="Préfixe:", value="n! ", inline=False)
        e.add_field(name="Personne Sympa :",value=f"{context.guild.owner}")
        e.set_footer(text="Demandé par  {0}".format(context.message.author))
        await context.message.channel.send(embed=e)

@client.command(name='infosurleserveur', pass_context=True)
async def serverinfo(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        server = context.message.guild
        roles = [x.name for x in server.roles]
        role_length = len(roles)
        if role_length > 50:
            roles = roles[:50]
            roles.append('>>>> Montre les[50/%s] Roles' % len(roles))
        roles = ', '.join(roles)
        channelz = len(server.channels)
        time = str(server.created_at)
        time = time.split(' ')
        time = time[0]
        embed = discord.Embed(description='%s ' % (str(server)), title='**Nom du serveur:**', color=0x00FF00)
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(name='__PROPRIETAIRE__', value=str(server.owner) + '\n' + str(server.owner.id))
        embed.add_field(name='__ID DU SERVEUR__', value=str(server.id))
        embed.add_field(name='__NB DE MEMBRES__', value=str(server.member_count))
        embed.add_field(name='__SALONS VOCAUX/TEXTUELS__', value=str(channelz))
        embed.add_field(name='__Roles (%s)__' % str(role_length), value=roles)
        embed.set_footer(text='Créé à : %s' % time)
        await context.message.channel.send(embed=embed)

@client.command(name='proprio', pass_context=True)
async def info(context):
    if context.message.author.id in BLACKLIST:
     embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
     await context.message.channel.send(embed=embed)
    else:
       embed = discord.Embed(title=f"Serveur infos :", description="Le serveur :", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
       embed.add_field(name="Serveur crée le ", value=f"{context.guild.created_at}")
       embed.add_field(name="Proprio", value=f"{context.guild.owner}")
       embed.add_field(name="Région du serveur", value=f"{context.guild.region}")
       embed.add_field(name="ID DU SERVEUR", value=f"{context.guild.id}")
       embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
       await context.message.channel.send(embed=embed)

@client.command(name='ping', pass_context=True)
async def ping(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        embed = discord.Embed(color=0x00FF00)
        embed.set_footer(text='requête pong par {0}'.format(context.message.author))
        embed.add_field(name='Pong!', value=':ping_pong:', inline=True)
        await context.message.channel.send(embed=embed)

@client.command(name='allemand', pass_context=True)
async def allemand(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        embed = discord.Embed(color=0x00FF00)
        embed.set_footer(text='requete allemand par Der Bürger : {0}'.format(context.message.author))
        embed.add_field(name='Hallo! Ich bin Franzose, aber ich liebe Deutschland!', value=':flag_de:', inline=True)
        await context.message.channel.send(embed=embed)

@client.command(name='invite', pass_context=True)
async def invite(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        await context.message.channel.send('Je vous ai envoyé un message en MP !')
        await context.message.channel.send('Invitez moi en cliquant ici: https://discordapp.com/oauth2/authorize?&client_id=699907648610631720&scope=bot&permissions=8')


@client.command(name='server', pass_context=True)
async def server(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        await context.message.channel.send('Je vous ai envoyé un message en MP !')
        await context.message.channel.send('Vous pouvez joindre mon serveur ici ! : https://discord.gg/Rm84JTm merci!')

@client.command(name='sondage', pass_context=True)
async def poll(context, *args):
    mesg = ' '.join(args)
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        await context.message.delete()
        embed = discord.Embed(title='Nous avons un sondage !', description='{0}'.format(mesg), color=0x00FF00)
        embed.set_footer(text='Sondage créé par : {0} • Réagissez pour voter!'.format(context.message.author))
        embed_message = await context.message.channel.send(embed=embed)
        await embed_message.add_reaction( '👍')
        await embed_message.add_reaction('👎')
        await embed_message.add_reaction('🤷')

@client.command(name='Oui?', pass_context=True)
async def eight_ball(context, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        answers = ['C est Certain.', 'C est ainsi.', 'Vous pouvez compter sur elle.', 'Sans aucun doute.',
                   'Oui - certainement.', 'Comme je le vois, oui.', 'Très probablement', 'Ca semble bon.', 'OUI.',
                   'Les signes pointent vers le oui.', 'Redemandez plus tard', 'Mieux vaut ne pas vous dire maintenant.',
                   'Ne peut pas prédire maintenant.', 'Concentrez-vous et demandez à nouveau plus tard', 'Ne comptez pas dessus.', 'Ma réponse est non',
                   'Mes sources disent non.', 'Ca sent pas bon', 'JE SAIS PAS MOI']
        embed = discord.Embed(title='**Ma réponse:** ', description='{0}'.format(answers[randint(0, len(answers))]), color=0x00FF00)
        embed.set_footer(text='Question demandé par: {0} • Demandez la votre maintenant !'.format(context.message.author))
        await context.message.channel.send(embed=embed)

@client.command(name='bitcoin', pass_context=True)
async def bitcoin(context):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed = discord.Embed(title='Wall Street : Info',
                              description='Le prix du bitcoincoin en US dollard actuellment: $' + response['bpi']['USD']['rate'], color=0x00FF00)
        await context.message.channel.send(embed=embed)


@client.command(name='eteindre', pass_context=True)
async def shutdown(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.id in OWNERS:
            embed = discord.Embed(title='Exctinction des feux !', description='Je m\'éteins ... A plus DANS L BUS ! :wave:', color=0x00FF00)
            await context.message.channel.send(embed=embed)
            await client.logout()
            await client.close()
        else:
            embed = discord.Embed(title='ERREUR!', description='Vous n\'avez pas la permission d utiliser cette commande',
                                  color=0x00FF00)
            await context.message.channel.send(embed=embed)


@client.command(name='dire', pass_context=True)
async def echo(context, *, content):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.id in OWNERS:
            await context.message.delete()
            await context.message.channel.send(content)
        else:
            embed = discord.Embed(title='ERREUR!', description='VOUS N\'AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
            await context.message.channel.send(embed=embed)

@client.command(name='ancrer', pass_context=True)
async def embed(context, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.id in OWNERS:
            mesg = ' '.join(args)
            embed = discord.Embed(description=mesg, color=0x00FF00)
            await context.message.channel.send(embed=embed)
            await context.message.delete()
        else:
            embed = discord.Embed(title='ERREUR!', description='VOUS N\'AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
            await context.message.channel.send(embed=embed)


@client.command(name='kicker', pass_context=True)
async def kick(context, member: discord.Member, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)

        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.kick_members:
            if member.guild_permissions.administrator:
                embed = discord.Embed(title='ERREUR', description='UTILISATEUR A DES PERMS ADMIN.', color=0x00FF00)
                await context.message.channel.send(embed=embed)
            else:
                mesg = ' '.join(args)
                embed = discord.Embed(title='Utilisateur a été kické', description='**{0}** a été kické par **{1}**!'.format(member,context.message.author),color=0x00FF00)
                embed.add_field(name='Raison:', value=mesg)
                await context.message.channel.send(embed=embed)
                await context.message.delete()
                await member.send('Vous avez été averti par  **{0}**!  '.format(context.message.author) + 'RAISON: {0}'.format(mesg))
                await member.kick()
        else:
            embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
            await context.message.channel.send(embed=embed)

@client.command(name='renomme', pass_context=True)
async def nick(context, member: discord.Member, *, name : str):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.administrator:
            if name.lower() == "!reset":
                name = None
            embed = discord.Embed(title='SURNOM changé !', description='**{0}** votre nouveau surnom est **{1}**!'.format(member, name), color=0x00FF00)
            await context.message.channel.send(embed=embed)
            await context.message.delete()
            await member.nick(name)
        else:
            embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
            await context.message.channel.send(embed=embed)

@client.command(name='ban', pass_context=True)
async def ban(context, member: discord.Member, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.administrator:
            if member.guild_permissions.administrator:
                eembed = discord.Embed(title='ERREUR', description='UTILISATEUR A DES PERMS ADMIN :sweat_smile: .', color=0x00FF00)
                await context.message.channel.send(embed=embed)
            else:
                mesg = ' '.join(args)
                embed = discord.Embed(title='Utilisateur Banni!', description='**{0}** à été banni par **{1}**! :neutral_face: '.format(member,context.message.author),color=0x00FF03)
                embed.add_field(name='Raison:', value=mesg)
                await context.message.channel.send(embed=embed)
                await context.message.delete()
                await member.send('Vous avez été banni par **{0}**!'.format(context.message.author) + 'RAISON : {0}'.format(mesg))
                await member.ban()
        else:
            embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE :sweat_smile: ', color=0x00FF00)
            await context.message.channel.send(embed=embed)


@client.command(name='deban', pass_context=True)
async def unban(context, user: discord.Member):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.administrator:
            embed = discord.Embed(title='Utilisateur débanni!',
                                  description='**{0}** à été débanni par **{1}**!'.format(user, context.message.author),
                                  color=0x00FF00)
            await context.message.channel.send(embed=embed)
            await context.message.delete()
            await user.send('Vous avez été débanni par **{0}**!  '.format(context.message.author) + 'RAISON: Ban révoqué :wink: ')
            await user.unban()
        else:
            embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
            await context.message.channel.send(embed=embed)


@client.command(name='avertir', pass_context=True)
async def warn(context, member: discord.Member, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.administrator:
            mesg = ' '.join(args)
            embed = discord.Embed(title='Utilisateur averti !',
                                  description='**{0}** a été averti par **{1}**!'.format(member, context.message.author),
                                  color=0x00FF00)
            embed.add_field(name='Raison:', value=mesg)
            await context.message.channel.send(embed=embed)
            await context.message.delete()
            await member.send('Vous avez été averti par **{0}**!  '.format(context.message.author) + 'Raison: {0}'.format(mesg))
        else:
            embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
            await context.message.channel.send(embed=embed)

@client.command(name='pfc' ,pass_context=True)
async def pfc(ctx):
	global message_pfc
	global joueur
	global host
	joueur = []
	action = []
	host = None
	mentions = ctx.message.mentions
	if len(mentions) == 0:
		host = ctx.message.channel.send(ctx.message.channel,content="Cliquer sur la coche ci-dessous pour jouer au Pierre Feuille Ciseaux",tts=False,embed=None)
		message_pfc = host
	else:
		mentions = mentions[0]
		if mentions != ctx.message.author:
			host = ctx.message.channel.send(ctx.message.channel,content="<@"+str(ctx.message.author.id)+"> a défier <@"+str(mentions.id)+"> au Pierre Feuille Ciseaux",tts=False,embed=None)
			message_pfc = ctx.message.channel.send(mentions,content="<@"+str(ctx.message.author.id)+'> vous a défier au Pierre Feuille Ciseaux sur le serveur "'+str(ctx.message.server)+'" dans le channel: #'+str(ctx.message.channel),tts=False,embed=None)
			joueur.append(ctx.message.author)
			await ctx.message.channel.send(ctx.message.author,content="Vous êtes prêt!",tts=False,embed=None)
			await client.add_reaction(message_pfc, "❌")
	await client.add_reaction(message_pfc, '✅')


@client.event
async def on_reaction_add(reaction,user):
	if str(user.id) != "420970087013679105":
		global message_pfc
		global joueur
		global action
		global host
		if message_pfc != None and reaction.message.id == message_pfc.id:
			if reaction.emoji == "✅":
				if len(joueur) <= 2:
					joueur.append(user)
					await client.send_message(user,content="Vous êtes prêt!",tts=False,embed=None)
				if len(joueur) == 2:
					if joueur[0].id > joueur[1].id:
						buffer = joueur[1]
						joueur[1] = joueur[0]
						joueur[0] = buffer
					await client.send_message(host.channel, content="La partie a démarré:\n<@"+str(joueur[0].id)+"> VS <@"+str(joueur[1].id)+">",tts=False,embed=None)
					action = [-1,-1]
					for i in joueur:
						autre_joueur = None
						for z in joueur:
							if z != i:
								autre_joueur = z
						message = await client.send_message(i, content="Vous jouer contre "+str(autre_joueur)+" (Réagissez pour jouer):",tts=False,embed=None)
						scheme = ['✊','🖐','✌']
						for z in scheme:
							await client.add_reaction(message, z)
			elif reaction.emoji == "❌" and host != message_pfc:
				await client.send_message(host.channel, content="Le joueur a refusé le défi!",tts=False,embed=None)
				await client.send_message(message_pfc.channel, content="Vous avez refusé le défi!",tts=False,embed=None)
				message_pfc = None
				joueur = []
				action = []
				host = None
		elif user in joueur:
			if reaction.emoji == "✊": # 1
				action[joueur.index(user)] = 1
			elif reaction.emoji == "🖐": # 2
				action[joueur.index(user)] = 2
			elif reaction.emoji == "✌": # 3
				action[joueur.index(user)] = 3
			if action.count(-1) == 0:
				if action[0] == action[1]:
					status = "C'est une égalité!"
				elif action[0] == 3 and action[1] == 1:
					status = "<@"+str(joueur[1].id)+"> a gagné!"
				elif action[1] == 3 and action[0] == 1:
					status = "<@"+str(joueur[0].id)+"> a gagné!"
				elif action[0] > action[1]:
					status = "<@"+str(joueur[0].id)+"> a gagné!"
				elif action[1] > action[0]:
					status = "<@"+str(joueur[1].id)+"> a gagné!"
				a = 0
				for i in action:
					if i == 1:
						action[a] = "✊"
					elif i == 2:
						action[a] = "🖐"
					elif i == 3:
						action[a] = "✌"
					a = a + 1
				coucou = await client.send_message(host.channel, content="Voici la partie:\n<@"+str(joueur[0].id)+"> : "+str(action[0])+" VS "+str(action[1])+" : <@"+str(joueur[1].id)+">\n"+status,tts=False,embed=None)
				await client.add_reaction(coucou, "👏")
				await client.add_reaction(coucou, "👍")
				message_pfc = None
				joueur = []
				action = []
				host = None


@client.event
async def on_reaction_remove(reaction,user):
	global joueur
	if user in joueur:
		if reaction.emoji == "✅":
			joueur.remove(user)
			await client.send_message(user,content="Vous n'êtes plus prêt!",tts=False,embed=None)

@client.command(name='nettoyage', pass_context=True)
async def purge(context, number):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.administrator:
            number = int(number)
            await context.message.channel.purge(limit=number)
            embed = discord.Embed(title='Chat nettoyé!',description='**{0}** a nettoyé **{1}** messagen!'.format(context.message.author,number), color=0x00FF00)
            message = await context.message.channel.send(embed=embed)
            await asyncio.sleep(3)
            await message.delete()
        else:
            embed = discord.Embed(title='ERREUR!', description='VOUS N AVEZ PAS LA PERMISSION D UTILISER CETTE COMMANDE', color=0x00FF00)
            await context.message.channel.send(embed=embed)

@client.command(name='listenoire', pass_context=True)
async def blacklist(context, mode : str, user : discord.User = None):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.id in OWNERS:
            if (mode.lower() == "ajouter"):
                userID = user.id
                try:
                    BLACKLIST.append(userID)
                    embed = discord.Embed(title="Utilisateur Blacklisté", description='**{0}** a été ajouté a la liste noire '.format(user.name), color=0x00FF00)
                    embed.set_footer(text='Il y a maintenant {0} utilisateurs dans la liste noire !'.format(len(BLACKLIST)))
                    await context.message.channel.send(embed=embed)
                except:
                    embed = discord.Embed(title=":x: ERREUR!", description="Un erreur inconnue se produit quand j'ajoute  **{0}** à la blackliste.".format(user.name), color=0xFF0000)
                    await context.message.channel.send(embed=embed)
            elif (mode.lower() == "supp"):
                userID = user.id
                try:
                    BLACKLIST.remove(userID)
                    embed = discord.Embed(title="Utilisateur déblacklisté",
                                          description='**{0}** a été supprimé de la blackliste '.format(
                                              user.name), color=0x00FF00)
                    embed.set_footer(text='Il y a maintenant {0} utilisateurs dans la liste noire !'.format(len(BLACKLIST)))
                    await context.message.channel.send(embed=embed)
                except:
                    embed = discord.Embed(title=":x: ERREUR!",
                                          description="Un erreur inconnue se produit quand j'ajoute  **{0}** à la blackliste.\nÊtes vous sur que l'utilisateur est blacklisté ??".format(
                                              user.name), color=0xFF0000)
                    await context.message.channel.send(embed=embed)
            elif (mode.lower() == "liste"):
                embed = discord.Embed(title="Il y a actuellement {0} IDs blacklistés ".format(len(BLACKLIST)),description="{0}".format(BLACKLIST),color=0x00FF00)
                await context.message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title='ERREUR', description='VOUS N\'AVEZ PAS LA PERMISSION POUR CETTE COMMANDE .',color=0xFF0000)
            await context.message.channel.send(embed=embed)

client.remove_command('AIDE')

@client.command(name='AIDE', description='AIDE POUR VOUS !', brief='A L\'AIDE !!!', pass_context=True)
async def help(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='Vous êtes blacklisté!', description='Demandez au propriétaire de retirer de la liste', color=0x00FF00)
        await context.message.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Bot', description='Liste des commandes :', color=0x00FF00)
        embed.add_field(name='Invite - Invite le bot', value='Usage: n!invite', inline=False)
        embed.add_field(name='Server - Rejoignez mon serveur', value='Usage: n!server', inline=False)
        embed.add_field(name='sondage - Crée un sondage pour les utilisateurs', value='Usage: n!sondage <idée>', inline=False)
        embed.add_field(name='Oui? - réponds a vos questions', value='Usage: n!Oui? <question>', inline=False)
        embed.add_field(name='Bitcoin - Montre la valeur du bitcoincoin en US dollard ', value='Usage: n!bitcoin', inline=False)
        embed.add_field(name='Info - Donne des infos sur le bot', value='Usage: n!info', inline=False)
        embed.add_field(name='eteindre - éteint le bot [PROPRIETAIRE]', value='Usage: n!eteindre', inline=False)
        embed.add_field(name='dire - J\'envoie un message de votre choix [PROPRIO]', value='Usage: n!dire <message>', inline=False)
        embed.add_field(name='ancrer - j\'envoie un message encré de votre choix [PROPRIO]', value='Usage: n!ancrer <message>', inline=False)
        embed.add_field(name='kicker - Kick un utilisateur', value='Usage: n!kicker <utilisateur> <raison>', inline=False)
        embed.add_field(name='ban - Ban un utilisateur ', value='Usage: n!ban <utilisateur> <raison>', inline=False)
        embed.add_field(name='avertir - averti un utilisateur en MP', value='Usage: n!avertir <utilisateur> <raison>', inline=False)
        embed.add_field(name='deban - Débanne un utilisateur', value='Usage: n!deban <utilisateur>', inline=False)
        embed.add_field(name='nettoyage - enleve un NB de messages ', value='Usage: n!nettoyage <nb>', inline=False)
        embed.add_field(name='AIDE - Montre ce menu', value='Usage: n!AIDE', inline=False)
        embed.add_field(name='proprio - Montre le propriétaire et la date de création du serveur ', value='Usage : n!proprio' , inline=False)
        embed.add_field(name='youtube - Chercher une vidéo(ALPHA !)', value='Usage : n!youtube <mot clé>', inline=False)
        embed.add_field(name='salut - Le bot se présente !' , value='Usage : n!salut ')
        embed.add_field(name='allemand - présentation du bot en allemand !' , value='Usage : n!allemand ', inline=False)
        await context.message.channel.send(embed=embed)

@client.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandOnCooldown):
        await context.message.delete()
        embed = discord.Embed(title="ERREUR", description='Cette commande ne peut etre executé que dans  %.2fs ' % error.retry_after, color=0x00FF00)
        message = await context.message.channel.send(embed=embed)
        await asyncio.sleep(5)
        await message.delete()
    raise error

@blacklist.error
async def blacklist_error(context, error):
    embed = discord.Embed(title='**Commande:** n!listenoire', description='**Description::** Empeche un utilisateur d\'utiliser le bot \n **Usage:** n!listenoire [ajouter/supp/liste] [utilisateur] \n **Example:** n!listenoire ajouter @RandomUser', color=0x00FF00)
    await context.message.channel.send(embed=embed)

@ban.error
async def ban_error(context, error):
    embed = discord.Embed(title='**Commande:** n!ban', description='**Description:** ban un joueur \n **Usage:** n!ban [utilisateur] [raison] \n **Example:** n!ban @RandomUser SORS D\'ICI', color=0x00FF00)
    await context.message.channel.send(embed=embed)

@pfc.error
async def pfc_error(context, error):
    embed = discord.Embed(title='**Commande:** n!pfc', description='**Description:** jouer à Pierre Feuille Ciseaux \n **Usage:** n!pfc \n **Example:** n!pfc \n **ALERTE:** SI VOUS VOYEZ CETTE ERREUR CE N\'EST PAS NORMAL ! VEUILLEZ LE PRECISER A ALEXDIEU SUR GITHUB !', color=0x10FF00)                                                                                
    await context.message.channel.send(embed=embed)
    
@poll.error
async def poll_error(context, error):
    embed = discord.Embed(title='**Commande:** n!sondage', description='**Description:** Crée un sondage pour voter ! \n **Usage:** n!sondage [idée] \n **Example:** n! sondage BAN TOUT LE MONDE!', color=0x00FF00)
    await context.message.channel.send(embed=embed)

@eight_ball.error
async def eight_ball_error(context, error):
    embed = discord.Embed(title='**Commande:** n!Oui?', description='**Description:** AYEZ DES REPONSES A VOS QUESTIONS \n **Usage:** n!Oui? [question] \n **Example:** n! Oui? Êtes vous banni d\'un jeu?', color=0x00FF00)
    await context.message.channel.send(embed=embed)

@echo.error
async def say_error(context, error):
    embed = discord.Embed(title='**Commande:** n!dire', description='**Description:** je dis ce que vous dites \n **Usage:** n!dire [message] \n **Example:** n! dire JVAIS TE BAN!!', color=0x00FF00)
    await context.message.channel.send(embed=embed)

@youtube.error
async def youtube_error(context, error):
	embed = discord.Embed(title='**Commande:** n!youtube',description='**Description:** Rechercher sur youtube \n **Usage:** n!youtube [recherche] \n **Example:** n!youtube Chouchoupeek \n **Ps:**Si vous obtenez cette erreur mais que la syntaxe est bonne , c\'est qu\'il n\'y a pas de resultats pour votre recherche !', color=0x00FF00)
	await context.message.channel.send(embed=embed)


@embed.error
async def embed_error(context, error):
    embed = discord.Embed(title='**Commande:** n!ancrer',description='**Description:** je dis ce que vous dites avec un msg ancré \n **Usage:** n!ancrer [message] \n **Example:** n!ancrer CEUX QUI LISENT CA SONT BANNI!!', color=0x00FF00)
    await context.message.channel.send(embed=embed)


@kick.error
async def kick_error(context, error):
    embed = discord.Embed(title='**Commande:** n!kicker',description='**Description:** Kick un utilisateur \n **Usage:** n!kicker [utilisateur] [raison] \n **Example:** n!kicker @RandomUser REJOINS quand tu sera plus malin que moi !', color=0x00FF00)
    await context.message.channel.send(embed=embed)


@unban.error
async def unban_error(context, error):
    embed = discord.Embed(title='**Commande:** n!deban',description='**Description:** debans un utilisateur \n **Usage:** n!deban [utilisateur] \n **Example:** n!deban @RandomUser', color=0x00FF00)
    await context.message.channel.send(embed=embed)

@warn.error
async def warn_error(context, error):
    embed = discord.Embed(title='**Commande:** n!avertir',description='**Description:** averti un utilisateur \n **Usage:** n!avertir [utilisateur] [raison] \n **Example:** n!avertir @RandomUser STOP SPAM OU BAN!', color=0x00FF00)
    await context.message.channel.send(embed=embed)


@purge.error
async def purge_error(context, error):
    embed = discord.Embed(title='**Commande:** n!nettoyage',description='**Description:** nettoie des msg \n **Usage:** n!nettoyage [nb de messages] \n **Example:** n!nettoyage 20', color=0x00FF00)
    await context.message.channel.send(embed=embed)

client.run(TOKEN)
