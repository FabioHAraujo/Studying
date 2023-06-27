import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False  # Desabilita a intenção de receber eventos de digitação
intents.presences = False  # Desabilita a intenção de receber eventos de presença

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def boom(ctx):
    await ctx.send("BAKURESTU MAHOOOOOU! EEEEKUUSPROOOOGIOOOOON! *BOOM*")

Secret = open("token.txt", 'r')
Secret = Secret.read()
bot.run(Secret)
