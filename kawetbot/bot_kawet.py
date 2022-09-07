import discord
import time
import asyncio
import random
#import rpg_dice
from discord.ext import commands, tasks
import csv
"""from discord.ext import tasks
import os
from dotenv import load_dotenv
import youtube_dl
from discord.ext.commands import bot"""


client = commands.Bot(command_prefix='K!', help_command=None)

"""musics = {}
ytdl = youtube_dl.YoutubeDL()"""




"""default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)"""

"""
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename




@client.event

async def rpg(client):
    lvl1 = 1000
    xpuser = 0
    if xpuser < lvl1:
        await client.channel.send("pong")

"""
@client.event

async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("K!ping"):
        await message.channel.send("pong")

    if message.content.startswith("K!wallahjevaistoutfairepeterdansleserveuravecmacommandedelamortquituecheh"):
        await message.delete()
        x = True
        start = time.time()
        while x == True:
            await message.channel.send("pong")
            await asyncio.sleep(7.5)
            if time.time() - start > 60:
                x = False
            await message.channel.send("ping")
            await asyncio.sleep(7.5)
            if time.time() - start > 60:
                x = False

    """
    if message.content.startswith("K!say"):
        mes = message.content.split()
        output = ""
        for word in mes[1:]:
            output += word
            output += " "
        await message.channel.send(output)
        await message.delete()"""

    if message.content.startswith('K!say'):
        await message.channel.send(message.content[5:])
        await message.delete()

    quoi = message.content.split()
    feur = quoi[-1]
    feur = feur.upper()
    if feur.endswith("QUOI") or feur.endswith("QUOL") or feur.endswith("KOI") or feur.endswith("KUOI") or feur.endswith("QU0I") or feur.endswith("QU0L") or feur.endswith("KOL") or feur.endswith("KUOL") or feur.endswith("K0L") or feur.endswith("KU0L"):
        await message.channel.send("https://c.tenor.com/zvg8w0FkecYAAAAC/feur-theobabac.gif")

    if message.content.startswith("K!rolldice"):
        mes = message.content.split()
        dice = int(mes[1])
        await message.channel.send(f"bien joué BG, tu as fait {random.randint(1, dice)} !")

    if message.content.startswith("K!pari"):
        tunes = []
        with open('fichier_maxime.csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                tunes.append(row)
        mes = message.content.split()
        dice = int(mes[1])
        choice = int(mes[2])
        if ((type(dice) and type(choice) == int) and dice>=choice>=0):
            lance = random.randint(1, dice)
            id = message.author.id
            index = 0
            if dice == 1:
                lance = random.randint(0, 1)
                if lance == choice:
                    await message.channel.send("T'as vraiment de la chance. Et si tu tentais de mettre une vraie mise ?")
                else:
                    await message.channel.send("T'as vraiment pas de chance. Conseil: entraine toi à avoir de la chance ou améliore ton karma")
            for loop in range(len(tunes)):
                if str(id) == str(tunes[loop][2]):
                    index = loop
            if lance == choice:
                tunes[index][1] = int(tunes[index][1]) * dice
                await message.channel.send(f"Bien joué {message.author.mention}, tu as gagné !")
            elif lance != choice and dice != 1:
                tunes[index][1] = int(tunes[index][1]) // dice
                await message.channel.send(f"Bah merde t'as perdu {message.author.mention}. Qu'est ce qui s'est passé ? Aller, ne perd pas espoir et retente ta chance")
            tunes[index][1] = int(tunes[index][1])
            if dice != 1:
                await message.channel.send(f"Il te reste actuellement {tunes[index][1]} points")
            tunes[index][1] = str(tunes[index][1])
            tab = [[" Name                  ","Money  ","ID"]]
            del(tunes[0])
            for loop in range(len(tunes)):
                tunes[loop][1] = int(tunes[loop][1])
            tunes = sorted(tunes, reverse = True, key=lambda money: money[1])
            for loop in range(len(tunes)):
                tab += [tunes[loop]]
            for loop in range(len(tunes) + 1):
                tab[loop][1] = str(tab[loop][1])
                tab[loop][1] += " " * (9 - len(tab[loop][1]))
                tab[loop][1] += " " * (9 - len(str(tab[loop][1])))
            with open('fichier_maxime.csv', 'w', newline="", encoding='utf-8') as f:
                f_csv = csv.writer(f, delimiter=";")
                for ligne in tunes:
                    f_csv.writerow(ligne)
        else:
            await message.channel.send("Wallah qu'est ce que tu comprends pas dans les règles du jeu ?")
        await message.delete()

    if message.content.startswith("K!point"):
        id = message.author.id
        index = 0
        for loop in range(len(tunes)):
            if str(id) == str(tunes[loop][2]):
                index = loop
        await message.delete()
        await message.channel.send(f"Tu as {tunes[index][1]} points {message.author.mention}")

    if message.content.startswith("K!don"):
        tunes = []
        with open('fichier_maxime.csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                tunes.append(row)
        donateur = message.author.id
        index_donateur = 0
        for loop in range(len(tunes)):
            if str(donateur) == str(tunes[loop][2]):
                index_donateur = loop
        mes = message.content.split()
        donation = int(mes[1])
        if 0 < donation <= int(tunes[index_donateur][1]):
            receveur = mes[2]
            receveur = receveur.replace("@", "")
            receveur = receveur.replace("<", "")
            receveur = receveur.replace(">", "")
            index_receveur = 0
            for loop in range(len(tunes)):
                if str(receveur) == str(tunes[loop][2]):
                    index_receveur = loop
            tunes[index_donateur][1] = int(tunes[index_donateur][1]) - donation
            tunes[index_receveur][1] = int(tunes[index_receveur][1]) + donation
            tunes[index_donateur][1] = str(tunes[index_donateur][1])
            tunes[index_receveur][1] = str(tunes[index_receveur][1])
            tab = [[" Name                  ","Money  ","ID"]]
            del(tunes[0])
            for loop in range(len(tunes)):
                tunes[loop][1] = int(tunes[loop][1])
            tunes = sorted(tunes, reverse = True, key=lambda money: money[1])
            for loop in range(len(tunes)):
                tab += [tunes[loop]]
            for loop in range(len(tunes)+1):
                tab[loop][1] = str(tab[loop][1])
                tab[loop][1] += " " * (9 - len(tab[loop][1]))
            with open('fichier_maxime.csv', 'w', newline="", encoding='utf-8') as f:
                f_csv = csv.writer(f, delimiter=";")
                for ligne in tab:
                    f_csv.writerow(ligne)
            await message.delete()
            await message.channel.send(f"{message.author.mention} as fait un don de {mes[1]} points à <@{receveur}>")

    if message.content.startswith("K!class"):
        tunes = []
        with open('fichier_maxime.csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                tunes.append(row)
        for loop in range(len(tunes)):
            tunes[loop] = [tunes[loop][0] + tunes[loop][1]]
        tab = str(tunes)
        tab = tab.replace("[", "")
        tab = tab.replace("],", "\n")
        tab = tab.replace("]", "")
        tab = tab.replace("',", " |")
        tab = tab.replace("'", "")
        await message.channel.send(f"```{tab}```")

    if message.content.startswith("K!etat"):
        reponses_etat = random.randint(1, 4)
        if reponses_etat == 1:
            await message.channel.send("Yep, ça va")
        elif reponses_etat == 2:
            await message.channel.send("Bof, je suis en train d'être modifié")
        elif reponses_etat == 3:
            await message.channel.send("No because my dad touch my code >w<")
        else:
            await message.channel.send(f"Mais t'es qui toi {message.author.mention} ?")

    await client.process_commands(message)


"""@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(997403651972812820)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")"""

@client.command()
async def lien(ctx):
    embed = discord.Embed(title="Ca c'est ma fusée batard", url="https://twitter.com/MaximeMonichon",
                          description="N'hésitez pas à me follow sur twitter",
                          color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name, url="https://twitter.com/MaximeMonichon",
                     icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://c.tenor.com/Plbi9zuA910AAAAM/minecraft.gif")
    embed.add_field(name="Minecrafteur", value="Je fais du minecraft (c'est un peu faux)",
                    inline=True)
    embed.add_field(name="Fortniteur", value="Je tape mes meilleurs games à chaque fois", inline=True)
    embed.add_field(name="Multiversussien", value="Nike tout le monde avec Shaggy ou Finn", inline=True)
    await ctx.send(embed=embed)

"""
@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Attend que je finisse la musique ou soit fait K!stop si t'es pas une feignasse")
        return


    voicechannel = discord.utils.get(ctx.guild.voice_channels, name = "Un mec semi-bourré")
    #if not voice.is_connected():
    await voicechannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)


    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmepgExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Je suis pas encore dans un voc connard")

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Je suis déjà en pause enculé")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Je suis déjà en marche salope")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]"""

""""@client.command()
async def skip(ctx):
    client = ctx.guilde.voice_client
    client.stop()

def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url, before_options = "-reconnect 1 -reconnect_stream 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after = next)


@client.command()
async def play(ctx, url):
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)

    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"C'est parti pour {video.url}")
        play_song(client, musics[ctx.guild], video)"""



@client.event
async def on_ready():
    print("RUNNING")

client.run(TOKEN)