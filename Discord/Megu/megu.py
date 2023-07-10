import asyncio
from datetime import datetime, timedelta

import discord
from discord.ext import commands

import youtube_dl
from ffmpeg import stream

intents = discord.Intents.all()  # Habilita todas as intenções
intents.typing = False  # Desabilita a intenção de receber eventos de digitação
intents.presences = False  # Desabilita a intenção de receber eventos de presença

bot = commands.Bot(command_prefix="!", intents=intents)

cooldowns = {}


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

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

def write_to_log(log_message):
    with open("logs.txt", "a") as log_file:
        log_file.write(log_message + "\n")

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def explosion(ctx, member: discord.Member):
    #await ctx.message.delete()  # Remove a mensagem de comando para evitar poluição no canal

    # Verifica se o usuário está em cooldown
    if ctx.author.id in cooldowns:
        remaining_time = cooldowns[ctx.author.id] - datetime.utcnow()
        await ctx.send(f"{ctx.author.mention}, EI EI EI, VOCÊ JÁ EXPLODIU ALGUÉM HOJE, PODERÁ EXPLODIR NOVAMENTE EM {remaining_time}. DESNCANA, NÃO VOU EXPLODIR NINGUÉM HOJE NÃO, TÁ BOM?")
        return

    # Aplica o cooldown ao usuário
    cooldowns[ctx.author.id] = datetime.utcnow() + timedelta(days=1)

    # Silencia o usuário mencionado por 10 minutos
    muted_role = discord.utils.get(ctx.guild.roles, name="EXPLODIDOS")
    await member.add_roles(muted_role, reason="Explosion Command")
    await ctx.send(f"EXPLOOOOOSIOOOON! O usuário {member.mention} FOI MUTADO POR 10 MINUTOS! BOOOOOM! MWAHAHAHAHAHA! 💥🔥💣. ENCOMENDA DE: {ctx.author.mention}! ")

    # Aguarda 10 minutos antes de remover o silenciamento
    await asyncio.sleep(600)
    await member.remove_roles(muted_role, reason="Explosion Command")

    log_message = f"[{datetime.utcnow()}] {ctx.author} usou o comando !explosion em {member}"
    write_to_log(log_message)


@explosion.error
async def explosion_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = error.retry_after
        hours = int(remaining_time / 3600)
        minutes = int((remaining_time % 3600) / 60)
        await ctx.send(f"{ctx.author.mention}, EI EI EI, VOCÊ JÁ EXPLODIU ALGUÉM HOJE, PODERÁ EXPLODIR NOVAMENTE EM {hours} HORAS E {minutes} MINUTOS. MWAHAHAHAHAHA! 💥🔥💣")
        log_message = f"[{datetime.utcnow()}] {ctx.author} tentou usar o comando !explosion, mas está em cooldown"
        write_to_log(log_message)
    else:
        await ctx.send("Ocorreu um erro ao executar o comando.")


@bot.command()
async def boom(ctx):
    await ctx.send("BAKURESTU MAHOOOOOU! EEEEKUUSPROOOOGIOOOOON! *BOOM*")
    log_message = f"[{datetime.utcnow()}] {ctx.author} usou um boom :)"
    write_to_log(log_message)

async def on_ready():
    print(f"Megumin na Area, conectando como: {bot.user}")


@bot.command(name='play', help='To play song')
async def play(ctx, url):
    try:
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="C:\\Users\\super\\OneDrive\Documentos\\1ESTUDANDO\\Discord\\Megu\\ffmpeg\\bin\\ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except Exception as e:
        await ctx.send("Ocorreu um erro ao baixar o vídeo.")
        print(f"Erro ao baixar o vídeo: {str(e)}")

@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")


@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

Secret = open("token.txt", 'r')
Secret = Secret.read()
bot.run(Secret)
