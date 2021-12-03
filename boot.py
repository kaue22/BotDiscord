import discord
from discord.ext import commands

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")

#Evento async para não retornar mensagens do bot
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "palavrão" in message.content:
        await message.channel.snd(f"Por favor,{message.author.name},não ofenda os demais usuários!")

        await message.delete()

    await  bot.process_commands(message)

#Quando digitar o prefixo !oi executa a função send_hello
@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Ola, " + name

    await ctx.send(response)


bot.run("TOKE_AQUI")