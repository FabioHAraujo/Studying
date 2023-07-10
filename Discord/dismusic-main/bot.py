import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

intents = discord.Intents.all()
intents.voice_states = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Configurações do Spotify
SPOTIFY_CLIENT_ID = 'be0a966034d74a9a9db4787fd3d9b58d'
SPOTIFY_CLIENT_SECRET = '86276a40fe8240cabe315bbc181ab909'
SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback'

# Configurações do bot
bot_token = 'be0a966034d74a9a9db4787fd3d9b58d'
bot_channel_id = '86276a40fe8240cabe315bbc181ab909'

# Configuração do Spotipy
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                           client_secret=SPOTIFY_CLIENT_SECRET))

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.command()
async def play(ctx, *, song):
    if not ctx.message.author.voice:
        await ctx.send('Você precisa estar em um canal de voz para usar este comando.')
        return

    channel = ctx.message.author.voice.channel
    voice_client = await channel.connect()

    results = sp.search(q=song, type='track', limit=1)

    if results and 'tracks' in results and 'items' in results['tracks'] and len(results['tracks']['items']) > 0:
        track = results['tracks']['items'][0]
        track_name = track['name']
        track_artist = track['artists'][0]['name']
        track_url = track['external_urls']['spotify']

        await ctx.send(f'Tocando a música: {track_name} - {track_artist}')
        voice_client.play(discord.FFmpegPCMAudio(track_url, executable='ffmpeg/bin/ffmpeg.exe'))
    else:
        await ctx.send('Música não encontrada.')

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send('Eu não estou conectado a nenhum canal de voz.')

bot.load_extension('dismusic')
bot.run('NjA1MjMwNzk4OTQ5NDQ5NzI4.Gt-pGz.eyNAH1ppdz2WP_7i4JlTYMums8B8JZAl_fVlYU')
