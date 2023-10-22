import discord
from discord.ext import commands

# Botunuzun komut önekini belirleyin (örneğin, "!")
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} botu olarak giriş yapıldı.')

@bot.command()
async def cevapla(ctx, soru):
    # Soruya verilen yanıtı burada işleyin
    yanit = "Kağıt,Cam veya Plastik"
    await ctx.send(yanit)

# Botunuzu çalıştırın
bot.run("TOKENİNİZ BURAYA")
