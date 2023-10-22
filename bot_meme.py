import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    '''dog komutunu çağırdığımızda, program kopek_resmi_urlsi_al fonksiyonunu çağırır'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

def get_anime_image_url():
    url = 'https://kitsu.io/api/edge/anime?filter[text]=tokyo.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('anime')
async def anime(ctx):
    '''anime komutunu çağırdığımızda, program anime_resmi_urlsi_al fonksiyonunu çağırır'''
    image_url = get_anime_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)    

def get_pokemon_image_url():
    url = 'https://pokeapi.co.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('pokemon')
async def pokemon(ctx):
    '''pokemon komutunu çağırdığımızda, program pokemon_resmi_urlsi_al fonksiyonunu çağırır'''
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

def get_tilki_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('fox')
async def fox(ctx):
    '''fox komutunu çağırdığımızda, program tilki_resmi_urlsi_al fonksiyonunu çağırır'''
    image_url = get_tilki_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

bot.run("METHODUNUZ BURAYA")
