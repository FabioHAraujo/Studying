import discord
from discord.ext import commands
import yt_dlp as youtube_dl

intents = discord.Intents.all()
intents.voice_states = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

queue = []  # Fila de músicas
playing = False  # Indica se há uma música sendo reproduzida no momento

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.command()
async def play(ctx, *, search):
    if not ctx.message.author.voice:
        await ctx.send('Você precisa estar em um canal de voz para usar este comando.')
        return

    if not bot.voice_clients:
        channel = ctx.message.author.voice.channel
        voice_client = await channel.connect()
    else:
        voice_client = bot.voice_clients[0]

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': 'True',
        'default_search': 'auto',
        'quiet': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{search}", download=False)
        url = info['entries'][0]['url']

    queue.append(url)

    if not playing:
        await play_song(voice_client, ctx)

async def play_song(voice_client, ctx):
    global playing
    playing = True

    url = queue.pop(0)
    voice_client.play(discord.FFmpegPCMAudio(url, executable='ffmpeg/bin/ffmpeg.exe'), after=lambda e: bot.loop.create_task(play_next_song(voice_client, ctx, e)))

    await ctx.send('Tocando a música...')

async def play_next_song(voice_client, ctx, error=None):
    if len(queue) > 0:
        if error is None or error.error != 'Source was terminated.':
            await play_song(voice_client, ctx)
        else:
            print('A música foi interrompida.')
    else:
        await voice_client.disconnect()
        global playing
        playing = False

@bot.command()
async def leave(ctx):
    if bot.voice_clients:
        await bot.voice_clients[0].disconnect()
        global playing
        playing = False
        queue.clear()
    else:
        await ctx.send('Eu não estou conectado a nenhum canal de voz.')

bot.run('NjA1MjMwNzk4OTQ5NDQ5NzI4.G0dToq.yvSqX78UaWzpr-YyPUQir74t98pF7njq5JlJmI')
