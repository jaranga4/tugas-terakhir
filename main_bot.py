import discord
from discord.ext import commands
import random, os 
import model  

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def checkAI(ctx):
    if ctx.message.attacments:
        for file in ctx.message.attachments:
            namafile = file.filename
            urlfile = file.url
            await ctx.save(f'./{namafile}')
            await ctx.send(f'gambar telah disimpan dengan nama {namafile}')
    
            kelas,skor = get_class('keras_model.h5','label.txt',namafile)
    
            if kelas == 'gitar akustik\n' and skor >= 0.75:
                await ctx.send('ini adalah gitar akustik')
                await ctx.send('gitar akustik dapat berbunyi tanpat mengunnakan alat bantuan seperti speaker')
                await ctx.send('harganya sangat murah dapat di beli di toko olah raga atau alat musik')
            elif kelas == 'gitar electric\n' and skor >= 0.75:
                await ctx.send('ini adalah gitar akustik')
                await ctx.send('gitar akustik hanya dapat berbunyi dibantu mengunnakan alat bantuan seperti speaker')
                await ctx.send('harganya lebih mahal jarang ada di toko olah raga tetapi pasti ada di toko alat musik')
            
    else:
        await ctx.send('mana nih gambarnya?????')

bot.run("TOKEN")
